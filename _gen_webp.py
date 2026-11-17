# Generates WebP placeholder images for Batam Good Transport.
# Replaces the old SVG placeholders. Keep same filenames (.webp).
import os
from PIL import Image, ImageDraw, ImageFont

BASE = os.path.dirname(os.path.abspath(__file__))

NAVY = (16, 28, 44)
DARK = (23, 40, 61)
ACCENT = (36, 123, 206)
WHITE = (255, 255, 255)


def font(size, bold=True):
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for c in candidates:
        if os.path.exists(c):
            return ImageFont.truetype(c, size)
    return ImageFont.load_default()


def vgrad(w, h, c1, c2):
    base = Image.new("RGB", (w, h), c1)
    top = Image.new("RGB", (w, h), c2)
    mask = Image.new("L", (w, h))
    md = mask.load()
    for y in range(h):
        v = int(255 * y / h)
        for x in range(w):
            md[x, y] = v
    base.paste(top, (0, 0), mask)
    return base


def card(w, h, c1, c2, title, subtitle, out, accent=ACCENT):
    img = vgrad(w, h, c1, c2)
    d = ImageDraw.Draw(img)
    # decorative circles
    cx, cy = int(w * 0.8), int(h * 0.7)
    for r in (int(min(w, h) * 0.42), int(min(w, h) * 0.30), int(min(w, h) * 0.18)):
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(255, 255, 255, 40), width=2)
    # accent bar
    d.rectangle([int(w * 0.08), int(h * 0.40), int(w * 0.18), int(h * 0.40) + 4], fill=accent)
    # title (wrap if long)
    f_title = font(max(22, int(h * 0.09)))
    f_sub = font(max(13, int(h * 0.05)), bold=False)
    f_brand = font(max(11, int(h * 0.04)), bold=False)
    # split title into max 2 lines
    words = title.split()
    lines, cur = [], ""
    for word in words:
        test = (cur + " " + word).strip()
        if d.textlength(test, font=f_title) < w * 0.8:
            cur = test
        else:
            lines.append(cur); cur = word
    lines.append(cur)
    ty = int(h * 0.46)
    for ln in lines[:2]:
        d.text((int(w * 0.08), ty), ln, fill=WHITE, font=f_title)
        ty += int(h * 0.11)
    if subtitle:
        d.text((int(w * 0.08), int(h * 0.66)), subtitle, fill=(210, 220, 232), font=f_sub)
    d.text((int(w * 0.08), int(h * 0.90)), "BATAM GOOD TRANSPORT", fill=(160, 175, 195), font=f_brand)
    img.save(out, "WEBP", quality=88)


def write(path, img):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    img.save(full, "WEBP", quality=88)


# ---- Favicon (64x64, navy bg + accent chevron) ----
fav = Image.new("RGB", (64, 64), NAVY)
d = ImageDraw.Draw(fav)
d.line([(18, 40), (32, 20), (46, 40)], fill=ACCENT, width=5, joint="curve")
d.line([(23, 34), (41, 34)], fill=ACCENT, width=5)
write("favicon.webp", fav)

# ---- Logo (transparent bg, dark text) ----
logo = Image.new("RGBA", (200, 48), (0, 0, 0, 0))
ld = ImageDraw.Draw(logo)
ld.rounded_rectangle([2, 8, 34, 40], radius=8, fill=ACCENT)
ld.line([(10, 28), (18, 16), (26, 28)], fill=WHITE, width=3, joint="curve")
ld.line([(13, 24), (23, 24)], fill=WHITE, width=3)
ld.text((42, 6), "BATAM GOOD", fill=NAVY, font=font(17))
ld.text((42, 28), "TRANSPORT", fill=ACCENT, font=font(10))
write("images/logo.webp", logo)

# ---- Hero ----
card(1920, 1080, (11, 22, 34), (30, 58, 95), "Premium Fleet in Batam", "COMFORT  ·  RELIABILITY  ·  STYLE",
     os.path.join(BASE, "images/hero.webp"))

