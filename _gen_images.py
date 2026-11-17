# Generates premium SVG placeholder images for Batam Good Transport.
# Run once; replace any .svg with real photos later (keep same filename).
import os

BASE = os.path.dirname(os.path.abspath(__file__))

# palette
NAVY = "#101C2C"
DARK = "#17283D"
ACCENT = "#247BCE"
SILVER = "#C6CDD5"
LIGHT = "#F5F7FA"

def svg_card(w, h, c1, c2, title, subtitle="", out="", accent=ACCENT, pattern="dots"):
    cx, cy = w * 0.82, h * 0.18
    gid = "g" + str(abs(hash(out)) % 100000)
    pat = ""
    if pattern == "dots":
        pat = f'''<circle cx="{w*0.78}" cy="{h*0.72}" r="{min(w,h)*0.42}" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="1.5"/>
  <circle cx="{w*0.78}" cy="{h*0.72}" r="{min(w,h)*0.30}" fill="none" stroke="rgba(255,255,255,0.06)" stroke-width="1.5"/>
  <circle cx="{w*0.78}" cy="{h*0.72}" r="{min(w,h)*0.18}" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="1.5"/>'''
    elif pattern == "lines":
        lines = ""
        for i in range(-6, 14):
            y = i * (h / 8)
            lines += f'<line x1="0" y1="{y}" x2="{w}" y2="{y+h*0.35}" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>'
        pat = lines
    sub = f'''<text x="{w*0.08}" y="{h*0.62}" font-family="Arial, sans-serif" font-size="{max(14, int(h*0.055))}" fill="rgba(255,255,255,0.75)" letter-spacing="3">{subtitle}</text>''' if subtitle else ""
    content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{c1}"/>
      <stop offset="100%" stop-color="{c2}"/>
    </linearGradient>
  </defs>
  <rect width="{w}" height="{h}" fill="url(#{gid})"/>
  {pat}
  <rect x="{w*0.08}" y="{h*0.40}" width="{w*0.10}" height="4" rx="2" fill="{accent}"/>
  <text x="{w*0.08}" y="{h*0.52}" font-family="Arial, sans-serif" font-size="{max(20, int(h*0.09))}" font-weight="700" fill="#ffffff">{title}</text>
  {sub}
  <text x="{w*0.08}" y="{h*0.90}" font-family="Arial, sans-serif" font-size="{max(11, int(h*0.04))}" fill="rgba(255,255,255,0.45)" letter-spacing="2">BATAM GOOD TRANSPORT</text>
</svg>'''
    with open(out, "w", encoding="utf-8") as f:
        f.write(content)

def write(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

# ---- Logo (SVG) ----
logo = '''<svg xmlns="http://www.w3.org/2000/svg" width="200" height="48" viewBox="0 0 200 48">
  <rect x="2" y="8" width="32" height="32" rx="8" fill="#247BCE"/>
  <path d="M10 28 L18 16 L26 28 M13 24 L23 24" stroke="#fff" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="42" y="27" font-family="Arial, sans-serif" font-size="17" font-weight="800" fill="#101C2C" letter-spacing="0.5">BATAM GOOD</text>
  <text x="42" y="42" font-family="Arial, sans-serif" font-size="10" font-weight="600" fill="#247BCE" letter-spacing="3">TRANSPORT</text>
</svg>'''
write("images/logo.svg", logo)

# ---- Favicon ----
favicon = '''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="14" fill="#101C2C"/>
  <path d="M18 38 L32 18 L46 38 M23 32 L41 32" stroke="#247BCE" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
</svg>'''
write("favicon.svg", favicon)

# ---- Hero (wide) ----
svg_card(1920, 1080, "#0B1622", "#1E3A5F", "Premium Fleet in Batam", "COMFORT · RELIABILITY · STYLE", os.path.join(BASE, "images/hero.svg"), pattern="lines")

# ---- About images ----
svg_card(800, 1000, "#101C2C", "#247BCE", "Professional Driver", "EXPERIENCED & COURTEOUS", os.path.join(BASE, "images/about-driver.svg"), pattern="dots")
svg_card(800, 600, "#17283D", "#0F4C81", "Our Fleet", "WELL-MAINTAINED VEHICLES", os.path.join(BASE, "images/about-fleet.svg"), pattern="lines")

# ---- Fleet (16:9 cards) ----
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
    svg_card(800, 500, "#101C2C", "#1F3A5F", name, cat, os.path.join(BASE, f"images/fleet/{slug}.svg"), pattern="dots")

# ---- Services (4:3) ----
services = [
    ("private-driver", "Private Driver", "PRIVATE TRANSPORTATION"),
    ("airport-transfer", "Airport & Ferry Transfer", "PICK-UP & DROP-OFF"),
    ("full-day", "Full Day Charter", "FLEXIBLE ITINERARY"),
    ("half-day", "Half Day Charter", "SHORT CITY VISITS"),
    ("corporate", "Corporate Transport", "BUSINESS & GUESTS"),
    ("group", "Group Transport", "FAMILIES & TOUR GROUPS"),
]
for slug, name, cat in services:
    svg_card(800, 600, "#17283D", "#247BCE", name, cat, os.path.join(BASE, f"images/services/{slug}.svg"), pattern="lines")

# ---- Tours ----
tours = [
    ("batam-city-tour", "Batam City Tour", "FULL DAY · 8 HOURS"),
    ("shopping-tour", "Shopping Tour", "FULL DAY · MALLS & FACTORY OUTLETS"),
    ("family-day-trip", "Family Day Trip", "FULL DAY · PARKS & BEACHES"),
    ("culinary-tour", "Culinary Tour", "HALF / FULL DAY · LOCAL FLAVOURS"),
    ("custom-private-tour", "Custom Private Tour", "FULLY CUSTOMIZABLE"),
]
for slug, name, cat in tours:
    svg_card(800, 560, "#0F2A44", "#2E86DE", name, cat, os.path.join(BASE, f"images/tours/{slug}.svg"), pattern="dots")

# ---- Destinations ----
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
    svg_card(800, 600, "#101C2C", "#1B4F72", name, cat, os.path.join(BASE, f"images/destinations/{slug}.svg"), pattern="lines")

print("Generated all placeholder SVGs.")
print("Fleet:", len(fleet), "Services:", len(services), "Tours:", len(tours), "Destinations:", len(dests))
