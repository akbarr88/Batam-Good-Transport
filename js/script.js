/* =========================================================
   Batam Good Transport — script.js
   Vanilla JS (ES6+). No frameworks.
   EDIT ZONE at the top: WhatsApp number, phone display,
   fleet data & prices, testimonials.
   ========================================================= */
'use strict';

/* =========================================================
   EDITABLE CONFIGURATION — change these values
   ========================================================= */
const CONFIG = {
  // WhatsApp number: country code + number, digits only, no '+', no spaces.
  // Example: Indonesia 62 + 85664085082  =>  "6285664085082"
  WHATSAPP_NUMBER: '6285664085082',

  // Display strings shown in the contact section / footer (formatted for humans).
  WHATSAPP_DISPLAY: '+62 856-6408-5082',
  PHONE_DISPLAY: '+62 856-6408-5082',

  // Default booking message template. {{VEHICLE}} and {{PACKAGE}} are auto-filled.
  BOOKING_TEMPLATE: `Hello, I would like to make a transportation booking in Batam.

Vehicle: {{VEHICLE}}
Package: {{PACKAGE}}
Name:
Travel Date:
Pick-Up Time:
Pick-Up Location:
Drop-Off Location:
Number of Passengers:
Additional Requests:

Please provide availability and pricing information.`,
};

