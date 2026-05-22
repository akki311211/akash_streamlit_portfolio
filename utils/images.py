"""
Image utilities.
- ensure_placeholders(): generates placeholder PNGs for any missing images.
  Runs once at startup. Replace these with real photos in assets/images/
  using the same filename — no code change needed.
"""

import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMG_DIR = ROOT / "assets" / "images"

# (filename, label, hex color)
PLACEHOLDERS = [
    ("profile.jpg",          "RJ",                       "#1F3A5F"),
    ("target.jpg",           "Target",                   "#CC0000"),
    ("symphony_cps.jpg",     "Symphony / CPS",           "#14B8A6"),
    ("indian_railways.jpg",  "Indian Railways",          "#5C2018"),
    ("state_street.jpg",     "State Street",             "#2E2E5C"),
    ("mastercard.jpg",       "Mastercard",               "#EB001B"),
    ("iisc.jpg",             "IISc",                     "#1F3A5F"),
    ("dtu.jpg",              "DTU",                      "#B22222"),
    ("cambridge.jpg",        "Cambridge",                "#A3C1AD"),
    ("dps.jpg",              "DPS",                      "#4A148C"),
    ("scaler.jpg",           "Scaler Academy",           "#4F46E5"),
    ("nexaml.jpg",           "NexaML",                   "#0F4C5C"),
    ("reva.jpg",             "REVA University",          "#C8102E"),
    ("teaching_misc.jpg",    "Workshops & Talks",        "#374151"),
]


def _font(size: int) -> ImageFont.ImageFont:
    """Try to load a nice font; fall back to PIL default."""
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVu-Sans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",  # macOS
        "C:/Windows/Fonts/arialbd.ttf",         # Windows
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size=size)
            except Exception:
                continue
    return ImageFont.load_default()


def _make_placeholder(path: Path, label: str, color_hex: str, size=(800, 500)):
    """Create one placeholder image with the org/school label."""
    img = Image.new("RGB", size, color_hex)
    draw = ImageDraw.Draw(img)

    # subtle darker band across the bottom for visual interest
    band_h = size[1] // 6
    draw.rectangle([0, size[1] - band_h, size[0], size[1]], fill=(0, 0, 0, 60))

    # main label, centered
    font = _font(64)
    bbox = draw.textbbox((0, 0), label, font=font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size[0] - w) / 2
    y = (size[1] - h) / 2 - 20
    draw.text((x, y), label, fill="#FFFFFF", font=font)

    # small caption below
    cap_font = _font(20)
    caption = "(replace with real photo)"
    cbbox = draw.textbbox((0, 0), caption, font=cap_font)
    cw = cbbox[2] - cbbox[0]
    draw.text(((size[0] - cw) / 2, size[1] - band_h + 12),
              caption, fill="#FFFFFFCC", font=cap_font)

    img.save(path, "JPEG", quality=88)


def ensure_placeholders() -> None:
    """Create any missing placeholder images. Idempotent — safe to call on every run."""
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    for filename, label, color in PLACEHOLDERS:
        path = IMG_DIR / filename
        if not path.exists():
            _make_placeholder(path, label, color)


def image_path(rel_path: str) -> str:
    """
    Resolve an image path relative to the project root.
    Returns the absolute path as a string. If the file is missing,
    returns the path to a generic fallback (RJ profile placeholder).
    """
    p = ROOT / rel_path
    if p.exists():
        return str(p)
    fallback = IMG_DIR / "profile.jpg"
    return str(fallback)
