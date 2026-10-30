import sys
from PIL import Image, ImageDraw, ImageFont
font_path, out = sys.argv[1], sys.argv[2]
LIME = (198, 244, 50, 255)
def mark(size, bg, k_scale=0.58, dot=True, dot_col=LIME, k_col=(255,255,255,255), pad=0.0):
    im = Image.new('RGBA', (size, size), bg)
    d = ImageDraw.Draw(im)
    f = ImageFont.truetype(font_path, int(size * k_scale))
    bbox = d.textbbox((0, 0), 'K', font=f)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - w) / 2 - bbox[0] - size * 0.03
    y = (size - h) / 2 - bbox[1]
    d.text((x, y), 'K', font=f, fill=k_col)
    if dot:
        r = size * 0.075
        cx, cy = size * 0.76, size * 0.73
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=dot_col)
    return im
mark(1024, (0, 0, 0, 255)).save(f'{out}/icon.png')
# Android adaptive: content within the central 66% safe zone
fg = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
inner = mark(680, (0, 0, 0, 0))
fg.paste(inner, (172, 172), inner)
fg.save(f'{out}/android-icon-foreground.png')
Image.new('RGBA', (1024, 1024), (0, 0, 0, 255)).save(f'{out}/android-icon-background.png')
mono = Image.new('RGBA', (1024, 1024), (0, 0, 0, 0))
m = mark(680, (0, 0, 0, 0), dot_col=(255, 255, 255, 255))
mono.paste(m, (172, 172), m)
mono.save(f'{out}/android-icon-monochrome.png')
# Splash: just the K mark on transparent (bg colour comes from app.json)
sp = mark(400, (0, 0, 0, 0))
sp.save(f'{out}/splash-icon.png')
mark(48, (0, 0, 0, 255)).save(f'{out}/favicon.png')
print('ok')