# ---- About ----
card(800, 1000, NAVY, ACCENT, "Professional Driver", "EXPERIENCED & COURTEOUS", os.path.join(BASE, "images/about-driver.webp"))
card(800, 600, DARK, (15, 76, 129), "Our Fleet", "WELL-MAINTAINED VEHICLES", os.path.join(BASE, "images/about-fleet.webp"))

fleet = [
    ("toyota-avanza", "Toyota Avanza", "MPV · 7 SEATS"),
    ("mitsubishi-xpander", "Mitsubishi Xpander", "MPV · 7 SEATS"),
    ("toyota-innova-reborn", "Toyota Innova Reborn", "MPV · 7 SEATS"),
    ("toyota-innova-zenix", "Toyota Innova Zenix", "PREMIUM MPV · 7 SEATS"),
    ("toyota-alphard", "Toyota Alphard", "LUXURY MPV · 7 SEATS"),
    ("toyota-fortuner", "Toyota Fortuner", "SUV · 7 SEATS"),
    ("toyota-hiace-commuter", "Toyota Hiace Commuter", "VAN · 15 SEATS"),
    ("toyota-hiace-premio", "Toyota Hiace Premio", "PREMIUM VAN · 15 SEATS"),
    ("isuzu-elf-long", "Isuzu Elf Long", "MINIBUS · 19 SEATS"),
    ("toyota-coaster", "Toyota Coaster", "MINIBUS · 29 SEATS"),
    ("medium-bus", "Medium Bus", "BUS · 35 SEATS"),
    ("big-bus", "Big Bus", "BUS · 59 SEATS"),
]
for slug, name, cat in fleet:
    card(800, 500, NAVY, (31, 58, 95), name, cat, os.path.join(BASE, f"images/fleet/{slug}.webp"))

services = [
    ("private-driver", "Private Driver", "PRIVATE TRANSPORTATION"),
    ("airport-transfer", "Airport & Ferry Transfer", "PICK-UP & DROP-OFF"),
    ("full-day", "Full Day Charter", "FLEXIBLE ITINERARY"),
    ("half-day", "Half Day Charter", "SHORT CITY VISITS"),
    ("corporate", "Corporate Transport", "BUSINESS & GUESTS"),
    ("group", "Group Transport", "FAMILIES & TOUR GROUPS"),
]
for slug, name, cat in services:
    card(800, 600, DARK, ACCENT, name, cat, os.path.join(BASE, f"images/services/{slug}.webp"))

tours = [
    ("batam-city-tour", "Batam City Tour", "FULL DAY · 8 HOURS"),
    ("shopping-tour", "Shopping Tour", "FULL DAY · MALLS & OUTLETS"),
    ("family-day-trip", "Family Day Trip", "FULL DAY · PARKS & BEACHES"),
    ("culinary-tour", "Culinary Tour", "HALF / FULL DAY · LOCAL FLAVOURS"),
    ("custom-private-tour", "Custom Private Tour", "FULLY CUSTOMIZABLE"),
]
for slug, name, cat in tours:
    card(800, 560, (15, 42, 68), (46, 134, 222), name, cat, os.path.join(BASE, f"images/tours/{slug}.webp"))

dests = [
    ("barelang-bridge", "Barelang Bridge", "ICONIC LANDMARK"),
    ("welcome-monument", "Welcome to Batam", "CITY MONUMENT"),
    ("maha-vihara", "Maha Vihara Duta Maitreya", "BUDDHIST TEMPLE"),
    ("nagoya-hill", "Nagoya Hill", "SHOPPING DISTRICT"),
    ("grand-batam-mall", "Grand Batam Mall", "SHOPPING MALL"),
    ("ocarina-park", "Ocarina Park", "FAMILY PARK"),
    ("turi-beach", "Turi Beach", "COASTAL RESORT"),
]
for slug, name, cat in dests:
    card(800, 600, NAVY, (27, 79, 114), name, cat, os.path.join(BASE, f"images/destinations/{slug}.webp"))

print("WebP placeholders generated.")
