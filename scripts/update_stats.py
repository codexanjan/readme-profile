import urllib.request
import json
import os
import re
import time

def fetch_leetcode(username="anjanshetty"):
    query = """
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            profile {
                ranking
            }
            submitStatsGlobal {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
        }
        allQuestionsCount {
            difficulty
            count
        }
    }
    """
    try:
        req = urllib.request.Request(
            "https://leetcode.com/graphql",
            data=json.dumps({"query": query, "variables": {"username": username}}).encode("utf-8"),
            headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            user = data.get("data", {}).get("matchedUser", {})
            subs = user.get("submitStatsGlobal", {}).get("acSubmissionNum", [])
            q_counts = data.get("data", {}).get("allQuestionsCount", [])
            
            stats = {"total": 5, "easy": 4, "medium": 1, "hard": 0}
            totals = {"total": 4046, "easy": 963, "medium": 2111, "hard": 972}
            
            for s in subs:
                diff = s.get("difficulty", "").lower()
                if diff == "all": stats["total"] = s.get("count", 5)
                elif diff == "easy": stats["easy"] = s.get("count", 4)
                elif diff == "medium": stats["medium"] = s.get("count", 1)
                elif diff == "hard": stats["hard"] = s.get("count", 0)
                
            for q in q_counts:
                diff = q.get("difficulty", "").lower()
                if diff == "all": totals["total"] = q.get("count", 4046)
                elif diff == "easy": totals["easy"] = q.get("count", 963)
                elif diff == "medium": totals["medium"] = q.get("count", 2111)
                elif diff == "hard": totals["hard"] = q.get("count", 972)
                
            return stats, totals
    except Exception as e:
        print(f"Warn: LeetCode fetch error ({e}), using last known stats.")
        return {"total": 5, "easy": 4, "medium": 1, "hard": 0}, {"total": 4046, "easy": 963, "medium": 2111, "hard": 972}

def fetch_codewars(username="codexanjan"):
    try:
        req = urllib.request.Request(
            f"https://www.codewars.com/api/v1/users/{username}",
            headers={"User-Agent": "Mozilla/5.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            completed = data.get("codeChallenges", {}).get("totalCompleted", 10)
            rank_name = data.get("ranks", {}).get("overall", {}).get("name", "6 kyu")
            honor = data.get("honor", 143)
            return {"completed": completed, "rank": rank_name, "honor": honor}
    except Exception as e:
        print(f"Warn: CodeWars fetch error ({e}), using last known stats.")
        return {"completed": 10, "rank": "6 kyu", "honor": 143}

def generate_problem_solving_svg(lc_stats, lc_totals, cw_stats):
    lc_total = lc_stats["total"]
    lc_easy = lc_stats["easy"]
    lc_med = lc_stats["medium"]
    lc_hard = lc_stats["hard"]

    tot_easy = lc_totals["easy"]
    tot_med = lc_totals["medium"]
    tot_hard = lc_totals["hard"]

    cw_completed = cw_stats["completed"]
    cw_rank = cw_stats["rank"]

    total_solved_hero = lc_total + cw_completed

    # Gauge geometry (r=36 -> circ ~ 226.2)
    # Milestone base of 50
    dash_val = max(10, min(220, int((total_solved_hero / 50.0) * 226.2)))
    dash_rest = 226 - dash_val

    # Tier bar widths (max width 115)
    w_easy = max(8, min(115, int((lc_easy / max(1, tot_easy)) * 115 * 10))) # scaled for visual visibility
    w_med = max(4, min(115, int((lc_med / max(1, tot_med)) * 115 * 10)))
    w_hard = min(115, int((lc_hard / max(1, tot_hard)) * 115 * 10))

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 495 245" width="495px" height="245px">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;700;800;900&amp;family=Plus+Jakarta+Sans:wght@500;600;700;800&amp;family=JetBrains+Mono:wght@500;700;800&amp;display=swap');

      * {{ box-sizing: border-box; }}
      text {{ font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; user-select: none; }}

      .card-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 13.5px;
        font-weight: 800;
        fill: #facc15;
        letter-spacing: 1.4px;
      }}
      .lc-total-num {{
        font-family: 'Orbitron', sans-serif;
        font-size: 24px;
        font-weight: 900;
        fill: #f8fafc;
      }}
      .lc-total-sub {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 6.5px;
        font-weight: 800;
        fill: #facc15;
        letter-spacing: 0.3px;
      }}
      .tier-label {{
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.2px;
      }}
      .tier-val {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 10.5px;
        font-weight: 700;
        fill: #e2e8f0;
      }}
      .hero-total {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 28px;
        font-weight: 900;
        fill: #f8fafc;
        letter-spacing: 0.5px;
      }}
      .hero-label {{
        font-family: 'Orbitron', sans-serif;
        font-size: 10px;
        font-weight: 800;
        fill: #facc15;
        letter-spacing: 1.3px;
      }}
      .badge-text {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        font-weight: 800;
        fill: #ffffff;
        letter-spacing: 0.5px;
      }}
      .footer-sub {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 9px;
        font-weight: 700;
        fill: #38bdf8;
        letter-spacing: 0.8px;
      }}

      /* Animations */
      .rotate-ring {{
        transform-origin: 76px 138px;
        animation: rotateGauge 12s linear infinite;
      }}
      @keyframes rotateGauge {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}

      .pulse-glow {{
        animation: glowPulse 3s ease-in-out infinite;
      }}
      @keyframes glowPulse {{
        0%, 100% {{ opacity: 0.9; filter: drop-shadow(0 0 3px #facc15); }}
        50% {{ opacity: 1; filter: drop-shadow(0 0 9px #eab308); }}
      }}

      .radar-blip {{
        animation: blipFade 2s ease-in-out infinite;
      }}
      @keyframes blipFade {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.35; transform: scale(0.85); }}
      }}

      .holo-sweep {{
        animation: sweepAnim 4.8s ease-in-out infinite;
      }}
      @keyframes sweepAnim {{
        0% {{ transform: translateX(-400px) skewX(-25deg); opacity: 0; }}
        15% {{ opacity: 0.45; }}
        45% {{ transform: translateX(550px) skewX(-25deg); opacity: 0.45; }}
        60%, 100% {{ transform: translateX(550px) skewX(-25deg); opacity: 0; }}
      }}

      .border-pulse {{
        animation: borderPulseAnim 4s ease-in-out infinite;
      }}
      @keyframes borderPulseAnim {{
        0%, 100% {{ stroke: rgba(250, 204, 21, 0.35); }}
        50% {{ stroke: rgba(250, 204, 21, 0.75); }}
      }}
    </style>

    <linearGradient id="cardBgProb" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e131d" />
      <stop offset="60%" stop-color="#0b0d10" />
      <stop offset="100%" stop-color="#07090c" />
    </linearGradient>

    <linearGradient id="lcGoldRing" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="50%" stop-color="#facc15" />
      <stop offset="100%" stop-color="#ca8a04" />
    </linearGradient>

    <linearGradient id="sheenProb" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#facc15" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>

    <clipPath id="cardProbClip">
      <rect x="0" y="0" width="495" height="245" rx="10" ry="10" />
    </clipPath>
  </defs>

  <g clip-path="url(#cardProbClip)">
    <!-- Card Frame -->
    <rect x="1" y="1" width="493" height="243" rx="9.5" fill="url(#cardBgProb)" stroke="rgba(250, 204, 21, 0.4)" stroke-width="1.5" class="border-pulse" />

    <!-- Tech Grid Lines -->
    <line x1="25" y1="46" x2="470" y2="46" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 4" />
    <line x1="255" y1="46" x2="255" y2="215" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <!-- Header Section -->
    <g transform="translate(25, 28)">
      <circle cx="0" cy="-3" r="5" fill="#22c55e" class="radar-blip" />
      <circle cx="0" cy="-3" r="8" fill="none" stroke="#22c55e" stroke-width="1" stroke-opacity="0.4" class="radar-blip" />
      <text x="16" y="0" class="card-title">ALGORITHMIC DEFENSE</text>
    </g>

    <!-- Top Right Mini Batman Logo Badge -->
    <g transform="translate(458, 25) scale(0.55)" class="pulse-glow" opacity="0.85">
      <path d="M 0 10 C 2.5 8 5.5 6.5 8.5 6 C 12.5 5.5 17 6.5 22 1 C 18 -1.5 13 -1.5 8 -0.5 C 5 -4 3 -5 1.5 -8.5 L 0.8 -5.5 L -0.8 -5.5 L -1.5 -8.5 C -3 -5 -5 -4 -8 -0.5 C -13 -1.5 -18 -1.5 -22 1 C -17 6.5 -12.5 5.5 -8.5 6 C -5.5 6.5 -2.5 8 0 10 Z" fill="#facc15" />
    </g>

    <!-- ================= LEFT COLUMN: LEETCODE BREAKDOWN ================= -->
    <a href="https://leetcode.com/u/anjanshetty/" target="_blank" style="cursor: pointer;">
      <text x="25" y="65" font-family="'Orbitron', sans-serif" font-size="10px" font-weight="700" fill="#facc15" letter-spacing="1px">TOTAL PROBLEMS // @ANJANSHETTY</text>

      <!-- LeetCode Progress Ring (cx=76, cy=138) -->
      <g transform="translate(76, 138)">
        <circle cx="0" cy="0" r="36" fill="none" stroke="#161e2e" stroke-width="5.5" />
        <!-- Active Gauge Ring -->
        <circle cx="0" cy="0" r="36" fill="none" stroke="url(#lcGoldRing)" stroke-width="5.5" stroke-dasharray="{dash_val} {dash_rest}" stroke-linecap="round" class="pulse-glow" transform="rotate(-90)" />
        <!-- Rotating outer dashed orbit -->
        <circle cx="0" cy="0" r="42" fill="none" stroke="#facc15" stroke-width="1.2" stroke-dasharray="4 8" class="rotate-ring" opacity="0.6" />

        <text x="0" y="5" text-anchor="middle" class="lc-total-num">{total_solved_hero}</text>
        <text x="0" y="19" text-anchor="middle" class="lc-total-sub">TOTAL PROBLEMS</text>
      </g>
    </a>

    <!-- LeetCode Tiers (Right of Ring) -->
    <!-- Easy -->
    <g transform="translate(132, 102)">
      <text x="0" y="0" fill="#22c55e" class="tier-label">Easy</text>
      <text x="115" y="0" text-anchor="end" class="tier-val">{lc_easy} / {tot_easy}</text>
      <rect x="0" y="6" width="115" height="5.5" rx="2.5" fill="#161e2e" />
      <rect x="0" y="6" width="{w_easy}" height="5.5" rx="2.5" fill="#22c55e" />
    </g>

    <!-- Medium -->
    <g transform="translate(132, 136)">
      <text x="0" y="0" fill="#eab308" class="tier-label">Medium</text>
      <text x="115" y="0" text-anchor="end" class="tier-val">{lc_med} / {tot_med}</text>
      <rect x="0" y="6" width="115" height="5.5" rx="2.5" fill="#161e2e" />
      <rect x="0" y="6" width="{w_med}" height="5.5" rx="2.5" fill="#eab308" />
    </g>

    <!-- Hard -->
    <g transform="translate(132, 170)">
      <text x="0" y="0" fill="#ef4444" class="tier-label">Hard</text>
      <text x="115" y="0" text-anchor="end" class="tier-val">{lc_hard} / {tot_hard}</text>
      <rect x="0" y="6" width="115" height="5.5" rx="2.5" fill="#161e2e" />
      <rect x="0" y="6" width="{w_hard}" height="5.5" rx="2.5" fill="#ef4444" />
    </g>

    <!-- ================= RIGHT COLUMN: PLATFORM METRICS ================= -->
    <g transform="translate(365, 80)">
      <text x="0" y="0" text-anchor="middle" class="hero-total">{total_solved_hero}+</text>
      <text x="0" y="18" text-anchor="middle" class="hero-label">TOTAL PROBLEMS SOLVED</text>
    </g>

    <!-- Platform Badges -->
    <!-- GeeksforGeeks -->
    <a href="https://www.geeksforgeeks.org/profile/anjanshetty" target="_blank" style="cursor: pointer;">
      <g transform="translate(280, 114)">
        <rect x="0" y="0" width="180" height="23" rx="5" fill="#161e2e" stroke="rgba(34, 197, 94, 0.45)" stroke-width="1" />
        <circle cx="12" cy="11.5" r="4.5" fill="#22c55e" />
        <text x="24" y="15" fill="#cbd5e1" font-size="10.5px" font-weight="600">GeeksforGeeks</text>
        <text x="170" y="15" text-anchor="end" class="badge-text" fill="#22c55e">@anjanshetty</text>
      </g>
    </a>

    <!-- LeetCode -->
    <a href="https://leetcode.com/u/anjanshetty/" target="_blank" style="cursor: pointer;">
      <g transform="translate(280, 143)">
        <rect x="0" y="0" width="180" height="23" rx="5" fill="#161e2e" stroke="rgba(250, 204, 21, 0.45)" stroke-width="1" />
        <circle cx="12" cy="11.5" r="4.5" fill="#facc15" />
        <text x="24" y="15" fill="#cbd5e1" font-size="10.5px" font-weight="600">LeetCode</text>
        <text x="170" y="15" text-anchor="end" class="badge-text" fill="#facc15">{lc_total} Solved</text>
      </g>
    </a>

    <!-- CodeWars -->
    <a href="https://www.codewars.com/users/codexanjan" target="_blank" style="cursor: pointer;">
      <g transform="translate(280, 172)">
        <rect x="0" y="0" width="180" height="23" rx="5" fill="#161e2e" stroke="rgba(239, 68, 68, 0.45)" stroke-width="1" />
        <circle cx="12" cy="11.5" r="4.5" fill="#ef4444" />
        <text x="24" y="15" fill="#cbd5e1" font-size="10.5px" font-weight="600">CodeWars</text>
        <text x="170" y="15" text-anchor="end" class="badge-text" fill="#ef4444">{cw_rank} • {cw_completed} Solved</text>
      </g>
    </a>

    <!-- Bottom Ticker -->
    <line x1="25" y1="214" x2="470" y2="214" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 4" />
    <text x="247" y="232" text-anchor="middle" class="footer-sub">⚡ MAINFRAME: ACTIVE OPERATIVE COMMITTED TO ALGORITHMIC MASTERY</text>

    <!-- Holographic Sheen Sweep -->
    <rect x="0" y="0" width="160" height="260" fill="url(#sheenProb)" class="holo-sweep" pointer-events="none" />
  </g>
</svg>'''
    return svg

def generate_developer_level_svg(total_solved):
    # Dynamic Level & XP calculation
    base_xp = 12000
    earned_xp = total_solved * 45
    total_xp = base_xp + earned_xp
    xp_max = 15000
    level = 20 + int((total_xp - base_xp) / 200)

    circ = 263.9
    xp_ratio = min(0.98, total_xp / xp_max)
    active_dash = int(xp_ratio * circ)
    rem_dash = int(circ - active_dash)

    bar_width = int(xp_ratio * 140)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 495 245" width="495px" height="245px">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600;700;800;900&amp;family=Plus+Jakarta+Sans:wght@500;600;700;800&amp;family=JetBrains+Mono:wght@500;700;800&amp;display=swap');

      * {{ box-sizing: border-box; }}
      text {{ font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; user-select: none; }}

      .card-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 13.5px;
        font-weight: 800;
        fill: #facc15;
        letter-spacing: 1.4px;
      }}
      .skill-name {{
        font-size: 11.5px;
        font-weight: 600;
        fill: #cbd5e1;
        letter-spacing: 0.2px;
      }}
      .skill-val {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        font-weight: 800;
        fill: #f8fafc;
      }}
      .level-num {{
        font-family: 'Orbitron', sans-serif;
        font-size: 26px;
        font-weight: 900;
        fill: #f8fafc;
        letter-spacing: 1px;
      }}
      .level-label {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 8.5px;
        font-weight: 800;
        fill: #facc15;
        letter-spacing: 1.5px;
      }}
      .xp-text {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        font-weight: 700;
        fill: #e2e8f0;
      }}
      .rank-pill-text {{
        font-family: 'Orbitron', sans-serif;
        font-size: 9px;
        font-weight: 800;
        fill: #facc15;
        letter-spacing: 1px;
      }}
      .quest-text {{
        font-size: 10px;
        font-weight: 600;
        fill: #94a3b8;
        letter-spacing: 0.2px;
      }}

      /* Animations */
      .rotate-ring {{
        transform-origin: 382px 105px;
        animation: rotateGauge 12s linear infinite;
      }}
      @keyframes rotateGauge {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}

      .pulse-glow {{
        animation: glowPulse 3s ease-in-out infinite;
      }}
      @keyframes glowPulse {{
        0%, 100% {{ opacity: 0.9; filter: drop-shadow(0 0 3px #facc15); }}
        50% {{ opacity: 1; filter: drop-shadow(0 0 9px #eab308); }}
      }}

      .radar-blip {{
        animation: blipFade 2s ease-in-out infinite;
      }}
      @keyframes blipFade {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.35; transform: scale(0.85); }}
      }}

      .holo-sweep {{
        animation: sweepAnim 4.8s ease-in-out infinite;
      }}
      @keyframes sweepAnim {{
        0% {{ transform: translateX(-400px) skewX(-25deg); opacity: 0; }}
        15% {{ opacity: 0.45; }}
        45% {{ transform: translateX(550px) skewX(-25deg); opacity: 0.45; }}
        60%, 100% {{ transform: translateX(550px) skewX(-25deg); opacity: 0; }}
      }}

      .border-pulse {{
        animation: borderPulseAnim 4s ease-in-out infinite;
      }}
      @keyframes borderPulseAnim {{
        0%, 100% {{ stroke: rgba(250, 204, 21, 0.35); }}
        50% {{ stroke: rgba(250, 204, 21, 0.75); }}
      }}

      .xp-bar-glow {{
        animation: xpBarPulse 3s ease-in-out infinite alternate;
      }}
      @keyframes xpBarPulse {{
        0% {{ filter: drop-shadow(0 0 2px rgba(250, 204, 21, 0.4)); }}
        100% {{ filter: drop-shadow(0 0 6px rgba(250, 204, 21, 0.9)); }}
      }}
    </style>

    <linearGradient id="cardBgDev" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e131d" />
      <stop offset="60%" stop-color="#0b0d10" />
      <stop offset="100%" stop-color="#07090c" />
    </linearGradient>

    <linearGradient id="goldRing" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="50%" stop-color="#facc15" />
      <stop offset="100%" stop-color="#ca8a04" />
    </linearGradient>

    <linearGradient id="sheenDev" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#facc15" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>

    <clipPath id="cardDevClip">
      <rect x="0" y="0" width="495" height="245" rx="10" ry="10" />
    </clipPath>
  </defs>

  <g clip-path="url(#cardDevClip)">
    <!-- Card Frame -->
    <rect x="1" y="1" width="493" height="243" rx="9.5" fill="url(#cardBgDev)" stroke="rgba(250, 204, 21, 0.4)" stroke-width="1.5" class="border-pulse" />

    <!-- Tech Grid Lines -->
    <line x1="25" y1="46" x2="470" y2="46" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 4" />
    <line x1="268" y1="46" x2="268" y2="230" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <!-- Header Section -->
    <g transform="translate(25, 28)">
      <circle cx="0" cy="-3" r="5" fill="#facc15" class="radar-blip" />
      <circle cx="0" cy="-3" r="8" fill="none" stroke="#facc15" stroke-width="1" stroke-opacity="0.4" class="radar-blip" />
      <text x="16" y="0" class="card-title">DEVELOPER LEVEL {level}</text>
    </g>

    <!-- Top Right Mini Batman Logo Badge -->
    <g transform="translate(458, 25) scale(0.55)" class="pulse-glow" opacity="0.85">
      <path d="M 0 10 C 2.5 8 5.5 6.5 8.5 6 C 12.5 5.5 17 6.5 22 1 C 18 -1.5 13 -1.5 8 -0.5 C 5 -4 3 -5 1.5 -8.5 L 0.8 -5.5 L -0.8 -5.5 L -1.5 -8.5 C -3 -5 -5 -4 -8 -0.5 C -13 -1.5 -18 -1.5 -22 1 C -17 6.5 -12.5 5.5 -8.5 6 C -5.5 6.5 -2.5 8 0 10 Z" fill="#facc15" />
    </g>

    <!-- Subheader Tracker -->
    <text x="25" y="65" font-family="'Orbitron', sans-serif" font-size="10.5px" font-weight="700" fill="#facc15" letter-spacing="1px">CODING DNA // CAPABILITIES</text>

    <!-- 1. Algorithms & DSA (90%) -->
    <g transform="translate(25, 84)">
      <text x="0" y="0" class="skill-name">Algorithms &amp; DSA</text>
      <text x="245" y="0" text-anchor="end" class="skill-val">90%</text>
      <rect x="0" y="6" width="245" height="6" rx="3" fill="#161e2e" />
      <rect x="0" y="6" width="220.5" height="6" rx="3" fill="#facc15" />
    </g>

    <!-- 2. AI / ML Engineering (80%) -->
    <g transform="translate(25, 114)">
      <text x="0" y="0" class="skill-name">Applied AI &amp; ML Architecture</text>
      <text x="245" y="0" text-anchor="end" class="skill-val">80%</text>
      <rect x="0" y="6" width="245" height="6" rx="3" fill="#161e2e" />
      <rect x="0" y="6" width="196" height="6" rx="3" fill="#38bdf8" />
    </g>

    <!-- 3. Full-Stack Development (85%) -->
    <g transform="translate(25, 144)">
      <text x="0" y="0" class="skill-name">Full-Stack Web Engineering</text>
      <text x="245" y="0" text-anchor="end" class="skill-val">85%</text>
      <rect x="0" y="6" width="245" height="6" rx="3" fill="#161e2e" />
      <rect x="0" y="6" width="208.2" height="6" rx="3" fill="#10b981" />
    </g>

    <!-- 4. SQL & Data Architecture (90%) -->
    <g transform="translate(25, 174)">
      <text x="0" y="0" class="skill-name">SQL &amp; High-Scale Data</text>
      <text x="245" y="0" text-anchor="end" class="skill-val">90%</text>
      <rect x="0" y="6" width="245" height="6" rx="3" fill="#161e2e" />
      <rect x="0" y="6" width="220.5" height="6" rx="3" fill="#a855f7" />
    </g>

    <!-- 5. Problem Solving (88%) -->
    <g transform="translate(25, 204)">
      <text x="0" y="0" class="skill-name">Algorithmic Problem Solving</text>
      <text x="245" y="0" text-anchor="end" class="skill-val">88%</text>
      <rect x="0" y="6" width="245" height="6" rx="3" fill="#161e2e" />
      <rect x="0" y="6" width="215.6" height="6" rx="3" fill="#f97316" />
    </g>

    <!-- ================= RIGHT COLUMN: LEVEL & QUEST ================= -->
    <!-- Level Circular Gauge (cx=382, cy=105) -->
    <g transform="translate(382, 105)">
      <!-- Track Ring -->
      <circle cx="0" cy="0" r="42" fill="none" stroke="#161e2e" stroke-width="6" />
      <!-- Active XP Ring -->
      <circle cx="0" cy="0" r="42" fill="none" stroke="url(#goldRing)" stroke-width="6" stroke-dasharray="{active_dash} {rem_dash}" stroke-linecap="round" class="pulse-glow" transform="rotate(-90)" />
      <!-- Rotating Outer Dashed Orbit Ring -->
      <circle cx="0" cy="0" r="48" fill="none" stroke="#facc15" stroke-width="1.2" stroke-dasharray="5 9" class="rotate-ring" opacity="0.6" />

      <!-- Inner Level Text -->
      <text x="0" y="6" text-anchor="middle" class="level-num">{level}</text>
      <text x="0" y="21" text-anchor="middle" class="level-label">LEVEL</text>
    </g>

    <!-- XP Bar & Count -->
    <g transform="translate(382, 168)">
      <text x="0" y="0" text-anchor="middle" class="xp-text">{total_xp:,} / {xp_max:,} XP</text>
      <!-- Mini XP Bar Background -->
      <rect x="-70" y="7" width="140" height="5" rx="2.5" fill="#161e2e" />
      <rect x="-70" y="7" width="{bar_width}" height="5" rx="2.5" fill="url(#goldRing)" class="xp-bar-glow" />
    </g>

    <!-- Rank Badge Pill -->
    <g transform="translate(382, 196)">
      <rect x="-75" y="0" width="150" height="20" rx="10" fill="#161e2e" stroke="rgba(250, 204, 21, 0.4)" stroke-width="1" />
      <text x="0" y="13.5" text-anchor="middle" class="rank-pill-text">⚔️ RANK: PROBLEM SOLVER</text>
    </g>

    <!-- Current Quest Note -->
    <g transform="translate(382, 230)">
      <text x="0" y="0" text-anchor="middle" class="quest-text">🚀 Quest: Build things people use</text>
    </g>

    <!-- Holographic Sheen Sweep -->
    <rect x="0" y="0" width="160" height="260" fill="url(#sheenDev)" class="holo-sweep" pointer-events="none" />
  </g>
</svg>'''
    return svg

def update_readme_cache_buster():
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        return
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    ts = str(int(time.time()))
    # Update all batcave SVG cache busters
    for name in [
        "batcave-problem-solving",
        "batcave-developer-level",
        "batcave-hero-banner",
        "batcave-divider-animated",
        "batcave-gadgets-arsenal",
        "batcave-metrics",
        "batcave-streak",
        "batcave-langs-repo",
        "batcave-langs-commit",
        "bat-contribution-snake",
        "batcave-skunkworks-prototypes",
        "batcave-audio-frequency",
        "lanyard"
    ]:
        content = re.sub(
            rf'src="\./assets/{name}\.svg(\?v=[^"]*)?"',
            f'src="./assets/{name}.svg?v={ts}"',
            content
        )

    # Update GIF cache busters
    for name in ["batcave-cinematic-hero"]:
        content = re.sub(
            rf'src="\./assets/{name}\.gif(\?v=[^"]*)?"',
            f'src="./assets/{name}.gif?v={ts}"',
            content
        )

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated README.md cache busters to ?v={ts}")

def main():
    print("=== Fetching Real Stats ===")
    lc_stats, lc_totals = fetch_leetcode("anjanshetty")
    cw_stats = fetch_codewars("codexanjan")
    print(f"LeetCode: {lc_stats}")
    print(f"CodeWars: {cw_stats}")

    total_solved = lc_stats["total"] + cw_stats["completed"]

    os.makedirs("assets", exist_ok=True)

    prob_svg = generate_problem_solving_svg(lc_stats, lc_totals, cw_stats)
    with open("assets/batcave-problem-solving.svg", "w", encoding="utf-8") as f:
        f.write(prob_svg)
    print("Generated assets/batcave-problem-solving.svg")

    dev_svg = generate_developer_level_svg(total_solved)
    with open("assets/batcave-developer-level.svg", "w", encoding="utf-8") as f:
        f.write(dev_svg)
    print("Generated assets/batcave-developer-level.svg")

    try:
        from generate_batman_visuals import create_hero_banner, create_animated_divider, create_arsenal_card
        create_hero_banner()
        create_animated_divider()
        create_arsenal_card()
        from generate_extra_batman_assets import create_skunkworks_card, create_audio_frequency_card
        create_skunkworks_card()
        create_audio_frequency_card()
        print("Generated Batman visual banners, skunkworks card, and audio frequency HUD")
    except Exception as e:
        print("Visual generator note:", e)

    update_readme_cache_buster()

if __name__ == "__main__":
    main()

