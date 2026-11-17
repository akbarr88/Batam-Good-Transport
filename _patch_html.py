# -*- coding: utf-8 -*-
import io, re

p = r"C:\Nutta\batam-good-transport\index.html"
with io.open(p, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove Tour option in contact form
html = html.replace("              <option>Tour</option>\n", "")

# 2. Remove Tour from footer Quick Links
html = html.replace('        <li><a href="#tours">Tour</a></li>\n', "")

# 3. Replace TOUR PACKAGES section + DESTINATIONS section with GALLERY section.
#    Match from the TOUR PACKAGES comment up to (but not including) the ABOUT comment.
start_marker = "<!-- ===================== TOUR PACKAGES ===================== -->"
end_marker = "<!-- ===================== ABOUT ===================== -->"
i = html.find(start_marker)
j = html.find(end_marker)
assert i != -1 and j != -1 and j > i, "markers not found"

gallery = '''<!-- ===================== GALLERY (Customer Photos) ===================== -->
<section class="section gallery-section" id="gallery">
  <div class="container">
    <div class="section-head reveal">
      <span class="section-eyebrow">Gallery</span>
      <h2 class="section-title">Moments With Our Customers</h2>
      <p class="section-sub">A glimpse of our riders exploring Batam with Batam Good Transport — tap any photo to enlarge.</p>
    </div>
    <div class="gallery-grid reveal" id="galleryGrid">
      <figure class="gallery-item wide"><img src="images/gallery/gallery-01.webp" alt="Batam Good Transport customer photo 1" loading="lazy" /></figure>
      <figure class="gallery-item"><img src="images/gallery/gallery-02.webp" alt="Batam Good Transport customer photo 2" loading="lazy" /></figure>
      <figure class="gallery-item tall"><img src="images/gallery/gallery-03.webp" alt="Batam Good Transport customer photo 3" loading="lazy" /></figure>
      <figure class="gallery-item"><img src="images/gallery/gallery-04.webp" alt="Batam Good Transport customer photo 4" loading="lazy" /></figure>
      <figure class="gallery-item"><img src="images/gallery/gallery-05.webp" alt="Batam Good Transport customer photo 5" loading="lazy" /></figure>
      <figure class="gallery-item wide"><img src="images/gallery/gallery-06.webp" alt="Batam Good Transport customer photo 6" loading="lazy" /></figure>
      <figure class="gallery-item"><img src="images/gallery/gallery-07.webp" alt="Batam Good Transport customer photo 7" loading="lazy" /></figure>
      <figure class="gallery-item"><img src="images/gallery/gallery-08.webp" alt="Batam Good Transport customer photo 8" loading="lazy" /></figure>
      <figure class="gallery-item tall"><img src="images/gallery/gallery-09.webp" alt="Batam Good Transport customer photo 9" loading="lazy" /></figure>
      <figure class="gallery-item"><img src="images/gallery/gallery-10.webp" alt="Batam Good Transport customer photo 10" loading="lazy" /></figure>
      <figure class="gallery-item"><img src="images/gallery/gallery-11.webp" alt="Batam Good Transport customer photo 11" loading="lazy" /></figure>
      <figure class="gallery-item wide"><img src="images/gallery/gallery-12.webp" alt="Batam Good Transport customer photo 12" loading="lazy" /></figure>
      <figure class="gallery-item"><img src="images/gallery/gallery-13.webp" alt="Batam Good Transport customer photo 13" loading="lazy" /></figure>
      <figure class="gallery-item"><img src="images/gallery/gallery-14.webp" alt="Batam Good Transport customer photo 14" loading="lazy" /></figure>
      <figure class="gallery-item tall"><img src="images/gallery/gallery-15.webp" alt="Batam Good Transport customer photo 15" loading="lazy" /></figure>
      <figure class="gallery-item"><img src="images/gallery/gallery-16.webp" alt="Batam Good Transport customer photo 16" loading="lazy" /></figure>
      <figure class="gallery-item"><img src="images/gallery/gallery-17.webp" alt="Batam Good Transport customer photo 17" loading="lazy" /></figure>
      <figure class="gallery-item wide"><img src="images/gallery/gallery-18.webp" alt="Batam Good Transport customer photo 18" loading="lazy" /></figure>
    </div>
  </div>
</section>

'''

html = html[:i] + gallery + html[j:]

# 4. Add menu backdrop + lightbox overlay right before <script src="js/script.js" defer></script>
overlay = '''<!-- Mobile menu backdrop -->
<div class="menu-backdrop" id="menuBackdrop" hidden></div>

<!-- Image lightbox -->
<div class="lightbox" id="lightbox" aria-hidden="true" role="dialog" aria-label="Photo viewer">
  <button class="lightbox-close" id="lightboxClose" aria-label="Close"><i class="fa-solid fa-xmark"></i></button>
  <button class="lightbox-prev" id="lightboxPrev" aria-label="Previous photo"><i class="fa-solid fa-chevron-left"></i></button>
  <img class="lightbox-img" id="lightboxImg" src="" alt="" />
  <button class="lightbox-next" id="lightboxNext" aria-label="Next photo"><i class="fa-solid fa-chevron-right"></i></button>
  <div class="lightbox-counter" id="lightboxCounter"></div>
</div>

'''
anchor = '<script src="js/script.js" defer></script>'
assert anchor in html
html = html.replace(anchor, overlay + anchor)

with io.open(p, "w", encoding="utf-8") as f:
    f.write(html)
print("index.html patched OK. Length:", len(html))
