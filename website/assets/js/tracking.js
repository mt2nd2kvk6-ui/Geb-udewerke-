/* Gebäudewerke: Ereignisse für Google Analytics 4 (Stand 06.11.2026)
   Alles läuft über window.gwEreignis(name, daten) aus consent.js. Ohne Zustimmung
   wird nichts gesendet. Jedes Ereignis bekommt seite, zielgruppe (falls die Seite
   eine hat) und position: kopf, hero, inhalt, kontaktblock, mobilleiste, schnellkontakt, fuss.
   Die Position kommt aus dem nächsten Vorfahren mit data-pos="…", sonst aus der Klasse.

   Ereignisse (Parameter in Klammern):
     anruf_klick, whatsapp_klick, email_klick (position, link_text)
     cta_klick (position, cta_text, ziel)
     google_bewertung_klick, bewertung_schreiben_klick (position)
     formular_start (formular), formular_fehler (formular)
     scroll_tiefe (prozent: 25, 50, 75, 90)
     abschnitt_gesehen (abschnitt), preis_ansicht (tabelle)
     faq_geoeffnet (frage), aufklappen (titel)
     ratgeber_gelesen (thema, titel)
     karte_geladen, laufband_pause (zustand), menue_geoeffnet
     seite_teilen (kanal), ausgehender_link (ziel, url)
     fehlerseite (adresse)
   generate_lead sendet consent.js auf der Danke-Seite. */
