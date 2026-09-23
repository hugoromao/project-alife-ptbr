"""Generate poster.png (mod list), icon.png and preview.png (Workshop) for the PT-BR mod."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'art'
FONT_CANDIDATES = [
    '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSansCondensed-Bold.ttf',
    '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',
]
GREEN, YELLOW, BLUE, INK, PAPER = (0, 146, 63), (254, 221, 0), (0, 39, 118), (18, 20, 18), (236, 236, 228)


def font(size):
    for f in FONT_CANDIDATES:
        if Path(f).exists():
            return ImageFont.truetype(f, size)
    return ImageFont.load_default(size)


def centered(draw, y, text, size, fill):
    f = font(size)
    w = draw.textbbox((0, 0), text, font=f)[2]
    draw.text(((draw.im.size[0] - w) / 2, y), text, font=f, fill=fill)


def card(size):
    s = size / 512
    img = Image.new('RGB', (size, size), INK)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, size, int(22 * s)], fill=GREEN)
    d.rectangle([0, size - int(22 * s), size, size], fill=GREEN)
    cx, cy = size / 2, size * 0.56
    d.polygon([(cx - 150 * s, cy), (cx, cy - 92 * s), (cx + 150 * s, cy), (cx, cy + 92 * s)], fill=YELLOW)
    d.ellipse([cx - 58 * s, cy - 58 * s, cx + 58 * s, cy + 58 * s], fill=BLUE)
    centered(d, 50 * s, 'PROJECT', int(40 * s), PAPER)
    centered(d, 92 * s, 'A-LIFE', int(96 * s), PAPER)
    centered(d, cy - 20 * s, 'PT-BR', int(34 * s), PAPER)
    centered(d, size - 92 * s, 'TRADUÇÃO', int(46 * s), PAPER)
    return img


def main():
    OUT.mkdir(exist_ok=True)
    card(512).save(OUT / 'poster.png')
    card(256).save(OUT / 'preview.png')
    icon = Image.new('RGB', (64, 64), GREEN)
    d = ImageDraw.Draw(icon)
    d.polygon([(4, 32), (32, 12), (60, 32), (32, 52)], fill=YELLOW)
    d.ellipse([20, 20, 44, 44], fill=BLUE)
    icon.resize((32, 32), Image.LANCZOS).save(OUT / 'icon.png')
    print('art written to', OUT)


if __name__ == '__main__':
    main()
