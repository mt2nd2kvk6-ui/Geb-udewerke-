(function () {
  var nav = document.getElementById('hauptnavigation');
  var schleier = document.querySelector('.nav-schleier');
  var oeffnen = document.getElementById('menue-oeffnen');
  var schliessen = document.querySelector('.nav__schliessen');
  var ruhig = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function menue(offen) {
    if (!nav) return;
    nav.classList.toggle('offen', offen);
    if (schleier) schleier.classList.toggle('offen', offen);
    if (oeffnen) oeffnen.setAttribute('aria-expanded', offen ? 'true' : 'false');
    document.body.style.overflow = offen ? 'hidden' : '';
    if (offen && schliessen) schliessen.focus();
  }
  if (oeffnen) oeffnen.addEventListener('click', function () { menue(true); });
  if (schliessen) schliessen.addEventListener('click', function () { menue(false); if (oeffnen) oeffnen.focus(); });
  if (schleier) schleier.addEventListener('click', function () { menue(false); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav && nav.classList.contains('offen')) { menue(false); if (oeffnen) oeffnen.focus(); }
  });
  // Sprungziele im mobilen Menü (z. B. /#fragen) schließen das Menü
  if (nav) nav.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href*="#"]') : null;
    if (a && nav.classList.contains('offen')) menue(false);
  });

  // Untermenü Leistungen (Tastatur und Mobil)
  document.querySelectorAll('[data-untermenue]').forEach(function (knopf) {
    var liste = document.getElementById(knopf.getAttribute('aria-controls'));
    knopf.addEventListener('click', function () {
      var offen = knopf.getAttribute('aria-expanded') === 'true';
      knopf.setAttribute('aria-expanded', offen ? 'false' : 'true');
      if (liste) liste.classList.toggle('offen', !offen);
    });
  });

  // Formular: Vorschau, bis Versand angebunden ist.
  // Nach Anbindung (Formulardienst oder PHP beim Hoster) das Attribut data-vorschau im HTML entfernen.
  document.querySelectorAll('form[data-vorschau]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var meldung = form.querySelector('.formular__meldung');
      if (meldung) {
        meldung.hidden = false;
        meldung.focus();
      }
    });
  });

  // Kopfbereich wird beim Scrollen kompakter (nur transform, kein Layoutsprung)
  var kopf = document.querySelector('.kopf');
  if (kopf) {
    var geplant = false;
    var pruefen = function () {
      geplant = false;
      kopf.classList.toggle('kopf--kompakt', window.scrollY > 60);
    };
    window.addEventListener('scroll', function () {
      if (!geplant) { geplant = true; window.requestAnimationFrame(pruefen); }
    }, { passive: true });
    pruefen();
  }

  // Sanftes Einblenden beim Scrollen (nur Elemente unterhalb des sichtbaren Bereichs)
  if (!ruhig && 'IntersectionObserver' in window) {
    var auswahl = '.abschnitt__kopf,.zusage,.lv__zeile,.zielgruppe,.ablauf>li,.team-karte,.faq,.antwort,.umfang__gruppe,' +
      '.ratgeber-karte,.teaser,.kosten,.karte,.steckbrief,.bewertungen__kopf,.laufband,.hinweisbox,.pruefliste,.stelle,.cta-band .wrap,.fuss__cta';
    var hoehe = window.innerHeight || 800;
    var beobachter = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('sichtbar'); beobachter.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    document.querySelectorAll(auswahl).forEach(function (el) {
      if (el.getBoundingClientRect().top < hoehe) return;
      var geschwister = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
      el.style.setProperty('--verz', (Math.min(geschwister, 5) * 0.07) + 's');
      el.classList.add('einblenden');
      beobachter.observe(el);
    });
  }

  // Bewertungs-Laufband: läuft nur ohne prefers-reduced-motion, sonst statisch und horizontal scrollbar
  document.querySelectorAll('[data-laufband]').forEach(function (band) {
    var knopf = band.parentElement && band.parentElement.querySelector('.laufband__knopf');
    var gruppe = band.querySelector('.laufband__gruppe');
    if (ruhig || !gruppe) return;
    band.classList.add('laufband--laeuft');
    var dauer = function () { band.style.setProperty('--dauer', Math.max(30, gruppe.scrollWidth / 38) + 's'); };
    dauer();
    window.addEventListener('resize', dauer, { passive: true });
    if (knopf) {
      var text = knopf.querySelector('span');
      knopf.hidden = false;
      knopf.addEventListener('click', function () {
        var pause = band.classList.toggle('laufband--pause');
        if (text) text.textContent = pause ? 'Laufband fortsetzen' : 'Laufband anhalten';
      });
    }
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (e) {
        band.classList.toggle('laufband--aus', !e[0].isIntersecting);
      }).observe(band);
    }
  });
})();

// Zwei-Klick-Karte: Google Maps wird erst nach Klick geladen
document.querySelectorAll('[data-karte-laden]').forEach(function (knopf) {
  knopf.addEventListener('click', function () {
    var box = knopf.closest('.karte');
    if (!box) return;
    var f = document.createElement('iframe');
    f.src = box.getAttribute('data-karte');
    f.title = 'Karte: Gebäudewerke GbR, Allmend 2, 76707 Hambrücken';
    f.loading = 'lazy';
    f.referrerPolicy = 'no-referrer-when-downgrade';
    f.setAttribute('allowfullscreen', '');
    box.innerHTML = '';
    box.appendChild(f);
  });
});
