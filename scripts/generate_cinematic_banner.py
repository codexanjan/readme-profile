import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_cinematic_hero_gif():
    base_img_path = 'assets/batman_hero_base.jpg'
    if not os.path.exists(base_img_path):
        print("Base image not found:", base_img_path)
        return
        
    base_img = Image.open(base_img_path).convert('RGBA')
    
    # Target banner dimensions
    W, H = 960, 340
    
    # Resize keeping aspect ratio, then crop
    scale = W / base_img.width
    new_h = int(base_img.height * scale)
    base_resized = base_img.resize((W, new_h), Image.Resampling.LANCZOS)
    
    # Crop from y=20 to y=360
    base_crop = base_resized.crop((0, 20, W, 20 + H))
    
    # Load custom fonts
    orbitron_title = ImageFont.truetype('Orbitron.ttf', 38)
    orbitron_sub = ImageFont.truetype('Orbitron.ttf', 13)
    orbitron_tag = ImageFont.truetype('Orbitron.ttf', 10)
    jb_mono_sm = ImageFont.truetype('JetBrainsMono.ttf', 11)
    jb_mono_xs = ImageFont.truetype('JetBrainsMono.ttf', 9)
    jb_mono_motto = ImageFont.truetype('JetBrainsMono.ttf', 11)
    
    num_frames = 20
    frames = []
    
    # Pre-render dark vignette overlay on left side so text pops cleanly
    vignette = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    v_draw = ImageDraw.Draw(vignette)
    for x in range(W):
        # Heavy darkness on left 0-580 for text contrast, fading towards right where Batman stands
        if x < 400:
            alpha = int(170)
        elif x < 650:
            factor = (650 - x) / 250.0
            alpha = int(170 * factor)
        else:
            alpha = 0
        v_draw.line([(x, 0), (x, H)], fill=(11, 13, 16, alpha))
        
    # Pre-render rain drops positions
    np.random.seed(42)
    num_rain = 50
    rain_x = np.random.randint(0, W, size=num_rain)
    rain_y = np.random.randint(0, H, size=num_rain)
    rain_speed = np.random.randint(18, 30, size=num_rain)
    rain_len = np.random.randint(10, 22, size=num_rain)

    # Bat-signal center in cropped image: around (x=260, y=95)
    bs_cx, bs_cy = 260, 95
    
    for f in range(num_frames):
        # Start with base image
        frame = base_crop.copy()
        
        # 1. Bat-Signal Pulsing Volumetric Light
        pulse = 0.5 + 0.5 * math.sin(f / num_frames * 2 * math.pi)
        glow_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        g_draw = ImageDraw.Draw(glow_layer)
        glow_radius = int(85 + 20 * pulse)
        glow_alpha = int(35 + 30 * pulse)
        g_draw.ellipse(
            [(bs_cx - glow_radius, bs_cy - glow_radius), (bs_cx + glow_radius, bs_cy + glow_radius)],
            fill=(250, 204, 21, glow_alpha)
        )
        # Inner brighter core
        core_r = int(55 + 10 * pulse)
        core_a = int(60 + 40 * pulse)
        g_draw.ellipse(
            [(bs_cx - core_r, bs_cy - core_r), (bs_cx + core_r, bs_cy + core_r)],
            fill=(254, 240, 138, core_a)
        )
        glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(14))
        frame = Image.alpha_composite(frame, glow_layer)
        
        # 2. Composite text-contrast vignette
        frame = Image.alpha_composite(frame, vignette)
        
        # 3. Rain streaks (moving diagonally down-left)
        rain_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        r_draw = ImageDraw.Draw(rain_layer)
        for i in range(num_rain):
            curr_y = (rain_y[i] + f * rain_speed[i]) % H
            curr_x = (rain_x[i] - f * (rain_speed[i] // 3)) % W
            r_draw.line(
                [(curr_x, curr_y), (curr_x - 3, curr_y + rain_len[i])],
                fill=(220, 230, 245, 75),
                width=1
            )
        frame = Image.alpha_composite(frame, rain_layer)
        
        # 4. HUD Overlay & Tech Graphics
        hud_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        h_draw = ImageDraw.Draw(hud_layer)
        
        # Border corners
        corner_gold = (250, 204, 21, 200)
        c_len = 16
        # Top-Left
        h_draw.line([(10, 10), (10 + c_len, 10)], fill=corner_gold, width=2)
        h_draw.line([(10, 10), (10, 10 + c_len)], fill=corner_gold, width=2)
        # Top-Right
        h_draw.line([(W - 10, 10), (W - 10 - c_len, 10)], fill=corner_gold, width=2)
        h_draw.line([(W - 10, 10), (W - 10, 10 + c_len)], fill=corner_gold, width=2)
        # Bottom-Left
        h_draw.line([(10, H - 10), (10 + c_len, H - 10)], fill=corner_gold, width=2)
        h_draw.line([(10, H - 10), (10, H - 10 - c_len)], fill=corner_gold, width=2)
        # Bottom-Right
        h_draw.line([(W - 10, H - 10), (W - 10 - c_len, H - 10)], fill=corner_gold, width=2)
        h_draw.line([(W - 10, H - 10), (W - 10, H - 10 - c_len)], fill=corner_gold, width=2)
        
        # Top status bar
        # Blinking status indicator
        is_blink_on = (f % 6 < 4)
        dot_color = (34, 197, 94, 255) if is_blink_on else (34, 197, 94, 90)
        h_draw.ellipse([(28, 22), (36, 30)], fill=dot_color)
        h_draw.ellipse([(26, 20), (38, 32)], outline=(34, 197, 94, 120), width=1)
        h_draw.text((44, 20), "WAYNE ENTERPRISES // SEC-OPS MAINFRAME v4.2", font=orbitron_tag, fill=(203, 213, 225, 230))
        h_draw.text((430, 20), "[ GOTHAM SECTOR 04 // DEFCON 1 ]", font=jb_mono_xs, fill=(234, 179, 8, 200))
        
        # Coordinates HUD right top
        h_draw.text((W - 275, 20), "LAT 40.7128° N • LON 74.0060° W", font=jb_mono_xs, fill=(148, 163, 184, 200))
        
        # Main Hero Title: ANJAN SHETTY
        # Text drop shadow
        h_draw.text((32, 62), "ANJAN SHETTY", font=orbitron_title, fill=(0, 0, 0, 240))
        h_draw.text((31, 61), "ANJAN SHETTY", font=orbitron_title, fill=(113, 63, 18, 240))
        # Main gold text
        h_draw.text((30, 60), "ANJAN SHETTY", font=orbitron_title, fill=(250, 204, 21, 255))
        
        # Subtitle
        h_draw.text((32, 116), "FULL-STACK ARCHITECT // APPLIED AI & SCALABLE SYSTEMS", font=orbitron_sub, fill=(241, 245, 249, 240))
        
        # Operative Motto
        h_draw.text((32, 142), "\"The night is darkest before the code compiles. Building in the dark, shipping into the light.\"", font=jb_mono_motto, fill=(234, 179, 8, 230))
        
        # 4 Tactical Telemetry Badges (x=30, y=175)
        badges = [
            ("SECURITY CLEARANCE", "LEVEL 10 // OMEGA", (250, 204, 21)),
            ("CODENAME", "CODEXANJAN", (234, 179, 8)),
            ("HEADQUARTERS", "BATCAVE // GOTHAM", (148, 163, 184)),
            ("MAINFRAME STATUS", "ONLINE // ACTIVE", (34, 197, 94)),
        ]
        
        bx = 30
        by = 175
        for title, val, col in badges:
            bw, bh = 135, 48
            # Dark glass box
            h_draw.rectangle([(bx, by), (bx + bw, by + bh)], fill=(11, 13, 16, 190), outline=(250, 204, 21, 60), width=1)
            # Corner accents
            h_draw.line([(bx, by), (bx + 6, by)], fill=(250, 204, 21, 180), width=1)
            h_draw.line([(bx, by), (bx, by + 6)], fill=(250, 204, 21, 180), width=1)
            
            h_draw.text((bx + 8, by + 7), title, font=jb_mono_xs, fill=(100, 116, 139, 255))
            h_draw.text((bx + 8, by + 24), val, font=jb_mono_sm, fill=col)
            bx += bw + 12
            
        # Holographic Laser Sweep
        sweep_x = int(-200 + (f / num_frames) * (W + 400))
        sweep_w = 90
        s_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        s_draw = ImageDraw.Draw(s_layer)
        s_draw.polygon(
            [(sweep_x, 0), (sweep_x + sweep_w, 0), (sweep_x + sweep_w - 70, H), (sweep_x - 70, H)],
            fill=(250, 204, 21, 35)
        )
        s_layer = s_layer.filter(ImageFilter.GaussianBlur(6))
        
        # Rotating Radar Widget (x=W-75, y=65)
        radar_cx, radar_cy = W - 75, 65
        radar_r = 24
        h_draw.ellipse([(radar_cx - radar_r, radar_cy - radar_r), (radar_cx + radar_r, radar_cy + radar_r)], outline=(250, 204, 21, 90), width=1)
        h_draw.ellipse([(radar_cx - radar_r//2, radar_cy - radar_r//2), (radar_cx + radar_r//2, radar_cy + radar_r//2)], outline=(250, 204, 21, 40), width=1)
        
        # Radar needle rotating
        radar_angle = (f / num_frames) * 2 * math.pi
        needle_x = radar_cx + int((radar_r - 2) * math.cos(radar_angle))
        needle_y = radar_cy + int((radar_r - 2) * math.sin(radar_angle))
        h_draw.line([(radar_cx, radar_cy), (needle_x, needle_y)], fill=(250, 204, 21, 220), width=1)
        # Radar ping dot
        h_draw.ellipse([(radar_cx + 8, radar_cy - 8), (radar_cx + 12, radar_cy - 4)], fill=(34, 197, 94, 220))
        
        # Bottom Telemetry Bar
        h_draw.rectangle([(25, H - 42), (W - 25, H - 18)], fill=(11, 13, 16, 210), outline=(234, 179, 8, 70), width=1)
        h_draw.text((36, H - 34), "⚡ BATCAVE INTELLIGENCE: 16+ VERIFIED DSA DIRECTIVES • 4 PRODUCTION SYSTEMS • REAL-TIME HUD TELEMETRY", font=jb_mono_xs, fill=(250, 204, 21, 230))
        h_draw.text((W - 190, H - 34), "ENCRYPTION: AES-256 // ACTIVE", font=jb_mono_xs, fill=(148, 163, 184, 200))
        
        # Merge HUD and sweep
        frame = Image.alpha_composite(frame, hud_layer)
        frame = Image.alpha_composite(frame, s_layer)
        
        # Convert to RGB with high-fidelity adaptive quantization
        rgb_frame = frame.convert('RGB')
        p_frame = rgb_frame.quantize(colors=128, method=Image.Quantize.MEDIANCUT)
        frames.append(p_frame)
        
    print(f"Generated {len(frames)} frames. Quantizing and saving GIF...")
    
    # Save as animated GIF with adaptive 128-color palette for speed & crisp quality
    first_frame = frames[0]
    out_path = 'assets/batcave-cinematic-hero.gif'
    first_frame.save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=100, # 100ms per frame = 10 fps
        loop=0,
        optimize=True
    )
    size_mb = os.path.getsize(out_path) / (1024 * 1024)
    print(f"Saved {out_path}! Size: {size_mb:.2f} MB")

if __name__ == '__main__':
    create_cinematic_hero_gif()