(function () {
  'use strict';
  function senden(name, daten) {
    if (typeof window.gwEreignis === 'function') window.gwEreignis(name, daten);
  }
  var POS = { kopf: '.kopf', hero: '.hero,.seitenkopf', mobilleiste: '.mobilleiste', schnellkontakt: '.schnellkontakt', fuss: '.fuss', kontaktblock: '.kontaktblock,.cta-band,.kontakt-block' };
  function position(el) {
    var p = el && el.closest ? el.closest('[data-pos]') : null;
    if (p) return p.getAttribute('data-pos');
    for (var k in POS) { if (el && el.closest && el.closest(POS[k])) return k; }
    return 'inhalt';
  }
  function text(el) { return (el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 80); }
  var pfad = window.location.pathname;

  /* Klicks: Anruf, WhatsApp, E-Mail, Bewertung, Teilen, CTA, Karte, Laufband, Menü, externe Links */
  document.addEventListener('click', function (e) {
    var ziel = e.target.closest ? e.target.closest('a[href],button') : null;
    if (!ziel) return;
    var pos = position(ziel);
    if (ziel.tagName === 'BUTTON') {
      if (ziel.hasAttribute('data-karte-laden')) senden('karte_geladen', { position: pos });
      else if (ziel.classList.contains('laufband__knopf')) senden('laufband_pause', { position: pos, zustand: /fortsetzen/i.test(text(ziel)) ? 'fortgesetzt' : 'angehalten' });
      else if (ziel.id === 'menue-oeffnen') senden('menue_geoeffnet', { position: pos });
      return;
    }
    var href = ziel.getAttribute('href') || '';
    var t = text(ziel) || ziel.getAttribute('aria-label') || '';
    if (href.indexOf('tel:') === 0) { senden('anruf_klick', { position: pos, link_text: t }); return; }
    if (/api\.whatsapp\.com\/send\?phone=|wa\.me\/\d/.test(href)) { senden('whatsapp_klick', { position: pos, link_text: t }); return; }
    if (/^mailto:info@/i.test(href)) { senden('email_klick', { position: pos, link_text: t }); return; }
    if (ziel.closest('.teilen')) {
      if (/wa\.me\/\?text=|whatsapp/i.test(href)) { senden('seite_teilen', { position: pos, kanal: 'whatsapp' }); return; }
      if (/^mailto:/i.test(href)) { senden('seite_teilen', { position: pos, kanal: 'email' }); return; }
    }
    if (/search\.google\.com\/local\/writereview/.test(href)) { senden('bewertung_schreiben_klick', { position: pos }); return; }
    if (/share\.google\/|google\.com\/maps\?cid=/.test(href)) { senden('google_bewertung_klick', { position: pos }); return; }
    if (ziel.hasAttribute('data-cta') || (ziel.classList.contains('btn') && /kontakt\.html|#anfrage|#kontakt/.test(href))) {
      senden('cta_klick', { position: pos, cta_text: ziel.getAttribute('data-cta') || t, ziel: href });
    }
    if (/^https?:\/\//i.test(href)) {
      var a = document.createElement('a'); a.href = href;
      if (a.hostname && a.hostname !== window.location.hostname && a.hostname !== 'gebaeudewerke.de') {
        senden('ausgehender_link', { position: pos, ziel: a.hostname, url: href.slice(0, 100) });
      }
    }
  }, true);

  /* Formular: erstes ausgefülltes Feld */
  var formStart = false;
  document.addEventListener('input', function (e) {
    if (formStart) return;
    var f = e.target && e.target.closest ? e.target.closest('form[action$="anfrage.php"]') : null;
    if (!f) return;
    formStart = true;
    senden('formular_start', { position: position(f), formular: (f.querySelector('input[name="seite"]') || {}).value || f.id || 'anfrage' });
  }, true);

  /* Seitenabhängige Ereignisse */
  if (/\/anfrage-fehler(\.html)?$/.test(pfad)) senden('formular_fehler', { formular: 'anfrage', position: 'inhalt' });
  if (document.body.hasAttribute('data-fehlerseite')) senden('fehlerseite', { adresse: pfad + window.location.search, position: 'inhalt' });

  /* Aufklappen: FAQ und andere Details */
  document.addEventListener('toggle', function (e) {
    var d = e.target;
    if (!d || d.tagName !== 'DETAILS' || !d.open) return;
    var s = d.querySelector('summary');
    if (d.closest('.faq')) senden('faq_geoeffnet', { position: position(d), frage: text(s) });
    else senden('aufklappen', { position: position(d), titel: text(s) });
  }, true);

  /* Scrolltiefe, Abschnitte, Preistabellen, Ratgeber gelesen */
  var marken = [25, 50, 75, 90], gesendet = {};
  function tiefe() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    if (h <= 0) return;
    var p = Math.round((window.scrollY / h) * 100);
    marken.forEach(function (m) { if (p >= m && !gesendet[m]) { gesendet[m] = true; senden('scroll_tiefe', { prozent: m, position: 'inhalt' }); } });
    if (artikel && !gesendet.artikel) {
      var r = artikel.getBoundingClientRect();
      if (window.innerHeight - r.top >= r.height * 0.75) {
        gesendet.artikel = true;
        var m = document.querySelector('meta[name="artikel-thema"]'), h1 = document.querySelector('h1');
        senden('ratgeber_gelesen', { thema: m ? m.getAttribute('content') : '', titel: h1 ? text(h1) : '', position: 'inhalt' });
      }
    }
  }
  /* Ratgeber: 75 % des Artikels gelesen (nur Seiten mit <meta name="artikel-datum">) */
  var artikel = document.querySelector('meta[name="artikel-datum"]') ? document.querySelector('main article, main') : null;
  var geplant = false;
  window.addEventListener('scroll', function () { if (!geplant) { geplant = true; requestAnimationFrame(function () { geplant = false; tiefe(); }); } }, { passive: true });

  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (eintraege) {
      eintraege.forEach(function (x) {
        if (!x.isIntersecting) return;
        io.unobserve(x.target);
        var el = x.target;
        if (el.hasAttribute('data-preistabelle')) senden('preis_ansicht', { tabelle: el.getAttribute('data-preistabelle'), position: 'inhalt' });
        else senden('abschnitt_gesehen', { abschnitt: el.getAttribute('data-abschnitt'), position: position(el) });
      });
    }, { threshold: 0.25 });
    document.querySelectorAll('[data-abschnitt],[data-preistabelle]').forEach(function (el) { io.observe(el); });
  }
})();
