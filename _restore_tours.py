# -*- coding: utf-8 -*-
import io

p = r"C:\Nutta\batam-good-transport\index.html"
with io.open(p, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Uniform gallery: remove wide/tall classes
html = html.replace(' class="gallery-item wide"', ' class="gallery-item"')
html = html.replace(' class="gallery-item tall"', ' class="gallery-item"')

# 2. Restore Tour nav link (desktop + mobile) between Services and Gallery
html = html.replace(
    '        <li><a href="#services" class="nav-link">Services</a></li>\n        <li><a href="#gallery" class="nav-link">Gallery</a></li>',
    '        <li><a href="#services" class="nav-link">Services</a></li>\n        <li><a href="#tours" class="nav-link">Tour</a></li>\n        <li><a href="#gallery" class="nav-link">Gallery</a></li>')
html = html.replace(
    '      <li><a href="#services" class="mobile-link">Services</a></li>\n      <li><a href="#gallery" class="mobile-link">Gallery</a></li>',
    '      <li><a href="#services" class="mobile-link">Services</a></li>\n      <li><a href="#tours" class="mobile-link">Tour</a></li>\n      <li><a href="#gallery" class="mobile-link">Gallery</a></li>')

# 3. Restore Tour in footer Quick Links
html = html.replace(
    '        <li><a href="#services">Services</a></li>\n        <li><a href="#gallery">Gallery</a></li>',
    '        <li><a href="#services">Services</a></li>\n        <li><a href="#tours">Tour</a></li>\n        <li><a href="#gallery">Gallery</a></li>')

# 4. Restore Tour option in contact form subject (before Group / Bus Rental)
html = html.replace(
    '              <option>Group / Bus Rental</option>',
    '              <option>Tour</option>\n              <option>Group / Bus Rental</option>')

# 5. Restore meta "tour packages" wording
html = html.replace(
    'full-day & half-day charter and group bus rental. Book via WhatsApp.',
    'full-day & half-day charter, tour packages and group bus rental. Book via WhatsApp.')
html = html.replace(
    'reliable private transport in Batam. Book easily via WhatsApp.',
    'reliable private transport and tour packages in Batam. Book easily via WhatsApp.')
html = html.replace(
    'airport & ferry transfer, charter services in Batam with professional drivers.',
    'airport & ferry transfer, charter and tour services in Batam with professional drivers.')
html = html.replace(
    'airport &amp; ferry transfers and charters in Batam — with professional drivers',
    'airport &amp; ferry transfers, charters and tour packages in Batam — with professional drivers')

# 6. Restore tours section before GALLERY section
tours = '''<!-- ===================== TOUR PACKAGES ===================== -->
<section class="section tours-section" id="tours">
  <div class="container">
    <div class="section-head reveal">
      <span class="section-eyebrow">Tour</span>
      <h2 class="section-title">Explore Batam Your Way</h2>
      <p class="section-sub">Curated private tour itineraries with a driver. Prices are placeholders — contact us for a tailored quote. Need something different? Request a custom itinerary.</p>
    </div>

    <div class="tours-grid">
      <article class="tour-card reveal">
        <div class="tour-img"><img src="images/tours/batam-city-tour.webp" alt="Batam City Tour package" loading="lazy" /></div>
        <div class="tour-body">
          <span class="tour-duration"><i class="fa-solid fa-clock"></i> Suggested: Full Day (8 hrs)</span>
          <h3>Batam City Tour</h3>
          <p>Discover the best of Batam: Barelang Bridge, Welcome Monument, temples, viewpoints and local cuisine.</p>
          <ul class="tour-spots"><li>Barelang Bridge</li><li>Welcome Monument</li><li>Maha Vihara Duta Maitreya</li></ul>
          <div class="tour-foot">
            <span class="tour-price">From <strong>Contact for Price</strong></span>
            <a href="#" class="btn btn-primary btn-sm js-wa-book" data-vehicle="Tour Vehicle" data-package="Batam City Tour">Book via WhatsApp</a>
          </div>
        </div>
      </article>

      <article class="tour-card reveal">
        <div class="tour-img"><img src="images/tours/shopping-tour.webp" alt="Batam Shopping Tour package" loading="lazy" /></div>
        <div class="tour-body">
          <span class="tour-duration"><i class="fa-solid fa-clock"></i> Suggested: Full Day</span>
          <h3>Shopping Tour</h3>
          <p>Malls, factory outlets and local markets — a full day of shopping with a private driver waiting for you.</p>
          <ul class="tour-spots"><li>Nagoya Hill</li><li>Grand Batam Mall</li><li>BCS Mall &amp; outlets</li></ul>
          <div class="tour-foot">
            <span class="tour-price">From <strong>Contact for Price</strong></span>
            <a href="#" class="btn btn-primary btn-sm js-wa-book" data-vehicle="Tour Vehicle" data-package="Shopping Tour">Book via WhatsApp</a>
          </div>
        </div>
      </article>

      <article class="tour-card reveal">
        <div class="tour-img"><img src="images/tours/family-day-trip.webp" alt="Batam Family Day Trip package" loading="lazy" /></div>
        <div class="tour-body">
          <span class="tour-duration"><i class="fa-solid fa-clock"></i> Suggested: Full Day</span>
          <h3>Family Day Trip</h3>
          <p>Parks, beaches and fun attractions — a relaxed itinerary designed for families and kids.</p>
          <ul class="tour-spots"><li>Ocarina Park</li><li>Turi Beach</li><li>Abang Island viewpoint</li></ul>
          <div class="tour-foot">
            <span class="tour-price">From <strong>Contact for Price</strong></span>
            <a href="#" class="btn btn-primary btn-sm js-wa-book" data-vehicle="Tour Vehicle" data-package="Family Day Trip">Book via WhatsApp</a>
          </div>
        </div>
      </article>

      <article class="tour-card reveal">
        <div class="tour-img"><img src="images/tours/culinary-tour.webp" alt="Batam Culinary Tour package" loading="lazy" /></div>
        <div class="tour-body">
          <span class="tour-duration"><i class="fa-solid fa-clock"></i> Suggested: Half / Full Day</span>
          <h3>Culinary Tour</h3>
          <p>Taste the best local seafood, kopitiam breakfasts and famous Batam cakes at authentic spots.</p>
          <ul class="tour-spots"><li>Seafood restaurants</li><li>Local kopitiam</li><li>Cake shops &amp; markets</li></ul>
          <div class="tour-foot">
            <span class="tour-price">From <strong>Contact for Price</strong></span>
            <a href="#" class="btn btn-primary btn-sm js-wa-book" data-vehicle="Tour Vehicle" data-package="Culinary Tour">Book via WhatsApp</a>
          </div>
        </div>
      </article>

      <article class="tour-card reveal tour-custom">
        <div class="tour-img"><img src="images/tours/custom-private-tour.webp" alt="Custom private tour Batam" loading="lazy" /></div>
        <div class="tour-body">
          <span class="tour-duration"><i class="fa-solid fa-wand-magic-sparkles"></i> Fully Customizable</span>
          <h3>Custom Private Tour</h3>
          <p>Tell us your interests and we'll design a private itinerary just for you — pace, stops and duration, your choice.</p>
          <ul class="tour-spots"><li>Your preferred destinations</li><li>Flexible duration</li><li>Private driver &amp; vehicle</li></ul>
          <div class="tour-foot">
            <span class="tour-price">Quote on request</span>
            <a href="#" class="btn btn-primary btn-sm js-wa-book" data-vehicle="Tour Vehicle" data-package="Custom Private Tour">Request Itinerary</a>
          </div>
        </div>
      </article>
    </div>
  </div>
</section>

'''

anchor = '<!-- ===================== GALLERY (Customer Photos) ===================== -->'
assert anchor in html
html = html.replace(anchor, tours + anchor)

with io.open(p, "w", encoding="utf-8") as f:
    f.write(html)
print("index.html restored. Length:", len(html))
print("tours section present:", 'id="tours"' in html)
print("tour nav links:", html.count('href="#tours"'))
print("gallery-item wide/tall remaining:", 'gallery-item wide' in html, 'gallery-item tall' in html)