/* ---------- FLEET DATA (editable: prices, capacities, features) ----------
   category: 'mpv' | 'premium' | 'van' | 'bus'  (matches filter buttons)
   prices: set numbers to show a price; use null to show "Contact for Price".
   Example price object:
     prices: { IDR: { oneWay: 350000, halfDay: 600000, fullDay: 900000 },
               SGD: { oneWay: 35, halfDay: 60, fullDay: 90 },
               MYR: { oneWay: 110, halfDay: 190, fullDay: 280 } }
   Leave as null (default) until you confirm real rates.
------------------------------------------------------------ */
const FLEET_DATA = [
  { slug:'toyota-avanza', name:'Toyota Avanza', category:'mpv', catLabel:'MPV', passengers:7, luggage:3,
    desc:'Compact and fuel-efficient MPV, ideal for small families and city transfers.',
    features:['AC','Bluetooth','Driver','Fuel'],
    prices:{ IDR:{oneWay:null,halfDay:385000,fullDay:605000}, SGD:{oneWay:10,halfDay:35,fullDay:55}, MYR:{oneWay:null,halfDay:120,fullDay:170} } },
  { slug:'mitsubishi-xpander', name:'Mitsubishi Xpander', category:'mpv', catLabel:'MPV', passengers:7, luggage:4,
    desc:'Spacious 7-seater with modern styling, great for families and day tours.',
    features:['AC','Bluetooth','Driver','Fuel','USB Charger'],
    prices:{ IDR:{oneWay:null,halfDay:385000,fullDay:605000}, SGD:{oneWay:10,halfDay:35,fullDay:55}, MYR:{oneWay:null,halfDay:120,fullDay:170} } },
  { slug:'toyota-innova-reborn', name:'Toyota Innova Reborn', category:'mpv', catLabel:'MPV', passengers:7, luggage:4,
    desc:'Reliable and comfortable MPV, a favourite for private transfers in Batam.',
    features:['AC','Driver','Fuel','Reclining Seats'],
    prices:{ IDR:{oneWay:null,halfDay:660000,fullDay:880000}, SGD:{oneWay:20,halfDay:60,fullDay:80}, MYR:{oneWay:null,halfDay:205,fullDay:220} } },
  { slug:'toyota-innova-zenix', name:'Toyota Innova Zenix', category:'premium', catLabel:'Premium MPV', passengers:7, luggage:4,
    desc:'Latest-generation premium MPV with hybrid option and a quiet, refined cabin.',
    features:['AC','Bluetooth','Driver','Fuel'],
    prices:{ IDR:{oneWay:null,halfDay:770000,fullDay:990000}, SGD:{oneWay:20,halfDay:70,fullDay:90}, MYR:{oneWay:null,halfDay:240,fullDay:280} } },
  { slug:'toyota-alphard', name:'Toyota Alphard', category:'premium', catLabel:'Luxury MPV', passengers:7, luggage:4,
    desc:'Executive luxury MPV — the ultimate comfort for VIP and business travellers.',
    features:['AC','Captain Seats','Driver','Fuel',],
    prices:{ IDR:{oneWay:null,halfDay:null,fullDay:3795000}, SGD:{oneWay:null,halfDay:null,fullDay:345}, MYR:{oneWay:null,halfDay:null,fullDay:1175} } },
  { slug:'toyota-fortuner', name:'Toyota Fortuner', category:'premium', catLabel:'SUV', passengers:7, luggage:4,
    desc:'Rugged yet comfortable SUV, perfect for longer trips and larger luggage.',
    features:['AC','Bluetooth','Driver','Fuel','SUV Power'],
    prices:{ IDR:{oneWay:null,halfDay:null,fullDay:1500000}, SGD:{oneWay:null,halfDay:null,fullDay:150}, MYR:{oneWay:null,halfDay:null,fullDay:400} } },
  { slug:'toyota-hiace-commuter', name:'Toyota Hiace Commuter', category:'van', catLabel:'Van', passengers:15, luggage:10,
    desc:'15-seat high-roof van for medium groups, airport transfers and tours.',
    features:['AC','Driver','Fuel','Ample Luggage'],
    prices:{ IDR:{oneWay:null,halfDay:770000,fullDay:1210000}, SGD:{oneWay:35,halfDay:70,fullDay:100}, MYR:{oneWay:null,halfDay:240,fullDay:320} } },
  { slug:'toyota-hiace-premio', name:'Toyota Hiace Premio', category:'van', catLabel:'Premium Van', passengers:15, luggage:10,
    desc:'Premium 15-seat van with extra comfort for corporate and group travel.',
    features:['AC','Driver','Fuel','Premium Interior'],
    prices:{ IDR:{oneWay:null,halfDay:770000,fullDay:1210000}, SGD:{oneWay:35,halfDay:70,fullDay:100}, MYR:{oneWay:null,halfDay:240,fullDay:320} } },
  { slug:'isuzu-elf-long', name:'Isuzu Elf Long', category:'bus', catLabel:'Minibus', passengers:19, luggage:15,
    desc:'18-seat minibus for medium-sized groups, tours and corporate outings.',
    features:['AC','Driver','Fuel','Luggage Space'],
    prices:{ IDR:{oneWay:null,halfDay:880000,fullDay:1256000}, SGD:{oneWay:40,halfDay:80,fullDay:110}, MYR:{oneWay:null,halfDay:270,fullDay:350} } },
  { slug:'toyota-coaster', name:'Toyota Coaster', category:'bus', catLabel:'Minibus', passengers:29, luggage:20,
    desc:'29-seat coaster bus — a dependable choice for larger tour groups.',
    features:['AC','Driver','Fuel','Aisle Seating'],
    prices:{ IDR:{oneWay:null,halfDay:null,fullDay:1650000}, SGD:{oneWay:null,halfDay:null,fullDay:150}, MYR:{oneWay:null,halfDay:null,fullDay:510} } },
  { slug:'medium-bus', name:'Medium Bus', category:'bus', catLabel:'Medium Bus', passengers:35, luggage:25,
    desc:'35-seat medium bus for corporate events, weddings and group excursions.',
    features:['AC','Driver','Fuel','Overhead Luggage'],
    prices:{ IDR:{oneWay:null,halfDay:null,fullDay:1980000}, SGD:{oneWay:null,halfDay:null,fullDay:180}, MYR:{oneWay:null,halfDay:null,fullDay:610} } },
  { slug:'big-bus', name:'Big Bus', category:'bus', catLabel:'Big Bus', passengers:59, luggage:40,
    desc:'59-seat big bus for large groups, school trips and big corporate events.',
    features:['AC','Driver','Fuel','Large Luggage Hold'],
    prices:{ IDR:{oneWay:null,halfDay:null,fullDay:2310000}, SGD:{oneWay:null,halfDay:null,fullDay:210}, MYR:{oneWay:null,halfDay:null,fullDay:715} } },
];

