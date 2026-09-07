import os

def create_hero_banner():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 260" width="100%" height="260px">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800;900&amp;family=JetBrains+Mono:wght@500;700;800&amp;family=Plus+Jakarta+Sans:wght@600;700;800&amp;display=swap');

      * { box-sizing: border-box; }
      text { user-select: none; }

      .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 38px;
        font-weight: 900;
        letter-spacing: 4px;
        fill: url(#goldGrad);
        filter: drop-shadow(0 0 12px rgba(250, 204, 21, 0.45));
      }
      .hero-tag {
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 3px;
        fill: #94a3b8;
      }
      .hero-sub {
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 1.5px;
        fill: #cbd5e1;
      }
      .hero-motto {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 11.5px;
        font-style: italic;
        font-weight: 600;
        fill: #eab308;
        letter-spacing: 0.8px;
      }
      .hud-metric {
        font-family: 'JetBrains Mono', monospace;
        font-size: 9.5px;
        font-weight: 800;
        fill: #facc15;
        letter-spacing: 1px;
      }
      .hud-label {
        font-family: 'JetBrains Mono', monospace;
        font-size: 8px;
        font-weight: 700;
        fill: #64748b;
        letter-spacing: 0.8px;
      }

      /* Animations */
      .signal-sweep {
        transform-origin: 180px 260px;
        animation: searchlight 8s ease-in-out infinite alternate;
      }
      @keyframes searchlight {
        0% { transform: rotate(-18deg); opacity: 0.7; }
        50% { transform: rotate(12deg); opacity: 0.95; }
        100% { transform: rotate(-8deg); opacity: 0.75; }
      }

      .pulse-gold {
        animation: goldGlow 3s ease-in-out infinite alternate;
      }
      @keyframes goldGlow {
        0% { filter: drop-shadow(0 0 4px #facc15); opacity: 0.85; }
        100% { filter: drop-shadow(0 0 16px #eab308); opacity: 1; }
      }

      .radar-spin {
        transform-origin: 875px 55px;
        animation: radarSpinAnim 6s linear infinite;
      }
      @keyframes radarSpinAnim {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
      }

      .holo-sweep {
        animation: sweepAnim 5s ease-in-out infinite;
      }
      @keyframes sweepAnim {
        0% { transform: translateX(-600px) skewX(-25deg); opacity: 0; }
        15% { opacity: 0.4; }
        45% { transform: translateX(1100px) skewX(-25deg); opacity: 0.4; }
        60%, 100% { transform: translateX(1100px) skewX(-25deg); opacity: 0; }
      }

      .border-pulse {
        animation: borderAnim 4s ease-in-out infinite;
      }
      @keyframes borderAnim {
        0%, 100% { stroke: rgba(250, 204, 21, 0.35); }
        50% { stroke: rgba(250, 204, 21, 0.85); filter: drop-shadow(0 0 6px rgba(250, 204, 21, 0.5)); }
      }
    </style>

    <linearGradient id="bannerBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e131d" />
      <stop offset="45%" stop-color="#0b0d10" />
      <stop offset="85%" stop-color="#080a0d" />
      <stop offset="100%" stop-color="#040507" />
    </linearGradient>

    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="35%" stop-color="#facc15" />
      <stop offset="70%" stop-color="#eab308" />
      <stop offset="100%" stop-color="#ca8a04" />
    </linearGradient>

    <linearGradient id="searchBeam" x1="0%" y1="100%" x2="50%" y2="0%">
      <stop offset="0%" stop-color="#facc15" stop-opacity="0.5" />
      <stop offset="60%" stop-color="#eab308" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#fef08a" stop-opacity="0.02" />
    </linearGradient>

    <linearGradient id="sheenHero" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#facc15" stop-opacity="0.35" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>

    <clipPath id="bannerClip">
      <rect x="0" y="0" width="960" height="260" rx="12" ry="12" />
    </clipPath>
  </defs>

  <g clip-path="url(#bannerClip)">
    <!-- Base Background -->
    <rect x="1" y="1" width="958" height="258" rx="11.5" fill="url(#bannerBg)" stroke="rgba(250, 204, 21, 0.4)" stroke-width="1.5" class="border-pulse" />

    <!-- Gotham Skyscraper Silhouettes (Background Skyline) -->
    <g fill="#07090c" opacity="0.9">
      <rect x="60" y="140" width="35" height="120" />
      <rect x="98" y="115" width="45" height="145" />
      <polygon points="120,80 115,115 125,115" fill="#07090c" />
      <rect x="145" y="150" width="30" height="110" />
      <rect x="180" y="130" width="50" height="130" />
      <rect x="235" y="160" width="40" height="100" />
      <rect x="680" y="145" width="42" height="115" />
      <rect x="725" y="120" width="55" height="140" />
      <polygon points="752,90 748,120 756,120" fill="#07090c" />
      <rect x="785" y="155" width="38" height="105" />
      <rect x="828" y="135" width="48" height="125" />
    </g>

    <!-- Searchlight / Bat-Signal Beam Sweeping Night Sky -->
    <g class="signal-sweep">
      <polygon points="180,260 80,10 280,10" fill="url(#searchBeam)" />
      <!-- Cloud Spotlight Oval -->
      <ellipse cx="180" cy="20" rx="80" ry="25" fill="#facc15" opacity="0.25" filter="blur(8px)" />
      <!-- Projected Bat Insignia in Spotlight -->
      <g transform="translate(180, 20) scale(0.65)" opacity="0.75">
        <path d="M 0 10 C 2.5 8 5.5 6.5 8.5 6 C 12.5 5.5 17 6.5 22 1 C 18 -1.5 13 -1.5 8 -0.5 C 5 -4 3 -5 1.5 -8.5 L 0.8 -5.5 L -0.8 -5.5 L -1.5 -8.5 C -3 -5 -5 -4 -8 -0.5 C -13 -1.5 -18 -1.5 -22 1 C -17 6.5 -12.5 5.5 -8.5 6 C -5.5 6.5 -2.5 8 0 10 Z" fill="#0b0d10" />
      </g>
    </g>

    <!-- Subtle Tech Circuit Grid Lines -->
    <line x1="30" y1="42" x2="930" y2="42" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 6" />
    <line x1="30" y1="218" x2="930" y2="218" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 6" />
    <line x1="680" y1="42" x2="680" y2="218" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 4" />

    <!-- Corner Cybernetic Reticles -->
    <!-- Top-Left -->
    <path d="M 12 28 L 12 12 L 28 12" stroke="#facc15" stroke-width="2" fill="none" />
    <!-- Top-Right -->
    <path d="M 948 28 L 948 12 L 932 12" stroke="#facc15" stroke-width="2" fill="none" />
    <!-- Bottom-Left -->
    <path d="M 12 232 L 12 248 L 28 248" stroke="#facc15" stroke-width="2" fill="none" />
    <!-- Bottom-Right -->
    <path d="M 948 232 L 948 248 L 932 248" stroke="#facc15" stroke-width="2" fill="none" />

    <!-- Top Status Bar -->
    <g transform="translate(35, 27)">
      <circle cx="0" cy="0" r="4" fill="#22c55e" />
      <circle cx="0" cy="0" r="7" fill="none" stroke="#22c55e" stroke-width="1" opacity="0.5" />
      <text x="14" y="3.5" class="hero-tag">WAYNE ENTERPRISES // SEC-OPS MAINFRAME v4.2</text>
    </g>

    <!-- Center-Left: Identity & Mission -->
    <g transform="translate(48, 88)">
      <!-- Animated Center Batman Logo -->
      <g transform="translate(0, -6) scale(0.95)" class="pulse-gold">
        <path d="M 0 14 C 4 11 9 9 14 8 C 20 7 27 9 35 1 C 29 -2 21 -2 13 -1 C 8 -6 5 -8 2 -13 L 1 -8 L -1 -8 L -2 -13 C -5 -8 -8 -6 -13 -1 C -21 -2 -29 -2 -35 1 C -27 9 -20 7 -14 8 C -9 9 -4 11 0 14 Z" fill="url(#goldGrad)" />
      </g>

      <!-- Name & Title -->
      <text x="48" y="2" class="hero-title">ANJAN SHETTY</text>
      <text x="50" y="28" class="hero-sub">FULL-STACK ARCHITECT // APPLIED AI &amp; SCALABLE SYSTEMS</text>
      <text x="50" y="52" class="hero-motto">"The night is darkest before the code compiles. Building in the dark, shipping into the light."</text>
    </g>

    <!-- Right Column: Live Telemetry HUD -->
    <!-- Radar Scanner (cx=875, cy=55) -->
    <g transform="translate(735, 62)">
      <!-- Radar Circle -->
      <circle cx="140" cy="0" r="28" fill="#101520" stroke="#1e293b" stroke-width="1.5" />
      <circle cx="140" cy="0" r="18" fill="none" stroke="#facc15" stroke-width="1" opacity="0.3" stroke-dasharray="2 4" />
      <line x1="112" y1="0" x2="168" y2="0" stroke="#1e293b" stroke-width="1" />
      <line x1="140" y1="-28" x2="140" y2="28" stroke="#1e293b" stroke-width="1" />
      <line x1="140" y1="0" x2="160" y2="-18" stroke="#facc15" stroke-width="1.5" class="radar-spin" />
      <circle cx="152" cy="-10" r="2.5" fill="#22c55e" />

      <!-- HUD Telemetry Metrics -->
      <g transform="translate(0, -10)">
        <text x="0" y="0" class="hud-label">SECURITY CLEARANCE</text>
        <text x="0" y="14" class="hud-metric">LEVEL 10 // OMEGA</text>
      </g>
      <g transform="translate(0, 26)">
        <text x="0" y="0" class="hud-label">TACTICAL CODENAME</text>
        <text x="0" y="14" class="hud-metric">CODEXANJAN</text>
      </g>
      <g transform="translate(0, 62)">
        <text x="0" y="0" class="hud-label">HEADQUARTERS</text>
        <text x="0" y="14" class="hud-metric">BATCAVE // GOTHAM</text>
      </g>
      <g transform="translate(0, 98)">
        <text x="0" y="0" class="hud-label">MAINFRAME STATUS</text>
        <text x="0" y="14" class="hud-metric" fill="#22c55e">ONLINE // DEPLOYED</text>
      </g>
    </g>

    <!-- Bottom Ticker -->
    <g transform="translate(35, 238)">
      <text x="0" y="0" font-family="'JetBrains Mono', monospace" font-size="9.5px" font-weight="700" fill="#facc15" letter-spacing="1.2px">⚡ BATCAVE INTELLIGENCE: 16+ VERIFIED DSA DIRECTIVES • 4 PRODUCTION REPOSITORIES • LIVE HUD TELEMETRY</text>
    </g>

    <!-- Holographic Light Sweep -->
    <rect x="0" y="0" width="220" height="280" fill="url(#sheenHero)" class="holo-sweep" pointer-events="none" />
  </g>
</svg>'''
    with open("assets/batcave-hero-banner.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Created assets/batcave-hero-banner.svg")

def create_animated_divider():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 32" width="100%" height="32px" fill="none">
  <defs>
    <style>
      .divider-pulse {
        animation: beamPulse 3s ease-in-out infinite alternate;
      }
      @keyframes beamPulse {
        0% { opacity: 0.6; }
        100% { opacity: 1; filter: drop-shadow(0 0 5px #facc15); }
      }
      .bat-glow {
        animation: batGlowAnim 2.5s ease-in-out infinite alternate;
      }
      @keyframes batGlowAnim {
        0% { transform: scale(1); filter: drop-shadow(0 0 2px #facc15); }
        100% { transform: scale(1.08); filter: drop-shadow(0 0 10px #eab308); }
      }
      .laser-travel-left {
        animation: laserLeft 3.5s linear infinite;
      }
      @keyframes laserLeft {
        0% { transform: translateX(0); opacity: 0; }
        30% { opacity: 0.9; }
        70% { opacity: 0.9; }
        100% { transform: translateX(-400px); opacity: 0; }
      }
      .laser-travel-right {
        animation: laserRight 3.5s linear infinite;
      }
      @keyframes laserRight {
        0% { transform: translateX(0); opacity: 0; }
        30% { opacity: 0.9; }
        70% { opacity: 0.9; }
        100% { transform: translateX(400px); opacity: 0; }
      }
    </style>

    <linearGradient id="beamGradLeft" x1="100%" y1="0%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#facc15" stop-opacity="0.9" />
      <stop offset="60%" stop-color="#eab308" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#ca8a04" stop-opacity="0" />
    </linearGradient>

    <linearGradient id="beamGradRight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#facc15" stop-opacity="0.9" />
      <stop offset="60%" stop-color="#eab308" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#ca8a04" stop-opacity="0" />
    </linearGradient>

    <filter id="laserGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Left & Right Main Guide Beams -->
  <line x1="30" y1="16" x2="445" y2="16" stroke="url(#beamGradLeft)" stroke-width="1.8" class="divider-pulse" />
  <line x1="515" y1="16" x2="930" y2="16" stroke="url(#beamGradRight)" stroke-width="1.8" class="divider-pulse" />

  <!-- Outward Traveling Laser Pulses -->
  <circle cx="440" cy="16" r="3.5" fill="#fef08a" filter="url(#laserGlow)" class="laser-travel-left" />
  <circle cx="520" cy="16" r="3.5" fill="#fef08a" filter="url(#laserGlow)" class="laser-travel-right" />

  <!-- Tech Precision Tick Marks -->
  <circle cx="60" cy="16" r="1.5" fill="#facc15" opacity="0.6" />
  <circle cx="160" cy="16" r="1.5" fill="#facc15" opacity="0.6" />
  <circle cx="800" cy="16" r="1.5" fill="#facc15" opacity="0.6" />
  <circle cx="900" cy="16" r="1.5" fill="#facc15" opacity="0.6" />

  <line x1="110" y1="12" x2="110" y2="20" stroke="#facc15" stroke-width="1.2" opacity="0.5" />
  <line x1="850" y1="12" x2="850" y2="20" stroke="#facc15" stroke-width="1.2" opacity="0.5" />

  <!-- Center Batman Emblem with Dynamic Glow -->
  <g transform="translate(480, 16)" class="bat-glow" style="transform-origin: 480px 16px;">
    <!-- Diamond Backing Frame -->
    <polygon points="0,-13 22,0 0,13 -22,0" fill="#0e131d" stroke="#facc15" stroke-width="1.2" />
    <!-- Bat Silhouette -->
    <path d="M 0 6 C 1.8 4.8 4 4 6 3.8 C 9 3.5 12 4.2 16 0.8 C 13 -0.8 9.5 -0.8 6 -0.3 C 3.8 -2.8 2.2 -3.5 1 -6 L 0.5 -3.8 L -0.5 -3.8 L -1 -6 C -2.2 -3.5 -3.8 -2.8 -6 -0.3 C -9.5 -0.8 -13 -0.8 -16 0.8 C -12 4.2 -9 3.5 -6 3.8 C -4 4 -1.8 4.8 0 6 Z" fill="#facc15" />
  </g>
</svg>'''
    with open("assets/batcave-divider-animated.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Created assets/batcave-divider-animated.svg")

def create_arsenal_card():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 220" width="100%" height="220px">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800;900&amp;family=JetBrains+Mono:wght@500;700;800&amp;display=swap');

      * { box-sizing: border-box; }
      text { font-family: 'JetBrains Mono', monospace; user-select: none; }

      .card-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 13.5px;
        font-weight: 800;
        fill: #facc15;
        letter-spacing: 1.4px;
      }
      .col-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 10.5px;
        font-weight: 800;
        fill: #facc15;
        letter-spacing: 1px;
      }
      .item-label {
        font-size: 10.5px;
        font-weight: 700;
        fill: #94a3b8;
      }
      .item-val {
        font-size: 11px;
        font-weight: 800;
        fill: #f8fafc;
      }
      .spec-pill {
        font-size: 9px;
        font-weight: 800;
        fill: #facc15;
      }

      .pulse-glow {
        animation: glowPulse 3s ease-in-out infinite;
      }
      @keyframes glowPulse {
        0%, 100% { opacity: 0.9; filter: drop-shadow(0 0 3px #facc15); }
        50% { opacity: 1; filter: drop-shadow(0 0 9px #eab308); }
      }

      .holo-sweep {
        animation: sweepAnim 4.8s ease-in-out infinite;
      }
      @keyframes sweepAnim {
        0% { transform: translateX(-600px) skewX(-25deg); opacity: 0; }
        15% { opacity: 0.45; }
        45% { transform: translateX(1100px) skewX(-25deg); opacity: 0.45; }
        60%, 100% { transform: translateX(1100px) skewX(-25deg); opacity: 0; }
      }

      .border-pulse {
        animation: borderPulseAnim 4s ease-in-out infinite;
      }
      @keyframes borderPulseAnim {
        0%, 100% { stroke: rgba(250, 204, 21, 0.35); }
        50% { stroke: rgba(250, 204, 21, 0.75); }
      }
    </style>

    <linearGradient id="cardBgArsenal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e131d" />
      <stop offset="60%" stop-color="#0b0d10" />
      <stop offset="100%" stop-color="#07090c" />
    </linearGradient>

    <linearGradient id="sheenArsenal" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#facc15" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>

    <clipPath id="cardArsenalClip">
      <rect x="0" y="0" width="960" height="220" rx="10" ry="10" />
    </clipPath>
  </defs>

  <g clip-path="url(#cardArsenalClip)">
    <!-- Card Frame -->
    <rect x="1" y="1" width="958" height="218" rx="9.5" fill="url(#cardBgArsenal)" stroke="rgba(250, 204, 21, 0.4)" stroke-width="1.5" class="border-pulse" />

    <!-- Tech Grid Lines -->
    <line x1="25" y1="42" x2="935" y2="42" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 4" />
    <line x1="315" y1="42" x2="315" y2="190" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />
    <line x1="635" y1="42" x2="635" y2="190" stroke="#1e293b" stroke-width="1" stroke-dasharray="3 3" />

    <!-- Header Section -->
    <g transform="translate(25, 26)">
      <circle cx="0" cy="-3" r="5" fill="#facc15" class="pulse-glow" />
      <circle cx="0" cy="-3" r="8" fill="none" stroke="#facc15" stroke-width="1" stroke-opacity="0.4" />
      <text x="16" y="0" class="card-title">BATCAVE WORKSTATION // TACTICAL GADGET ARSENAL</text>
    </g>

    <!-- Top Right Mini Batman Logo Badge -->
    <g transform="translate(920, 24) scale(0.55)" class="pulse-glow" opacity="0.85">
      <path d="M 0 10 C 2.5 8 5.5 6.5 8.5 6 C 12.5 5.5 17 6.5 22 1 C 18 -1.5 13 -1.5 8 -0.5 C 5 -4 3 -5 1.5 -8.5 L 0.8 -5.5 L -0.8 -5.5 L -1.5 -8.5 C -3 -5 -5 -4 -8 -0.5 C -13 -1.5 -18 -1.5 -22 1 C -17 6.5 -12.5 5.5 -8.5 6 C -5.5 6.5 -2.5 8 0 10 Z" fill="#facc15" />
    </g>

    <!-- Column 1: Core System & Terminal -->
    <g transform="translate(30, 68)">
      <text x="0" y="0" class="col-header">🖥️ SYSTEM CORE &amp; KERNEL</text>
      
      <g transform="translate(0, 24)">
        <text x="0" y="0" class="item-label">PRIMARY OS</text>
        <text x="0" y="15" class="item-val">Ubuntu Linux LTS • Win11 Dual-Core</text>
      </g>
      
      <g transform="translate(0, 64)">
        <text x="0" y="0" class="item-label">COMMAND TERMINAL</text>
        <text x="0" y="15" class="item-val">Zsh • Starship Prompt • PowerShell 7</text>
      </g>
    </g>

    <!-- Column 2: Code Rig & Architecture -->
    <g transform="translate(345, 68)">
      <text x="0" y="0" class="col-header">⚡ CODE RIG &amp; TOOLING</text>
      
      <g transform="translate(0, 24)">
        <text x="0" y="0" class="item-label">PRIMARY EDITORS</text>
        <text x="0" y="15" class="item-val">VS Code (Dark Knight) • Neovim Lua</text>
      </g>
      
      <g transform="translate(0, 64)">
        <text x="0" y="0" class="item-label">CONTAINER &amp; CI/CD</text>
        <text x="0" y="15" class="item-val">Docker Engine • GitHub Actions</text>
      </g>
    </g>

    <!-- Column 3: Security & Tactical Creed -->
    <g transform="translate(665, 68)">
      <text x="0" y="0" class="col-header">🛡️ SECURITY &amp; DIRECTIVES</text>
      
      <g transform="translate(0, 24)">
        <text x="0" y="0" class="item-label">CRYPTOGRAPHIC VAULT</text>
        <text x="0" y="15" class="item-val">SSH ED25519 • GPG Signed Commits</text>
      </g>
      
      <g transform="translate(0, 64)">
        <text x="0" y="0" class="item-label">OPERATIVE PHILOSOPHY</text>
        <text x="0" y="15" class="item-val" fill="#facc15">"Ship robust code into the light."</text>
      </g>
    </g>

    <!-- Bottom Status Ticker -->
    <line x1="25" y1="192" x2="935" y2="192" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 4" />
    <text x="480" y="208" text-anchor="middle" font-size="9px" font-weight="700" fill="#38bdf8" letter-spacing="1px">⚡ WAYNE ENTERPRISES SEC-OP PROTOCOLS ACTIVE • CONTINUOUS CONTINUOUS INTEGRATION NOMINAL</text>

    <!-- Holographic Sheen Sweep -->
    <rect x="0" y="0" width="220" height="240" fill="url(#sheenArsenal)" class="holo-sweep" pointer-events="none" />
  </g>
</svg>'''
    with open("assets/batcave-gadgets-arsenal.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Created assets/batcave-gadgets-arsenal.svg")

if __name__ == "__main__":
    create_hero_banner()
    create_animated_divider()
    create_arsenal_card()
