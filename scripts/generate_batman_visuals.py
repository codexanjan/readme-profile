import os

def create_hero_banner():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 260" width="100%" height="260px">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800;900&amp;family=JetBrains+Mono:wght@500;700;800&amp;family=Plus+Jakarta+Sans:wght@600;700;800&amp;display=swap');

      * { box-sizing: border-box; }
      text { user-select: none; }

      .hero-title {
        font-family: 'Orbitron', -apple-system, sans-serif;
        font-size: 46px;
        font-weight: 900;
        letter-spacing: 6px;
        fill: url(#goldGrad);
        filter: drop-shadow(0 0 16px rgba(250, 204, 21, 0.75)) drop-shadow(0 0 30px rgba(234, 179, 8, 0.45));
      }
      .hero-tag {
        font-family: 'JetBrains Mono', monospace;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 2.5px;
        fill: #94a3b8;
      }
      .hero-sub {
        font-family: 'JetBrains Mono', monospace;
        font-size: 13.5px;
        font-weight: 700;
        letter-spacing: 1.8px;
        fill: #f8fafc;
      }
      .hero-motto {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        font-weight: 600;
        fill: #eab308;
        letter-spacing: 0.8px;
      }
      .tag-pill {
        font-family: 'JetBrains Mono', monospace;
        font-size: 9px;
        font-weight: 800;
        fill: #facc15;
        letter-spacing: 1px;
      }
      .radar-text {
        font-family: 'JetBrains Mono', monospace;
        font-size: 8px;
        font-weight: 800;
        fill: #94a3b8;
        letter-spacing: 0.8px;
      }

      /* Animations */
      .spotlight-sweep {
        transform-origin: 60px 260px;
        animation: spotSweepAnim 7s ease-in-out infinite alternate;
      }
      @keyframes spotSweepAnim {
        0% { transform: rotate(-8deg); opacity: 0.7; }
        50% { transform: rotate(8deg); opacity: 0.95; }
        100% { transform: rotate(-2deg); opacity: 0.8; }
      }

      .name-pulse {
        animation: nameGlow 3s ease-in-out infinite alternate;
      }
      @keyframes nameGlow {
        0% { filter: drop-shadow(0 0 12px rgba(250, 204, 21, 0.55)); }
        100% { filter: drop-shadow(0 0 24px rgba(250, 204, 21, 0.95)) drop-shadow(0 0 45px rgba(234, 179, 8, 0.6)); }
      }

      .right-bat-glowing {
        transform-origin: 0px 0px;
        animation: rightBatGlowAnim 2.5s ease-in-out infinite alternate;
      }
      @keyframes rightBatGlowAnim {
        0% { transform: scale(1); filter: drop-shadow(0 0 6px #facc15) drop-shadow(0 0 14px rgba(234, 179, 8, 0.6)); }
        100% { transform: scale(1.12); filter: drop-shadow(0 0 14px #fef08a) drop-shadow(0 0 28px #facc15) drop-shadow(0 0 48px #ca8a04); }
      }

      .radar-sweep-needle {
        transform-origin: 0px 0px;
        animation: radarNeedleAnim 5s linear infinite;
      }
      @keyframes radarNeedleAnim {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
      }

      .radar-blip-pulse {
        animation: blipAnim 1.8s ease-in-out infinite;
      }
      @keyframes blipAnim {
        0%, 100% { opacity: 0.3; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1.3); filter: drop-shadow(0 0 4px #22c55e); }
      }

      .holo-sweep {
        animation: sweepAnim 5s ease-in-out infinite;
      }
      @keyframes sweepAnim {
        0% { transform: translateX(-600px) skewX(-25deg); opacity: 0; }
        15% { opacity: 0.35; }
        45% { transform: translateX(1100px) skewX(-25deg); opacity: 0.35; }
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
      <stop offset="0%" stop-color="#ffffff" />
      <stop offset="25%" stop-color="#fef08a" />
      <stop offset="55%" stop-color="#facc15" />
      <stop offset="85%" stop-color="#eab308" />
      <stop offset="100%" stop-color="#ca8a04" />
    </linearGradient>

    <!-- Volumetric Spotlight Cone Gradient focused on Name -->
    <linearGradient id="spotlightBeamGrad" x1="0%" y1="100%" x2="40%" y2="0%">
      <stop offset="0%" stop-color="#facc15" stop-opacity="0.6" />
      <stop offset="45%" stop-color="#eab308" stop-opacity="0.3" />
      <stop offset="85%" stop-color="#fef08a" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#fef08a" stop-opacity="0" />
    </linearGradient>

    <!-- Radial Glow Backdrop directly behind Name -->
    <radialGradient id="nameSpotlightRadial" cx="45%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#facc15" stop-opacity="0.35" />
      <stop offset="40%" stop-color="#eab308" stop-opacity="0.18" />
      <stop offset="80%" stop-color="#0b0d10" stop-opacity="0.05" />
      <stop offset="100%" stop-color="#0b0d10" stop-opacity="0" />
    </radialGradient>

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
    <g fill="#07090c" opacity="0.95">
      <rect x="40" y="140" width="40" height="120" />
      <rect x="85" y="110" width="48" height="150" />
      <polygon points="109,70 103,110 115,110" fill="#07090c" />
      <rect x="138" y="148" width="35" height="112" />
      <rect x="178" y="125" width="55" height="135" />
      <rect x="238" y="155" width="45" height="105" />
      <rect x="288" y="135" width="50" height="125" />
      <!-- Building glowing windows -->
      <circle cx="98" cy="125" r="1.5" fill="#facc15" opacity="0.6" />
      <circle cx="110" cy="138" r="1.5" fill="#facc15" opacity="0.4" />
      <circle cx="122" cy="150" r="1.5" fill="#facc15" opacity="0.5" />
      <circle cx="195" cy="140" r="1.5" fill="#facc15" opacity="0.5" />
      <circle cx="210" cy="155" r="1.5" fill="#facc15" opacity="0.4" />

      <!-- Right skyline -->
      <rect x="580" y="150" width="40" height="110" />
      <rect x="625" y="130" width="45" height="130" />
      <rect x="675" y="140" width="42" height="120" />
      <rect x="722" y="115" width="55" height="145" />
      <polygon points="750,80 744,115 756,115" fill="#07090c" />
      <rect x="782" y="148" width="38" height="112" />
      <rect x="825" y="128" width="52" height="132" />
      <rect x="882" y="158" width="38" height="102" />
      <!-- Right windows -->
      <circle cx="735" cy="130" r="1.5" fill="#facc15" opacity="0.5" />
      <circle cx="750" cy="145" r="1.5" fill="#facc15" opacity="0.6" />
      <circle cx="765" cy="160" r="1.5" fill="#facc15" opacity="0.4" />
      <circle cx="842" cy="142" r="1.5" fill="#facc15" opacity="0.5" />
    </g>

    <!-- FULL SPOTLIGHT BEAM ILLUMINATING THE NAME -->
    <g class="spotlight-sweep">
      <!-- Broad volumetric searchlight cone shining directly over the name -->
      <polygon points="60,260 0,0 480,0" fill="url(#spotlightBeamGrad)" />
      <!-- Intense spotlight core cone -->
      <polygon points="120,260 80,40 380,40" fill="url(#spotlightBeamGrad)" opacity="0.75" />
    </g>

    <!-- Radial Spotlight Aura centered directly behind ANJAN SHETTY -->
    <ellipse cx="270" cy="98" rx="260" ry="68" fill="url(#nameSpotlightRadial)" />

    <!-- Subtle Tech Circuit Grid Lines -->
    <line x1="30" y1="42" x2="930" y2="42" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 6" />
    <line x1="30" y1="218" x2="930" y2="218" stroke="#1e293b" stroke-width="1" stroke-dasharray="4 6" />

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
      <!-- Right side telemetry coordinates -->
      <text x="590" y="3.5" class="hero-tag" fill="#eab308">[ GOTHAM SECTOR 04 // DEFCON 1 • 40.7128° N, 74.0060° W ]</text>
    </g>

    <!-- Center-Left: Spotlighted Identity & Mission (NO LEFT BAT) -->
    <g transform="translate(48, 86)">
      <!-- Name in Full Spotlight with radiant pulse -->
      <g class="name-pulse">
        <text x="0" y="4" class="hero-title">ANJAN SHETTY</text>
      </g>
      <text x="2" y="33" class="hero-sub">FULL-STACK ARCHITECT // APPLIED AI &amp; SCALABLE SYSTEMS</text>
      <text x="2" y="56" class="hero-motto">"The night is darkest before the code compiles. Building in the dark, shipping into the light."</text>

      <!-- Tactical Tag Pills -->
      <g transform="translate(2, 71)">
        <rect x="0" y="0" width="112" height="20" rx="4" fill="#101520" stroke="rgba(250, 204, 21, 0.4)" stroke-width="1" />
        <text x="10" y="13.5" class="tag-pill">⚡ FULL-STACK</text>

        <rect x="122" y="0" width="168" height="20" rx="4" fill="#101520" stroke="rgba(250, 204, 21, 0.4)" stroke-width="1" />
        <text x="132" y="13.5" class="tag-pill">🛡️ DISTRIBUTED SYSTEMS</text>

        <rect x="300" y="0" width="124" height="20" rx="4" fill="#101520" stroke="rgba(250, 204, 21, 0.4)" stroke-width="1" />
        <text x="310" y="13.5" class="tag-pill">🧠 APPLIED AI/ML</text>

        <rect x="434" y="0" width="128" height="20" rx="4" fill="#101520" stroke="rgba(250, 204, 21, 0.4)" stroke-width="1" />
        <text x="444" y="13.5" class="tag-pill">🚀 OPEN SOURCE</text>
      </g>
    </g>

    <!-- RIGHT SIDE: PROMINENT GLOWING BAT LOGO + CYBERNETIC ROTATING RADAR HUD -->
    <!-- 1. Glowing Bat Logo (x=690, y=125) -->
    <g transform="translate(680, 125)">
      <!-- Outer Hex/Diamond Frame -->
      <polygon points="0,-48 48,0 0,48 -48,0" stroke="#facc15" stroke-width="1.2" fill="#101520" opacity="0.9" />
      <polygon points="0,-40 40,0 0,40 -40,0" stroke="#eab308" stroke-width="0.8" fill="none" opacity="0.4" stroke-dasharray="3 3" />
      <!-- Corner ticks -->
      <line x1="-54" y1="0" x2="-44" y2="0" stroke="#facc15" stroke-width="1.5" />
      <line x1="44" y1="0" x2="54" y2="0" stroke="#facc15" stroke-width="1.5" />
      <line x1="0" y1="-54" x2="0" y2="-44" stroke="#facc15" stroke-width="1.5" />
      <line x1="0" y1="44" x2="0" y2="54" stroke="#facc15" stroke-width="1.5" />

      <!-- Prominent Glowing Gold Batman Silhouette -->
      <g class="right-bat-glowing" style="transform-origin: 0px 0px;">
        <path d="M 0 16 C 4.5 12.5 10 10 16 9 C 23 8 31 10 40 1 C 33 -2.5 24 -2.5 15 -1 C 9 -7 6 -9 2 -15 L 1 -9 L -1 -9 L -2 -15 C -6 -9 -9 -7 -15 -1 C -24 -2.5 -33 -2.5 -40 1 C -31 10 -23 8 -16 9 C -10 10 -4.5 12.5 0 16 Z" fill="url(#goldGrad)" />
      </g>
      <text x="0" y="62" text-anchor="middle" font-family="'JetBrains Mono', monospace" font-size="8.5px" font-weight="800" fill="#facc15" letter-spacing="1.2px">BAT-SIGNAL // 100%</text>
    </g>

    <!-- 2. High-Tech Rotating Radar (x=845, y=125) -->
    <g transform="translate(845, 120)">
      <!-- Radar Concentric Rings -->
      <circle cx="0" cy="0" r="34" fill="#0b0e14" stroke="#1e293b" stroke-width="1.5" />
      <circle cx="0" cy="0" r="23" fill="none" stroke="#facc15" stroke-width="1" opacity="0.3" stroke-dasharray="2 3" />
      <circle cx="0" cy="0" r="12" fill="none" stroke="#22c55e" stroke-width="0.8" opacity="0.4" />

      <!-- Crosshairs -->
      <line x1="-34" y1="0" x2="34" y2="0" stroke="#1e293b" stroke-width="1" />
      <line x1="0" y1="-34" x2="0" y2="34" stroke="#1e293b" stroke-width="1" />

      <!-- Rotating Sweep Needle -->
      <g class="radar-sweep-needle">
        <line x1="0" y1="0" x2="30" y2="-12" stroke="#22c55e" stroke-width="1.8" />
        <polygon points="0,0 28,-18 32,-8" fill="#22c55e" opacity="0.25" />
      </g>

      <!-- Blip 1: Green Active Target -->
      <g transform="translate(14, -14)" class="radar-blip-pulse">
        <circle cx="0" cy="0" r="3" fill="#22c55e" />
        <circle cx="0" cy="0" r="6" fill="none" stroke="#22c55e" stroke-width="1" />
      </g>
      <!-- Blip 2: Gold Secondary Ping -->
      <circle cx="-16" cy="12" r="2" fill="#facc15" opacity="0.8" />

      <!-- Radar Telemetry Labels -->
      <text x="0" y="-42" text-anchor="middle" class="radar-text" fill="#22c55e">RADAR: ACTIVE SWEEP</text>
      <text x="0" y="47" text-anchor="middle" class="radar-text" fill="#facc15">LOCK: ACQUIRED</text>
      <text x="0" y="58" text-anchor="middle" class="radar-text" fill="#64748b">RANGE: 25 KM</text>
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
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 40" width="100%" height="40px" fill="none">
  <defs>
    <style>
      .divider-pulse {
        animation: beamPulse 3s ease-in-out infinite alternate;
      }
      @keyframes beamPulse {
        0% { opacity: 0.55; }
        100% { opacity: 1; filter: drop-shadow(0 0 6px #facc15); }
      }
      .bat-center-glow {
        transform-origin: 0px 0px;
        animation: batGlowAnim 2.6s ease-in-out infinite alternate;
      }
      @keyframes batGlowAnim {
        0% { transform: scale(1); filter: drop-shadow(0 0 4px #facc15); }
        100% { transform: scale(1.18); filter: drop-shadow(0 0 16px #eab308); }
      }
      .laser-travel-left {
        animation: laserLeft 3s linear infinite;
      }
      @keyframes laserLeft {
        0% { transform: translateX(0); opacity: 0; }
        20% { opacity: 1; }
        75% { opacity: 1; }
        100% { transform: translateX(-400px); opacity: 0; }
      }
      .laser-travel-right {
        animation: laserRight 3s linear infinite;
      }
      @keyframes laserRight {
        0% { transform: translateX(0); opacity: 0; }
        20% { opacity: 1; }
        75% { opacity: 1; }
        100% { transform: translateX(400px); opacity: 0; }
      }
    </style>

    <linearGradient id="beamGradLeft" x1="100%" y1="0%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="1" />
      <stop offset="30%" stop-color="#facc15" stop-opacity="0.85" />
      <stop offset="70%" stop-color="#eab308" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#ca8a04" stop-opacity="0" />
    </linearGradient>

    <linearGradient id="beamGradRight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="1" />
      <stop offset="30%" stop-color="#facc15" stop-opacity="0.85" />
      <stop offset="70%" stop-color="#eab308" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#ca8a04" stop-opacity="0" />
    </linearGradient>

    <linearGradient id="batGold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#fef08a" />
      <stop offset="50%" stop-color="#facc15" />
      <stop offset="100%" stop-color="#eab308" />
    </linearGradient>

    <filter id="laserGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2.5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <!-- Left & Right Main Guide Beams (y=20) -->
  <line x1="30" y1="20" x2="435" y2="20" stroke="url(#beamGradLeft)" stroke-width="2" class="divider-pulse" />
  <line x1="525" y1="20" x2="930" y2="20" stroke="url(#beamGradRight)" stroke-width="2" class="divider-pulse" />

  <!-- Secondary subtle hairline guides -->
  <line x1="60" y1="20" x2="435" y2="20" stroke="#ffffff" stroke-width="0.8" opacity="0.6" />
  <line x1="525" y1="20" x2="900" y2="20" stroke="#ffffff" stroke-width="0.8" opacity="0.6" />

  <!-- Outward Traveling Laser Pulse Bullets -->
  <circle cx="430" cy="20" r="3.5" fill="#ffffff" filter="url(#laserGlow)" class="laser-travel-left" />
  <circle cx="530" cy="20" r="3.5" fill="#ffffff" filter="url(#laserGlow)" class="laser-travel-right" />

  <!-- Precision Tick Marks & Reticles along beams -->
  <circle cx="90" cy="20" r="2" fill="#facc15" opacity="0.7" />
  <circle cx="210" cy="20" r="2" fill="#facc15" opacity="0.7" />
  <circle cx="330" cy="20" r="2" fill="#facc15" opacity="0.7" />
  <circle cx="630" cy="20" r="2" fill="#facc15" opacity="0.7" />
  <circle cx="750" cy="20" r="2" fill="#facc15" opacity="0.7" />
  <circle cx="870" cy="20" r="2" fill="#facc15" opacity="0.7" />

  <line x1="150" y1="15" x2="150" y2="25" stroke="#facc15" stroke-width="1.2" opacity="0.6" />
  <line x1="810" y1="15" x2="810" y2="25" stroke="#facc15" stroke-width="1.2" opacity="0.6" />

  <!-- Center Framing Diamond Reticle -->
  <polygon points="480,4 522,20 480,36 438,20" stroke="#facc15" stroke-width="1.4" fill="#0b0d10" opacity="0.95" />
  <polygon points="480,8 514,20 480,32 446,20" stroke="#eab308" stroke-width="0.8" fill="none" opacity="0.5" />

  <!-- Center Animated Batman Emblem (cx=480, cy=20) -->
  <g transform="translate(480, 20)">
    <g class="bat-center-glow">
      <path d="M 0 10 C 3 8 7 6.5 11 6 C 16 5.5 22 7 28 1 C 23 -1.5 17 -1.5 10 -0.5 C 6 -4 4 -6 1.5 -10 L 0.8 -6.5 L -0.8 -6.5 L -1.5 -10 C -4 -6 -6 -4 -10 -0.5 C -17 -1.5 -23 -1.5 -28 1 C -22 7 -16 5.5 -11 6 C -7 6.5 -3 8 0 10 Z" fill="url(#batGold)" />
    </g>
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
