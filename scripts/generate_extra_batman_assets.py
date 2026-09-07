import os

def create_skunkworks_card():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 250" width="100%" height="250px">
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
      .proto-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 11.5px;
        font-weight: 800;
        fill: #facc15;
        letter-spacing: 0.8px;
      }
      .proto-mission {
        font-size: 10px;
        font-weight: 700;
        fill: #94a3b8;
      }
      .proto-label {
        font-size: 8.5px;
        font-weight: 800;
        fill: #64748b;
        letter-spacing: 0.8px;
      }
      .proto-val {
        font-size: 9.5px;
        font-weight: 700;
        fill: #cbd5e1;
      }
      .status-pill {
        font-family: 'Orbitron', sans-serif;
        font-size: 8.5px;
        font-weight: 800;
        letter-spacing: 0.8px;
      }

      .pulse-glow {
        animation: glowPulse 3s ease-in-out infinite alternate;
      }
      @keyframes glowPulse {
        0% { opacity: 0.85; filter: drop-shadow(0 0 3px #facc15); }
        100% { opacity: 1; filter: drop-shadow(0 0 8px #eab308); }
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

      .bar-pulse {
        animation: barGlow 2.5s ease-in-out infinite alternate;
      }
      @keyframes barGlow {
        0% { opacity: 0.85; }
        100% { opacity: 1; filter: drop-shadow(0 0 4px #22c55e); }
      }
    </style>

    <linearGradient id="skunkBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e131d" />
      <stop offset="50%" stop-color="#0b0d10" />
      <stop offset="100%" stop-color="#080a0d" />
    </linearGradient>

    <linearGradient id="sheen" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#facc15" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>

    <clipPath id="skunkClip">
      <rect x="0" y="0" width="960" height="250" rx="10" ry="10" />
    </clipPath>
  </defs>

  <g clip-path="url(#skunkClip)">
    <!-- Base Card Frame -->
    <rect x="1" y="1" width="958" height="248" rx="9.5" fill="url(#skunkBg)" stroke="rgba(250, 204, 21, 0.45)" stroke-width="1.5" />

    <!-- Corner Reticles -->
    <path d="M 8 20 L 8 8 L 20 8" stroke="#facc15" stroke-width="2" fill="none" />
    <path d="M 952 20 L 952 8 L 940 8" stroke="#facc15" stroke-width="2" fill="none" />
    <path d="M 8 230 L 8 242 L 20 242" stroke="#facc15" stroke-width="2" fill="none" />
    <path d="M 952 230 L 952 242 L 940 242" stroke="#facc15" stroke-width="2" fill="none" />

    <!-- Card Header -->
    <g transform="translate(26, 26)">
      <circle cx="0" cy="0" r="4.5" fill="#facc15" />
      <circle cx="0" cy="0" r="7.5" fill="none" stroke="#facc15" stroke-width="1" opacity="0.5" />
      <text x="14" y="4.5" class="card-title">BATCAVE SKUNKWORKS // ACTIVE PROTOTYPES</text>
    </g>

    <!-- Bat Emblem Top Right -->
    <g transform="translate(905, 24) scale(0.65)" class="pulse-glow">
      <path d="M 0 14 C 4 11 9 9 14 8 C 20 7 27 9 35 1 C 29 -2 21 -2 13 -1 C 8 -6 5 -8 2 -13 L 1 -8 L -1 -8 L -2 -13 C -5 -8 -8 -6 -13 -1 C -21 -2 -29 -2 -35 1 C -27 9 -20 7 -14 8 C -9 9 -4 11 0 14 Z" fill="#facc15" />
    </g>

    <!-- 3 Skunkworks Prototype Columns -->
    <!-- COLUMN 1: WEATHER AI -->
    <g transform="translate(24, 52)">
      <rect x="0" y="0" width="292" height="178" rx="7" fill="#101520" stroke="rgba(250, 204, 21, 0.25)" stroke-width="1" />
      <g transform="translate(14, 20)">
        <text x="0" y="0" class="proto-title">🌦️ WEATHER AI</text>
        <text x="0" y="18" class="proto-mission">Meteorological Intelligence &amp; Risk Prediction</text>

        <!-- Status Pill -->
        <rect x="0" y="32" width="138" height="20" rx="4" fill="rgba(34, 197, 94, 0.12)" stroke="rgba(34, 197, 94, 0.5)" stroke-width="1" />
        <circle cx="9" cy="42" r="3" fill="#22c55e" />
        <text x="18" y="45.5" class="status-pill" fill="#22c55e">ACTIVE ALPHA • 85%</text>

        <!-- Specs -->
        <text x="0" y="74" class="proto-label">ENGINE ARCHITECTURE</text>
        <text x="0" y="88" class="proto-val">Python • Scikit-Learn • FastAPI • Next.js</text>

        <text x="0" y="110" class="proto-label">MISSION FOCUS</text>
        <text x="0" y="124" class="proto-val">Extreme climate pattern telemetry &amp; forecasting</text>

        <!-- Progress bar -->
        <rect x="0" y="136" width="264" height="4" rx="2" fill="#1e293b" />
        <rect x="0" y="136" width="224" height="4" rx="2" fill="#22c55e" class="bar-pulse" />
      </g>
    </g>

    <!-- COLUMN 2: AEGIS SHIELD -->
    <g transform="translate(334, 52)">
      <rect x="0" y="0" width="292" height="178" rx="7" fill="#101520" stroke="rgba(250, 204, 21, 0.25)" stroke-width="1" />
      <g transform="translate(14, 20)">
        <text x="0" y="0" class="proto-title">🛡️ AEGIS SHIELD</text>
        <text x="0" y="18" class="proto-mission">Sub-Second Payment Stream Fraud Detection</text>

        <!-- Status Pill -->
        <rect x="0" y="32" width="146" height="20" rx="4" fill="rgba(234, 179, 8, 0.12)" stroke="rgba(234, 179, 8, 0.5)" stroke-width="1" />
        <circle cx="9" cy="42" r="3" fill="#eab308" />
        <text x="18" y="45.5" class="status-pill" fill="#eab308">HARDENING • 70%</text>

        <!-- Specs -->
        <text x="0" y="74" class="proto-label">ENGINE ARCHITECTURE</text>
        <text x="0" y="88" class="proto-val">TypeScript • Node.js • Kafka • PostgreSQL</text>

        <text x="0" y="110" class="proto-label">MISSION FOCUS</text>
        <text x="0" y="124" class="proto-val">Graph anomaly analysis &amp; heuristic risk scoring</text>

        <!-- Progress bar -->
        <rect x="0" y="136" width="264" height="4" rx="2" fill="#1e293b" />
        <rect x="0" y="136" width="185" height="4" rx="2" fill="#eab308" />
      </g>
    </g>

    <!-- COLUMN 3: BAT-AGENT -->
    <g transform="translate(644, 52)">
      <rect x="0" y="0" width="292" height="178" rx="7" fill="#101520" stroke="rgba(250, 204, 21, 0.25)" stroke-width="1" />
      <g transform="translate(14, 20)">
        <text x="0" y="0" class="proto-title">⚡ BAT-AGENT</text>
        <text x="0" y="18" class="proto-mission">Autonomous LLM Workflow Runner &amp; CLI</text>

        <!-- Status Pill -->
        <rect x="0" y="32" width="144" height="20" rx="4" fill="rgba(56, 189, 248, 0.12)" stroke="rgba(56, 189, 248, 0.5)" stroke-width="1" />
        <circle cx="9" cy="42" r="3" fill="#38bdf8" />
        <text x="18" y="45.5" class="status-pill" fill="#38bdf8">PILOT RUNNER • 92%</text>

        <!-- Specs -->
        <text x="0" y="74" class="proto-label">ENGINE ARCHITECTURE</text>
        <text x="0" y="88" class="proto-val">Python • LangChain • FastAPI • Redis</text>

        <text x="0" y="110" class="proto-label">MISSION FOCUS</text>
        <text x="0" y="124" class="proto-val">Multi-tool autonomous orchestration &amp; exec</text>

        <!-- Progress bar -->
        <rect x="0" y="136" width="264" height="4" rx="2" fill="#1e293b" />
        <rect x="0" y="136" width="242" height="4" rx="2" fill="#38bdf8" />
      </g>
    </g>

    <!-- Holographic Sheen -->
    <rect x="0" y="0" width="200" height="250" fill="url(#sheen)" class="holo-sweep" pointer-events="none" />
  </g>
</svg>'''
    with open("assets/batcave-skunkworks-prototypes.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Created assets/batcave-skunkworks-prototypes.svg")

def create_audio_frequency_card():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 95" width="100%" height="95px">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;800;900&amp;family=JetBrains+Mono:wght@500;700;800&amp;display=swap');

      * { box-sizing: border-box; }
      text { font-family: 'JetBrains Mono', monospace; user-select: none; }

      .audio-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 11px;
        font-weight: 800;
        fill: #facc15;
        letter-spacing: 1.2px;
      }
      .track-name {
        font-family: 'JetBrains Mono', monospace;
        font-size: 11px;
        font-weight: 800;
        fill: #f8fafc;
        letter-spacing: 0.5px;
      }
      .artist-name {
        font-size: 9.5px;
        font-weight: 700;
        fill: #94a3b8;
      }
      .freq-tag {
        font-size: 8.5px;
        font-weight: 800;
        fill: #22c55e;
        letter-spacing: 0.8px;
      }

      /* Animated Audio Equalizer Bars */
      .bar {
        transform-origin: bottom;
        animation: eqPulse 1.2s ease-in-out infinite alternate;
      }
      @keyframes eqPulse {
        0% { transform: scaleY(0.2); }
        50% { transform: scaleY(0.95); }
        100% { transform: scaleY(0.4); }
      }
      .b1 { animation-delay: 0.1s; animation-duration: 0.9s; }
      .b2 { animation-delay: 0.4s; animation-duration: 1.3s; }
      .b3 { animation-delay: 0.2s; animation-duration: 0.8s; }
      .b4 { animation-delay: 0.6s; animation-duration: 1.1s; }
      .b5 { animation-delay: 0.3s; animation-duration: 1.4s; }
      .b6 { animation-delay: 0.7s; animation-duration: 0.7s; }
      .b7 { animation-delay: 0.2s; animation-duration: 1.2s; }
      .b8 { animation-delay: 0.5s; animation-duration: 1.0s; }
      .b9 { animation-delay: 0.3s; animation-duration: 0.85s; }
      .b10 { animation-delay: 0.8s; animation-duration: 1.35s; }
      .b11 { animation-delay: 0.1s; animation-duration: 1.05s; }
      .b12 { animation-delay: 0.4s; animation-duration: 0.95s; }
      .b13 { animation-delay: 0.6s; animation-duration: 1.25s; }
      .b14 { animation-delay: 0.2s; animation-duration: 0.75s; }
      .b15 { animation-delay: 0.5s; animation-duration: 1.15s; }
      .b16 { animation-delay: 0.3s; animation-duration: 1.3s; }
    </style>

    <linearGradient id="audioBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0e131d" />
      <stop offset="100%" stop-color="#080a0d" />
    </linearGradient>

    <linearGradient id="barGrad" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#eab308" />
      <stop offset="60%" stop-color="#facc15" />
      <stop offset="100%" stop-color="#fef08a" />
    </linearGradient>

    <clipPath id="audioClip">
      <rect x="0" y="0" width="960" height="95" rx="8" ry="8" />
    </clipPath>
  </defs>

  <g clip-path="url(#audioClip)">
    <rect x="1" y="1" width="958" height="93" rx="7.5" fill="url(#audioBg)" stroke="rgba(250, 204, 21, 0.4)" stroke-width="1.2" />

    <!-- Left: Equalizer animation & Vinyl badge -->
    <g transform="translate(25, 22)">
      <!-- Pulsing Dot -->
      <circle cx="6" cy="6" r="4" fill="#22c55e" />
      <circle cx="6" cy="6" r="7" fill="none" stroke="#22c55e" stroke-width="1" opacity="0.5" />
      <text x="20" y="10" class="audio-title">BATCAVE SECURE TRANSMISSION</text>
      <text x="280" y="10" class="freq-tag">FREQ: 148.85 MHz // ENCRYPTED LINK</text>

      <!-- Track details -->
      <text x="20" y="38" class="track-name">🎵 THE BATMAN THEME // BEAUTIFUL LIE</text>
      <text x="20" y="54" class="artist-name">Hans Zimmer &amp; Junkie XL • Wayne Enterprises Applied Soundscapes</text>
    </g>

    <!-- Right: Equalizer Visualizer Bars -->
    <g transform="translate(680, 25)">
      <!-- 16 Equalizer bars, height=45, centered -->
      <!-- bar x, y, width=6, height=40 -->
      <rect x="0" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b1" transform="translate(0, -38)" />
      <rect x="12" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b2" transform="translate(0, -38)" />
      <rect x="24" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b3" transform="translate(0, -38)" />
      <rect x="36" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b4" transform="translate(0, -38)" />
      <rect x="48" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b5" transform="translate(0, -38)" />
      <rect x="60" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b6" transform="translate(0, -38)" />
      <rect x="72" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b7" transform="translate(0, -38)" />
      <rect x="84" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b8" transform="translate(0, -38)" />
      <rect x="96" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b9" transform="translate(0, -38)" />
      <rect x="108" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b10" transform="translate(0, -38)" />
      <rect x="120" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b11" transform="translate(0, -38)" />
      <rect x="132" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b12" transform="translate(0, -38)" />
      <rect x="144" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b13" transform="translate(0, -38)" />
      <rect x="156" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b14" transform="translate(0, -38)" />
      <rect x="168" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b15" transform="translate(0, -38)" />
      <rect x="180" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b16" transform="translate(0, -38)" />
      <rect x="192" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b5" transform="translate(0, -38)" />
      <rect x="204" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b2" transform="translate(0, -38)" />
      <rect x="216" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b7" transform="translate(0, -38)" />
      <rect x="228" y="44" width="7" height="38" rx="2" fill="url(#barGrad)" class="bar b1" transform="translate(0, -38)" />
    </g>

    <!-- Mini bat emblem right -->
    <g transform="translate(925, 46) scale(0.45)">
      <path d="M 0 14 C 4 11 9 9 14 8 C 20 7 27 9 35 1 C 29 -2 21 -2 13 -1 C 8 -6 5 -8 2 -13 L 1 -8 L -1 -8 L -2 -13 C -5 -8 -8 -6 -13 -1 C -21 -2 -29 -2 -35 1 C -27 9 -20 7 -14 8 C -9 9 -4 11 0 14 Z" fill="#facc15" />
    </g>
  </g>
</svg>'''
    with open("assets/batcave-audio-frequency.svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print("Created assets/batcave-audio-frequency.svg")

if __name__ == '__main__':
    create_skunkworks_card()
    create_audio_frequency_card()
