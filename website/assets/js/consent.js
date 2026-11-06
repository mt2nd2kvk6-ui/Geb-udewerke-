/* Gebäudewerke: Einwilligung für Google Analytics 4
   Google Analytics wird erst nach ausdrücklicher Zustimmung geladen.
   Entscheidung im localStorage unter gw_consent: "granted" oder "denied".
   Banner erneut öffnen: jedes Element mit data-cookie-einstellungen.

   Ergänzung 06.11.2026: Google Consent Mode v2.
   Beim Seitenaufruf wird nur ein lokaler Standard "alles denied" in den dataLayer
   geschrieben (ohne Netzwerk). Erst nach "Alle akzeptieren" wird analytics_storage
   auf "granted" gesetzt und gtag.js geladen. Werbe-Signale (ad_storage,
   ad_user_data, ad_personalization) bleiben immer "denied". Ohne Zustimmung
   geht keine Anfrage an Google.

   Alle Ereignisse laufen über window.gwEreignis(name, daten), siehe tracking.js.
   Jedes Ereignis bekommt automatisch: seite (Pfad), zielgruppe (meta name="zielgruppe",
   falls vorhanden) und, falls vom Aufrufer übergeben, position. */
(function () {
  'use strict';
  var MESS_ID = 'G-PKEXEYK6CG';
  var SCHLUESSEL = 'gw_consent';
  var gaGeladen = false;
  var banner = null;

  function lesen() {
    try { return window.localStorage.getItem(SCHLUESSEL); } catch (e) { return null; }
  }
  function speichern(wert) {
    try { window.localStorage.setItem(SCHLUESSEL, wert); } catch (e) { /* Speicher gesperrt */ }
  }

  /* Consent Mode v2: Standard ohne Netzwerkzugriff, nur lokaler dataLayer */
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
  window.gtag('consent', 'default', {
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    analytics_storage: 'denied',
    wait_for_update: 500
  });

  function gaLaden() {
    window['ga-disable-' + MESS_ID] = false;
    window.gtag('consent', 'update', { analytics_storage: 'granted' });
    if (gaGeladen) return;
    gaGeladen = true;
    window.gtag('js', new Date());
    window.gtag('config', MESS_ID, {
      allow_google_signals: false,
      allow_ad_personalization_signals: false
    });
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + MESS_ID;
    document.head.appendChild(s);
    dankeSeite();
    document.dispatchEvent(new CustomEvent('gw:consent', { detail: 'granted' }));
  }

  function gaStoppen() {
    window['ga-disable-' + MESS_ID] = true;
    window.gtag('consent', 'update', { analytics_storage: 'denied' });
    var host = window.location.hostname;
    var domains = ['', host, '.' + host];
    var teile = host.split('.');
    if (teile.length > 2) domains.push('.' + teile.slice(-2).join('.'));
    document.cookie.split(';').forEach(function (c) {
      var name = c.split('=')[0].trim();
      if (name.indexOf('_ga') !== 0) return;
      domains.forEach(function (d) {
        document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + (d ? '; domain=' + d : '');
      });
    });
  }

  function entscheiden(wert) {
    speichern(wert);
    if (wert === 'granted') gaLaden(); else gaStoppen();
    schliessen();
  }

  function bauen() {
    if (banner) return banner;
    banner = document.createElement('div');
    banner.className = 'cookie-banner';
    banner.id = 'cookie-banner';
    banner.setAttribute('role', 'region');
    banner.setAttribute('aria-labelledby', 'cookie-banner-titel');
    banner.hidden = true;
    banner.innerHTML =
      '<div class="cookie-banner__inhalt">' +
        '<div>' +
          '<p class="cookie-banner__titel" id="cookie-banner-titel">Ihre Zustimmung zur Statistik</p>' +
          '<p class="cookie-banner__text">Mit Ihrer Zustimmung messen wir mit Google Analytics, wie unsere Website genutzt wird. Dabei werden Cookies gesetzt und Daten an Google übermittelt, auch in die USA. Ändern können Sie Ihre Entscheidung jederzeit über „Cookie-Einstellungen“ im Seitenfuß. Mehr dazu in der <a href="/datenschutz.html#google-analytics">Datenschutzerklärung</a>.</p>' +
        '</div>' +
        '<div class="cookie-banner__knoepfe">' +
          '<button type="button" class="cookie-banner__knopf" data-einwilligung="granted">Alle akzeptieren</button>' +
          '<button type="button" class="cookie-banner__knopf" data-einwilligung="denied">Nur notwendige</button>' +
        '</div>' +
      '</div>';
    banner.addEventListener('click', function (e) {
      var knopf = e.target.closest ? e.target.closest('[data-einwilligung]') : null;
      if (knopf) entscheiden(knopf.getAttribute('data-einwilligung'));
    });
    document.body.appendChild(banner);
    return banner;
  }

  var ausloeser = null;
  function oeffnen(fokus) {
    bauen().hidden = false;
    if (fokus) {
      var erster = banner.querySelector('button');
      if (erster) erster.focus();
    }
  }
  function schliessen() {
    if (!banner) return;
    banner.hidden = true;
    if (ausloeser && document.contains(ausloeser)) ausloeser.focus();
    ausloeser = null;
  }

  /* Zentrale Ereignisfunktion. Wird nur gesendet, wenn GA4 nach Zustimmung geladen ist.
     Standardparameter: seite (Pfad), zielgruppe (aus <meta name="zielgruppe">), position (falls übergeben).
     Die Klick- und Scroll-Ereignisse selbst stehen in assets/js/tracking.js. */
  var zielgruppeMeta = document.querySelector('meta[name="zielgruppe"]');
  var ZIELGRUPPE = zielgruppeMeta ? zielgruppeMeta.getAttribute('content') : '';
  function ereignis(name, daten) {
    if (!gaGeladen || lesen() !== 'granted' || typeof window.gtag !== 'function') return false;
    daten = daten || {};
    daten.seite = window.location.pathname;
    if (ZIELGRUPPE && !daten.zielgruppe) daten.zielgruppe = ZIELGRUPPE;
    daten.transport_type = 'beacon';
    window.gtag('event', name, daten);
    return true;
  }
  window.gwEreignis = ereignis;
  window.gwZustimmung = function () { return gaGeladen && lesen() === 'granted'; };

  /* generate_lead = Anfrageformular erfolgreich gesendet (Aufruf von danke.html) */
  function dankeSeite() {
    if (/\/danke(\.html)?$/.test(window.location.pathname)) {
      ereignis('generate_lead', { formular: 'anfrage', position: 'inhalt' });
    }
  }

  function start() {
    document.addEventListener('click', function (e) {
      var link = e.target.closest ? e.target.closest('[data-cookie-einstellungen]') : null;
      if (!link) return;
      e.preventDefault();
      ausloeser = link;
      oeffnen(true);
    });
    var wert = lesen();
    if (wert === 'granted') gaLaden();
    else if (wert !== 'denied') {
      oeffnen(false);
      // Erster Besuch: Serverregeln anlegen, falls sie nach dem Entpacken noch fehlen
      try { fetch('/einrichtung.php', { cache: 'no-store', credentials: 'omit' }).catch(function () {}); } catch (e) { /* ältere Browser */ }
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