/* ---------- TESTIMONIALS (sample content — replace with verified reviews) ---------- */
const TESTIMONIALS = [
  { text:'"The driver was punctual, friendly and knew all the best spots. Our Batam city tour was smooth from start to finish."', name:'Michell', location:'Singapore', stars:5 },
  { text:'"Booked an airport transfer via WhatsApp — confirmation was fast and the vehicle was clean and comfortable. Highly recommended."', name:'Siti Hana', location:'Kuala Lumpur, Malaysia', stars:5 },
  { text:'"We rented a Hiace for our family group of 12. Plenty of space, great driver, and a very fair price. Will use again."', name:'Ahmad', location:'Jakarta, Indonesia', stars:5 },
];

/* =========================================================
   HELPERS
   ========================================================= */
const $  = (sel, ctx = document) => ctx.querySelector(sel);
const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));

/** Build a WhatsApp URL with an encoded message. */
function whatsappUrl(message) {
  return `https://wa.me/${CONFIG.WHATSAPP_NUMBER}?text=${encodeURIComponent(message)}`;
}

/** Build booking message from template. */
function bookingMessage(vehicle, pkg) {
  return CONFIG.BOOKING_TEMPLATE
    .replace('{{VEHICLE}}', vehicle || '—')
    .replace('{{PACKAGE}}', pkg || '—');
}

/** Open WhatsApp booking in a new tab. */
function openWhatsAppBooking(vehicle, pkg) {
  window.open(whatsappUrl(bookingMessage(vehicle, pkg)), '_blank', 'noopener');
}

/** Format a price number with currency symbol. */
function formatPrice(value, currency) {
  if (value === null || value === undefined || value === '') return null;
  const symbols = { IDR: 'Rp ', SGD: 'S$ ', MYR: 'RM ' };
  const num = Number(value);
  if (currency === 'IDR') return `${symbols.IDR}${num.toLocaleString('id-ID')}`;
  return `${symbols[currency] || ''}${num.toLocaleString('en-US')}`;
}

/* =========================================================
   1. FLEET RENDERING + FILTERS + CURRENCY
   ========================================================= */
let currentCurrency = 'IDR';
let currentFilter = 'all';

function priceCellHTML(price, label) {
  const formatted = formatPrice(price, currentCurrency);
  return formatted
    ? `<span class="val">${formatted}</span>`
    : `<span class="val contact">Contact for Price</span>`;
}

function renderFleet() {
  const grid = $('#fleetGrid');
  if (!grid) return;
  grid.innerHTML = FLEET_DATA.map(v => {
    const p = v.prices[currentCurrency] || {};
    const features = (v.features || []).map(f => `<span>${f}</span>`).join('');
    return `
    <article class="fleet-card" data-category="${v.category}">
      <div class="fleet-img">
        <img src="images/fleet/${v.slug}.webp" alt="${v.name} rental Batam" loading="lazy" />
        <span class="fleet-cat">${v.catLabel}</span>
      </div>
      <div class="fleet-body">
        <h3 class="fleet-name">${v.name}</h3>
        <div class="fleet-specs">
          <span class="fleet-spec"><i class="fa-solid fa-users"></i> ${v.passengers} Passengers</span>
          <span class="fleet-spec"><i class="fa-solid fa-suitcase-rolling"></i> ${v.luggage} Luggage</span>
        </div>
        <p class="fleet-desc">${v.desc}</p>
        <div class="fleet-features">${features}</div>
        <div class="fleet-pricing">
          <div class="fleet-pricing-title">Price · ${currentCurrency}</div>
          <div class="price-row"><span class="pkg">One Way Transfer</span>${priceCellHTML(p.oneWay)}</div>
          <div class="price-row"><span class="pkg">Half Day</span>${priceCellHTML(p.halfDay)}</div>
          <div class="price-row"><span class="pkg">Full Day</span>${priceCellHTML(p.fullDay)}</div>
        </div>
        <a href="#" class="btn btn-primary btn-sm fleet-book js-wa-book"
           data-vehicle="${v.name}" data-package="Please specify: One Way / Half Day / Full Day">
          <i class="fa-brands fa-whatsapp"></i> Book This Vehicle
        </a>
      </div>
    </article>`;
  }).join('');
  applyFilter();
  bindWhatsAppButtons(); // re-bind newly created buttons
}

function applyFilter() {
  $$('.fleet-card').forEach(card => {
    const show = currentFilter === 'all' || card.dataset.category === currentFilter;
    card.classList.toggle('hide', !show);
  });
}

function initFleet() {
  renderFleet();
  $$('.filter-btn').forEach(btn => btn.addEventListener('click', () => {
    $$('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentFilter = btn.dataset.filter;
    applyFilter();
  }));
  $$('.currency-btn').forEach(btn => btn.addEventListener('click', () => {
    $$('.currency-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    currentCurrency = btn.dataset.currency;
    renderFleet(); // re-render prices in chosen currency
  }));
}

/* =========================================================
   2. WHATSAPP BOOKING BUTTONS (all .js-wa-book elements)
   ========================================================= */
/** Close the slide-in mobile menu (if open) — called after tapping a book button inside it. */
function closeMobileMenu() {
  const mobileMenu = $('#mobileMenu');
  if (!mobileMenu || !mobileMenu.classList.contains('open')) return;
  const hamburger = $('#hamburger');
  const backdrop = $('#menuBackdrop');
  mobileMenu.classList.remove('open');
  if (hamburger) { hamburger.classList.remove('open'); hamburger.setAttribute('aria-expanded', 'false'); }
  mobileMenu.setAttribute('aria-hidden', 'true');
  document.body.classList.remove('menu-open');
  if (backdrop) { backdrop.classList.remove('show'); backdrop.hidden = true; }
}

function bindWhatsAppButtons() {
  $$('.js-wa-book').forEach(el => {
    if (el.dataset.waBound) return;
    el.dataset.waBound = '1';
    el.addEventListener('click', e => {
      e.preventDefault();
      closeMobileMenu();
      openWhatsAppBooking(el.dataset.vehicle || 'General Enquiry', el.dataset.package || 'General Enquiry');
    });
  });
}

/* =========================================================
   3. HEADER: sticky state, mobile menu, smooth scroll, active link
   ========================================================= */
function initHeader() {
  const header = $('#siteHeader');
  const hamburger = $('#hamburger');
  const mobileMenu = $('#mobileMenu');

  const onScroll = () => {
    header.classList.toggle('scrolled', window.scrollY > 40);
    $('#backToTop').classList.toggle('show', window.scrollY > 500);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu toggle
  const backdrop = $('#menuBackdrop');
  const toggleMenu = (force) => {
    const open = force !== undefined ? force : !mobileMenu.classList.contains('open');
    // Never allow the mobile menu to open on desktop widths
    if (open && window.innerWidth >= 1024) return;
    mobileMenu.classList.toggle('open', open);
    hamburger.classList.toggle('open', open);
    hamburger.setAttribute('aria-expanded', String(open));
    mobileMenu.setAttribute('aria-hidden', String(!open));
    document.body.classList.toggle('menu-open', open);
    if (backdrop) { backdrop.hidden = !open; backdrop.classList.toggle('show', open); }
  };
  hamburger.addEventListener('click', () => toggleMenu());
  if (backdrop) backdrop.addEventListener('click', () => toggleMenu(false));
  document.addEventListener('keydown', e => { if (e.key === 'Escape') toggleMenu(false); });
  // If the window is widened to desktop while the menu is open, close it automatically
  window.addEventListener('resize', () => { if (window.innerWidth >= 1024) toggleMenu(false); });

  // Smooth scroll with header offset + close mobile menu + active state
  $$('a[href^="#"]').forEach(link => {
    link.addEventListener('click', e => {
      const id = link.getAttribute('href');
      if (!id || id === '#') return;
      const target = $(id);
      if (!target) return;
      e.preventDefault();
      toggleMenu(false);
      const offset = 70;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });

  // Active nav link on scroll
  const sections = $$('section[id]');
  const navLinks = $$('.nav-link');
  const setActive = () => {
    const pos = window.scrollY + 120;
    let current = 'home';
    sections.forEach(s => { if (s.offsetTop <= pos) current = s.id; });
    navLinks.forEach(l => l.classList.toggle('active', l.getAttribute('href') === `#${current}`));
  };
  window.addEventListener('scroll', setActive, { passive: true });
  setActive();

  // Back to top
  $('#backToTop').addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
}

/* =========================================================
   4. FAQ ACCORDION — single open + smooth animation
   ========================================================= */
function initFaq() {
  const items = $$('.faq-item');
  items.forEach(item => {
    const summary = $('summary', item);
    const body = $('.faq-body', item);
    // set initial collapsed state
    body.style.maxHeight = '0px';
    body.style.overflow = 'hidden';
    body.style.transition = 'max-height .35s ease';

    summary.addEventListener('click', e => {
      e.preventDefault();
      const isOpen = item.hasAttribute('open');
      // close all
      items.forEach(other => {
        other.removeAttribute('open');
        const b = $('.faq-body', other);
        b.style.maxHeight = '0px';
      });
      // open clicked if it was closed
      if (!isOpen) {
        item.setAttribute('open', '');
        body.style.maxHeight = body.scrollHeight + 'px';
      }
    });
  });
}

/* =========================================================
   5. TESTIMONIAL SLIDER
   ========================================================= */
function initTestimonials() {
  const track = $('#testimonialTrack');
  const dotsWrap = $('#sliderDots');
  if (!track) return;
  let index = 0;
  let timer = null;

  track.innerHTML = TESTIMONIALS.map(t => `
    <div class="testimonial-slide">
      <div class="testimonial-card">
        <div class="testimonial-stars">${'★'.repeat(t.stars)}</div>
        <p class="testimonial-text">${t.text}</p>
        <div class="testimonial-author">${t.name}</div>
        <div class="testimonial-loc">${t.location} · Sample review</div>
      </div>
    </div>`).join('');

  dotsWrap.innerHTML = TESTIMONIALS.map((_, i) =>
    `<button class="slider-dot${i === 0 ? ' active' : ''}" data-i="${i}" aria-label="Go to review ${i + 1}"></button>`
  ).join('');

  const go = (i) => {
    index = (i + TESTIMONIALS.length) % TESTIMONIALS.length;
    track.style.transform = `translateX(-${index * 100}%)`;
    $$('.slider-dot', dotsWrap).forEach((d, di) => d.classList.toggle('active', di === index));
  };
  const autoplay = () => { clearInterval(timer); timer = setInterval(() => go(index + 1), 6000); };

  $('#prevTestimonial').addEventListener('click', () => { go(index - 1); autoplay(); });
  $('#nextTestimonial').addEventListener('click', () => { go(index + 1); autoplay(); });
  dotsWrap.addEventListener('click', e => {
    const dot = e.target.closest('.slider-dot');
    if (dot) { go(Number(dot.dataset.i)); autoplay(); }
  });

  // Touch swipe
  let startX = 0;
  track.addEventListener('touchstart', e => { startX = e.touches[0].clientX; }, { passive: true });
  track.addEventListener('touchend', e => {
    const dx = e.changedTouches[0].clientX - startX;
    if (Math.abs(dx) > 50) { go(dx < 0 ? index + 1 : index - 1); autoplay(); }
  }, { passive: true });

  autoplay();
}

/* =========================================================
   6. ANIMATED STAT COUNTERS
   ========================================================= */
function initCounters() {
  const nums = $$('.stat-num');
  if (!('IntersectionObserver' in window)) {
    nums.forEach(n => n.textContent = n.dataset.target + (n.dataset.suffix || ''));
    return;
  }
  const io = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      io.unobserve(el);
      const target = Number(el.dataset.target) || 0;
      const suffix = el.dataset.suffix || '';
      const duration = 1600;
      const start = performance.now();
      const tick = (now) => {
        const p = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - p, 3);
        el.textContent = Math.round(target * eased).toLocaleString() + suffix;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  }, { threshold: 0.4 });
  nums.forEach(n => io.observe(n));
}

/* =========================================================
   7. SCROLL REVEAL (IntersectionObserver)
   ========================================================= */
function initReveal() {
  const els = $$('.reveal');
  if (!('IntersectionObserver' in window)) { els.forEach(el => el.classList.add('visible')); return; }
  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  els.forEach(el => io.observe(el));
}

/* =========================================================
   8. CONTACT FORM — validate + open WhatsApp (no fake submit)
   ========================================================= */
function initContactForm() {
  const form = $('#contactForm');
  if (!form) return;
  const errorBox = $('#formError');

  const showError = (msg) => {
    errorBox.textContent = msg;
    errorBox.hidden = false;
  };
  const clearError = () => { errorBox.hidden = true; errorBox.textContent = ''; };

  form.addEventListener('submit', e => {
    e.preventDefault();
    clearError();
    const name = $('#cfName').value.trim();
    const phone = $('#cfPhone').value.trim();
    const email = $('#cfEmail').value.trim();
    const subject = $('#cfSubject').value;
    const message = $('#cfMessage').value.trim();

    // validation
    let ok = true;
    const mark = (el, invalid) => { el.classList.toggle('invalid', invalid); if (invalid) ok = false; };
    mark($('#cfName'), name.length < 2);
    mark($('#cfPhone'), phone.length < 6);
    mark($('#cfMessage'), message.length < 5);
    if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { mark($('#cfEmail'), true); }

    if (!ok) { showError('Please fill in the required fields (name, phone, message) with valid information.'); return; }

    const full = `Hello Batam Good Transport,

Subject: ${subject}
Name: ${name}
Phone/WhatsApp: ${phone}
Email: ${email || '—'}

${message}

Please reply with availability and pricing. Thank you.`;

    window.open(whatsappUrl(full), '_blank', 'noopener');
  });

  // clear invalid styling on input
  form.addEventListener('input', e => e.target.classList.remove('invalid'));
}

/* =========================================================
   9. MISC: year, contact display strings
   ========================================================= */
function initMisc() {
  const y = $('#year'); if (y) y.textContent = new Date().getFullYear();
  $$('.js-wa-display').forEach(el => el.textContent = CONFIG.WHATSAPP_DISPLAY);
  $$('.js-phone-display').forEach(el => el.textContent = CONFIG.PHONE_DISPLAY);
}

/* =========================================================
   9b. IMAGE FALLBACK — if a .webp photo is missing, silently
   fall back to the .svg placeholder. Remove once real .webp
   photos are in place.
   ========================================================= */
function initImageFallback() {
  // <img> tags: swap .webp -> .svg on load error (capture phase)
  document.addEventListener('error', e => {
    const img = e.target;
    if (img && img.tagName === 'IMG' && /\.webp($|\?)/i.test(img.src) && !img.dataset.fallback) {
      img.dataset.fallback = '1';
      img.src = img.src.replace(/\.webp($|\?)/i, '.svg$1');
    }
  }, true);

  // Hero CSS background-image fallback (no onerror for CSS backgrounds)
  const heroBg = document.querySelector('.hero-bg');
  if (heroBg) {
    const probe = new Image();
    probe.onerror = () => { heroBg.style.backgroundImage = "url('images/hero.svg')"; };
    probe.src = 'images/hero.webp';
  }
}

/* =========================================================
   10. GALLERY LIGHTBOX — click any gallery photo to enlarge
   ========================================================= */
function initGalleryLightbox() {
  const grid = $('#galleryGrid');
  const lightbox = $('#lightbox');
  if (!grid || !lightbox) return;
  const imgs = $$('.gallery-item img', grid);
  const lbImg = $('#lightboxImg');
  const counter = $('#lightboxCounter');
  let index = 0;

  const show = (i) => {
    index = (i + imgs.length) % imgs.length;
    lbImg.src = imgs[index].src;
    lbImg.alt = imgs[index].alt || '';
    if (counter) counter.textContent = `${index + 1} / ${imgs.length}`;
    lightbox.classList.add('open');
    lightbox.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  };
  const close = () => {
    lightbox.classList.remove('open');
    lightbox.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  };

  grid.addEventListener('click', e => {
    const item = e.target.closest('.gallery-item');
    if (!item) return;
    const img = $('img', item);
    show(imgs.indexOf(img));
  });
  $('#lightboxClose').addEventListener('click', close);
  $('#lightboxPrev').addEventListener('click', () => show(index - 1));
  $('#lightboxNext').addEventListener('click', () => show(index + 1));
  lightbox.addEventListener('click', e => { if (e.target === lightbox) close(); });
  document.addEventListener('keydown', e => {
    if (!lightbox.classList.contains('open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowLeft') show(index - 1);
    if (e.key === 'ArrowRight') show(index + 1);
  });
}

/* =========================================================
   BOOT
   ========================================================= */
document.addEventListener('DOMContentLoaded', () => {
  initMisc();
  initImageFallback();
  initFleet();
  bindWhatsAppButtons();
  initHeader();
  initFaq();
  initTestimonials();
  initCounters();
  initReveal();
  initContactForm();
  initGalleryLightbox();
});
