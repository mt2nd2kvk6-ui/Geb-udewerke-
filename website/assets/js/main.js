/* Gebäudewerke: Bedienung und Bewegung. Alle Inhalte stehen im HTML, das Skript ergänzt nur
   Menü, Live-Werte und Bewegung. Bewegung nur über transform und opacity, bei „Bewegung reduzieren“ still. */
(function () {
  'use strict';
  var ruhig = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function spaeter(fn) {
    var los = function () { (window.requestIdleCallback || function (f) { return setTimeout(f, 1); })(fn, { timeout: 1500 }); };
    if (document.readyState === 'complete') los(); else window.addEventListener('load', los);
  }

  /* ---------- Menü ---------- */
  var nav = document.getElementById('hauptnavigation');
  var oeffnen = document.getElementById('menue-oeffnen');
  var schliessen = $('.nav__schliessen');
  function menue(offen) {
    if (!nav) return;
    nav.classList.toggle('offen', offen);
    if (oeffnen) oeffnen.setAttribute('aria-expanded', offen ? 'true' : 'false');
    document.body.style.overflow = offen ? 'hidden' : '';
    if (offen && schliessen) schliessen.focus();
    if (offen) document.dispatchEvent(new CustomEvent('gw:menue'));
  }
  if (oeffnen) oeffnen.addEventListener('click', function () { menue(true); });
  if (schliessen) schliessen.addEventListener('click', function () { menue(false); if (oeffnen) oeffnen.focus(); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav && nav.classList.contains('offen')) { menue(false); if (oeffnen) oeffnen.focus(); }
  });
  if (nav) nav.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href*="#"]') : null;
    if (a && nav.classList.contains('offen')) menue(false);
  });
  $$('[data-untermenue]').forEach(function (knopf) {
    var liste = document.getElementById(knopf.getAttribute('aria-controls'));
    knopf.addEventListener('click', function () {
      var offen = knopf.getAttribute('aria-expanded') === 'true';
      knopf.setAttribute('aria-expanded', offen ? 'false' : 'true');
      if (liste) liste.classList.toggle('offen', !offen);
    });
  });

  /* ---------- Formular-Vorschau (nur solange data-vorschau gesetzt ist) ---------- */
  $$('form[data-vorschau]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var m = $('.formular__meldung', form);
      if (m) { m.hidden = false; m.focus(); }
    });
  });

  /* ---------- Sanftes Einblenden unterhalb des ersten Bildschirms ---------- */
  if (!ruhig && 'IntersectionObserver' in window) spaeter(function () {
    var auswahl = '.abschnitt__kopf,.kopfteil,.antwort,.umfang__gruppe,.ablauf>li,.teaser,.leistung,.person,.zusagen>li,' +
      '.steckbrief,.stelle,.ratgeber-karte,.pruefliste,.kosten,.start-ratgeber>li,.faq';
    var hoehe = window.innerHeight || 800;
    var b = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('sichtbar'); b.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    $$(auswahl).forEach(function (el) {
      if (el.getBoundingClientRect().top < hoehe) return;
      var i = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
      el.style.setProperty('--verz', (Math.min(i, 5) * 0.06) + 's');
      el.classList.add('einblenden');
      b.observe(el);
    });
  });

  /* ---------- Bewertungen: Laufband (Kopie nur für die Schleife, nicht im HTML) ---------- */
  spaeter(function () {
    $$('[data-laufband]').forEach(function (band) {
      var gruppe = $('.laufband__gruppe', band);
      var knopf = band.parentElement && band.parentElement.querySelector('.laufband__knopf');
      if (ruhig || !gruppe) return;
      if (!$('.laufband__gruppe[aria-hidden="true"]', band)) {
        var kopie = gruppe.cloneNode(true);
        kopie.setAttribute('aria-hidden', 'true');
        $$('[role="img"]', kopie).forEach(function (e) { e.removeAttribute('role'); e.removeAttribute('aria-label'); e.setAttribute('aria-hidden', 'true'); });
        gruppe.parentNode.appendChild(kopie);
      }
      band.classList.add('laufband--laeuft');
      band.style.setProperty('--dauer', Math.max(40, gruppe.scrollWidth / 30) + 's');
      if (knopf) {
        var text = $('span', knopf);
        knopf.hidden = false;
        knopf.addEventListener('click', function () {
          var pause = band.classList.toggle('laufband--pause');
          if (text) text.textContent = pause ? 'Laufband fortsetzen' : 'Laufband anhalten';
          if (pause) document.dispatchEvent(new CustomEvent('gw:laufband'));
        });
      }
      if ('IntersectionObserver' in window) new IntersectionObserver(function (e) { band.classList.toggle('laufband--aus', !e[0].isIntersecting); }).observe(band);
    });
  });

  /* ---------- Zwei-Klick-Karte: Google Maps erst nach Klick ---------- */
  $$('[data-karte-laden]').forEach(function (knopf) {
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
      document.dispatchEvent(new CustomEvent('gw:karte'));
    });
  });

  /* ================= Startseite ================= */

  /* ---------- Zeit, Feiertage und Sonne in Bruchsal ---------- */
  var LAT = 49.1291927, LON = 8.5914434;
  var WT = ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'];
  var MON = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'];
  var zwei = function (n) { return (n < 10 ? '0' : '') + n; };
  function berlin(d) {
    var t = {};
    new Intl.DateTimeFormat('de-DE', { timeZone: 'Europe/Berlin', year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', hourCycle: 'h23', weekday: 'long' })
      .formatToParts(d).forEach(function (p) { t[p.type] = p.value; });
    return { j: +t.year, m: +t.month, t: +t.day, std: +t.hour, min: +t.minute, wt: WT.indexOf(t.weekday) };
  }
  function uhrzeit(d) { var b = berlin(d); return zwei(b.std) + ':' + zwei(b.min); }
  function ostern(j) {
    var a = j % 19, b = Math.floor(j / 100), c = j % 100, d = Math.floor(b / 4), e = b % 4, f = Math.floor((b + 8) / 25), g = Math.floor((b - f + 1) / 3),
      h = (19 * a + b - d - g + 15) % 30, i = Math.floor(c / 4), k = c % 4, l = (32 + 2 * e + 2 * i - h - k) % 7, m = Math.floor((a + 11 * h + 22 * l) / 451);
    return Date.UTC(j, Math.floor((h + l - 7 * m + 114) / 31) - 1, ((h + l - 7 * m + 114) % 31) + 1);
  }
  function feiertagBW(b) {
    if (['1.1', '6.1', '1.5', '3.10', '1.11', '25.12', '26.12'].indexOf(b.t + '.' + b.m) > -1) return true;
    var o = ostern(b.j), heute = Date.UTC(b.j, b.m - 1, b.t);
    return [-2, 1, 39, 50, 60].some(function (x) { return heute === o + x * 864e5; });
  }
  function sonne(d) {
    var r = Math.PI / 180, jd = d.getTime() / 864e5 + 2440587.5, n = Math.ceil(jd - 2451545 + 0.0008), js = n - LON / 360,
      M = (357.5291 + 0.98560028 * js) % 360, C = 1.9148 * Math.sin(M * r) + 0.02 * Math.sin(2 * M * r) + 0.0003 * Math.sin(3 * M * r),
      L = (M + C + 180 + 102.9372) % 360, jt = 2451545 + js + 0.0053 * Math.sin(M * r) - 0.0069 * Math.sin(2 * L * r),
      dek = Math.asin(Math.sin(L * r) * Math.sin(23.4397 * r)),
      w = Math.acos((Math.sin(-0.833 * r) - Math.sin(LAT * r) * Math.sin(dek)) / (Math.cos(LAT * r) * Math.cos(dek))) / r;
    var ms = function (j) { return new Date((j - 2440587.5) * 864e5); };
    return { auf: ms(jt - w / 360), unter: ms(jt + w / 360) };
  }

  /* ---------- Modell: Lichtkegel und Wetter ---------- */
  var modell = document.getElementById('modell');
  if (modell) {
    var zonen = $$('.welt .zone', modell), punkte = $$('.punkt', modell), links10 = $$('.liste10 a'), unter = document.getElementById('unterzeile');
    var tour = ['keller', 'treppenhaus', 'wohnung', 'reparatur', 'buero', 'hausmeister', 'gewerbe', 'winter', 'metall', 'garten'];
    var ti = 0, pause = false, sichtbar = true;
    var zeigen = function (z) {
      modell.classList.toggle('fokus', !!z);
      var spot = $('.spot', modell); spot.innerHTML = '';
      zonen.forEach(function (g) { if (g.getAttribute('data-zone') === z) spot.appendChild(g.cloneNode(true)); });
      punkte.forEach(function (p) { p.classList.toggle('an', p.getAttribute('data-zone') === z); });
      links10.forEach(function (a) { a.classList.toggle('an', a.getAttribute('data-zone') === z); });
      var p = punkte.filter(function (x) { return x.getAttribute('data-zone') === z; })[0];
      if (p && unter) { $('b', unter).textContent = $('b', p).textContent; $('small', unter).textContent = $('small', p).textContent; }
    };
    [modell, $('.liste10')].forEach(function (el) {
      if (!el) return;
      el.addEventListener('mouseenter', function () { pause = true; });
      el.addEventListener('mouseleave', function () { pause = false; });
      el.addEventListener('focusin', function () { pause = true; });
      el.addEventListener('focusout', function () { pause = false; });
    });
    punkte.concat(links10).forEach(function (el) {
      var z = el.getAttribute('data-zone');
      el.addEventListener('mouseenter', function () { zeigen(z); ti = tour.indexOf(z) + 1; });
      el.addEventListener('focus', function () { zeigen(z); ti = tour.indexOf(z) + 1; });
    });
    if ('IntersectionObserver' in window) new IntersectionObserver(function (e) { sichtbar = e[0].isIntersecting; }).observe(modell);
    if (!ruhig) setTimeout(function () {
      zeigen(tour[ti++]);
      setInterval(function () { if (!pause && sichtbar && !document.hidden) zeigen(tour[ti++ % tour.length]); }, 2600);
    }, 1500);
  }
  function wetterZustand(w, jetzt) {
    if (!modell) return;
    var k = [], ev = ((w && w.warnungen) || []).map(function (a) { return (a.ereignis || '').toUpperCase(); }).join(' ');
    var s = sonne(jetzt);
    if (jetzt < s.auf || jetzt > s.unter) k.push('nacht');
    if (w) {
      if (w.zustand === 'snow' || w.zustand === 'sleet' || /SCHNEE/.test(ev)) k.push('w-schnee', 'w-glatt');
      else if ((typeof w.temperatur === 'number' && w.temperatur <= 1) || /GLÄTTE|GLATTEIS|FROST/.test(ev)) k.push('w-glatt');
      if (w.zustand === 'rain' || w.zustand === 'thunderstorm' || w.zustand === 'hail') k.push('w-regen');
      if (w.zustand === 'fog') k.push('w-nebel');
      if ((w.wind || 0) >= 35 || /WIND|STURM|ORKAN|BÖEN/.test(ev)) k.push('w-wind');
    }
    ['w-schnee', 'w-glatt', 'w-regen', 'w-nebel', 'w-wind', 'nacht'].forEach(function (c) { modell.classList.toggle(c, k.indexOf(c) > -1); });
  }

  /* ---------- Karteikarte „Bruchsal heute“: Regeln aus Satzung und Gesetz, Wetter vom DWD ---------- */
  var BESCHREIBUNG = { 'clear-day': 'klar', 'clear-night': 'klar', 'partly-cloudy-day': 'leicht bewölkt', 'partly-cloudy-night': 'leicht bewölkt', cloudy: 'bewölkt', fog: 'Nebel', wind: 'windig', rain: 'Regen', sleet: 'Schneeregen', snow: 'Schnee', hail: 'Hagel', thunderstorm: 'Gewitter' };
  var heuteDa = !!document.querySelector('[data-heute]');
  function setze(k, t) { $$('[data-heute="' + k + '"]').forEach(function (el) { el.textContent = t; }); }
  function regeln(jetzt, w) {
    var b = berlin(jetzt), so = b.wt === 0 || feiertagBW(b), sa = b.wt === 6;
    var bis = so ? '9 Uhr' : sa ? '8 Uhr' : '7 Uhr', name = so && b.wt !== 0 ? 'Feiertag' : WT[b.wt];
    setze('kopf', 'Bruchsal · ' + WT[b.wt] + ', ' + b.t + '. ' + MON[b.m - 1] + ' ' + b.j);
    setze('datum', WT[b.wt].slice(0, 2) + ' ' + zwei(b.t) + '.' + zwei(b.m) + '.');
    setze('zeit', zwei(b.std) + ':' + zwei(b.min) + ' Uhr');
    setze('raeumen', 'Heute (' + name + '): Gehwege geräumt und gestreut bis ' + bis + ', Pflicht endet um 20 Uhr');
    setze('raeumen2', 'heute bis ' + bis + ', bei Schnee und Glätte');
    var heute = Date.UTC(b.j, b.m - 1, b.t);
    var start = b.m >= 11 ? Date.UTC(b.j, 10, 1) : Date.UTC(b.j - 1, 10, 1), ende = b.m >= 11 ? Date.UTC(b.j + 1, 2, 31) : Date.UTC(b.j, 2, 31);
    var laeuft = heute >= start && heute <= ende, tag = Math.round((heute - start) / 864e5) + 1, von = Math.round((ende - start) / 864e5) + 1;
    setze('saison', laeuft ? 'Saison läuft, Tag ' + tag + ' von ' + von + ' (1. November bis 31. März)' : 'Nächste Saison ab 1. November, in ' + Math.round((Date.UTC(b.j, 10, 1) - heute) / 864e5) + ' Tagen');
    setze('saison-kurz', laeuft ? 'Saison läuft · Tag ' + tag : 'Saison ab 1. November');
    var schonzeit = b.m >= 3 && b.m <= 9, frost = w && typeof w.temperatur === 'number' && w.temperatur <= 0;
    setze('hecke', schonzeit ? 'Bis 30. September nur schonender Form- und Pflegeschnitt' : 'Starker Rückschnitt erlaubt bis Ende Februar, an frostfreien Tagen' + (frost ? ' (heute Frost, besser warten)' : ''));
    setze('hecke-kurz', schonzeit ? 'Heckenschnitt heute: nur schonend bis 30. September' : 'Heckenschnitt heute: starker Rückschnitt erlaubt' + (frost ? ', bei Frost warten' : ''));
    var s = sonne(jetzt);
    setze('sonne', 'Aufgang ' + uhrzeit(s.auf) + ', Untergang ' + uhrzeit(s.unter));
    var u = zwei(b.std) + ':' + zwei(b.min), werktag = b.wt >= 1 && b.wt <= 5 && !feiertagBW(b), lang, kurz;
    if (b.std >= 17) { lang = 'Jetzt ' + u + ': Notdienst erreichbar bis 24 Uhr'; kurz = 'Notdienst jetzt erreichbar bis 24 Uhr'; }
    else if (werktag && b.std >= 7) { lang = 'Jetzt ' + u + ': Büro besetzt bis 17 Uhr'; kurz = 'Büro besetzt bis 17 Uhr, danach Notdienst'; }
    else { lang = 'Jetzt ' + u + ': WhatsApp schreiben, ' + (werktag ? 'Rückruf ab 7 Uhr' : 'Notdienst ab 17 Uhr'); kurz = 'Notdienst wieder ab 17 Uhr'; }
    setze('erreichbar', lang); setze('notdienst', kurz);
    setze('jahreswechsel', 'Noch ' + Math.round((Date.UTC(b.j + 1, 0, 1) - heute) / 864e5) + ' Tage bis zum Jahreswechsel: Zählerstände planen');
  }
  function wetter(w) {
    var grad = typeof w.temperatur === 'number' ? String(Math.round(w.temperatur)).replace('-', '−') + ' °C' : '–';
    var text = BESCHREIBUNG[w.icon] || BESCHREIBUNG[w.zustand] || 'keine Angabe';
    var wind = typeof w.wind === 'number' ? ', Wind ' + Math.round(w.wind) + ' km/h' : '';
    setze('grad', grad); setze('grad2', grad);
    setze('wetter', text + wind + (w.station ? ' · DWD-Station ' + w.station : ''));
    setze('wetter2', text + (typeof w.niederschlag === 'number' && w.niederschlag > 0 ? ', ' + w.niederschlag.toFixed(1).replace('.', ',') + ' mm in der letzten Stunde' : ''));
    var warn = (w.warnungen || []).map(function (a) { return a.titel || a.ereignis; }).filter(Boolean);
    var wt = warn.length ? warn.join(' · ') : 'keine amtliche Warnung für Bruchsal';
    setze('warnung', wt); setze('warnung2', wt);
    $$('[data-heute="warnung"],[data-heute="warnung2"]').forEach(function (el) { el.classList.toggle('warn', warn.length > 0); });
    setze('status', 'Live'); setze('quelle', 'DWD'); setze('quelle2', 'DWD');
    var chip = document.getElementById('live-chip');
    if (chip) {
      chip.classList.remove('beispiel');
      chip.textContent = 'Bruchsal jetzt ' + grad + ', ' + text + ' · ';
      if (warn.length) { var bb = document.createElement('b'); bb.textContent = warn[0]; chip.appendChild(bb); chip.appendChild(document.createTextNode(' · ')); }
      chip.appendChild(document.createTextNode('DWD'));
    }
  }
  if (heuteDa || modell) {
    var daten = null;
    var tick = function () { var j = new Date(); if (heuteDa) regeln(j, daten); wetterZustand(daten, j); };
    tick();
    setInterval(tick, 30000);
    if ('fetch' in window) {
      fetch('/wetter.php', { cache: 'no-store' }).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
        .then(function (w) { if (w && !w.fehler) { daten = w; wetter(w); tick(); } })
        .catch(function () { setze('status', 'Wetterdaten gerade nicht erreichbar'); });
    }
  }

  /* ---------- Karteikarten ---------- */
  var tabs = $$('.register [role="tab"]');
  function karte(tab, fokus) {
    tabs.forEach(function (t) {
      var an = t === tab;
      t.setAttribute('aria-selected', an ? 'true' : 'false'); t.tabIndex = an ? 0 : -1;
      var p = document.getElementById(t.getAttribute('aria-controls')); if (p) p.classList.toggle('aktiv', an);
    });
    if (fokus) tab.focus();
    var reg = tab.parentElement;
    if (reg.scrollWidth > reg.clientWidth) reg.scrollTo({ left: Math.max(0, tab.offsetLeft - 24), behavior: ruhig ? 'auto' : 'smooth' });
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { karte(t); });
    t.addEventListener('keydown', function (e) {
      var n = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (n) { e.preventDefault(); karte(tabs[(i + n + tabs.length) % tabs.length], true); }
    });
  });

  /* ---------- Was steht an? Aufgaben antippen, Liste geht fertig in WhatsApp ---------- */
  var liste = document.getElementById('aufgaben');
  if (liste) {
    var chips = document.getElementById('chips'), zahl = document.getElementById('zahl');
    var leiste = $('.mobilleiste'), leisteWa = leiste && $('.btn--wa', leiste);
    if (leisteWa) { var zz = document.createElement('span'); zz.className = 'zahl'; leisteWa.appendChild(zz); }
    var waLinks = [document.getElementById('wa-senden'), leisteWa].filter(Boolean);
    var gewaehlt = [];
    var SAETZE = {
      alles: 'Zehn Leistungen, ein Team, eigenes Personal.',
      hv: 'Ein Ansprechpartner für mehrere Objekte, umlagefähige Positionen getrennt.',
      privat: 'Für alle, die nicht selbst vor Ort sein können oder keine Zeit dafür haben.',
      buero: 'Gereinigt wird, wenn Ihr Betrieb ruht. Nach schriftlichem Plan.',
      gewerbe: 'Ein Vertrag, ein Ansprechpartner, ein fester Meldeweg für Störungen.'
    };
    $$('.aufgabe', liste).forEach(function (b) {
      var w = document.createElement('span'); w.className = 'wisch'; w.setAttribute('aria-hidden', 'true');
      var innen = document.createElement('span'); innen.className = 'wisch__innen';
      Array.prototype.forEach.call(b.children, function (k) { innen.appendChild(k.cloneNode(true)); });
      w.appendChild(innen); b.appendChild(w);
      b.addEventListener('click', function () { umschalten(b); });
    });
    var nachricht = function () {
      var t = 'Hallo Gebäudewerke, ' + (gewaehlt.length ? 'bei uns steht an:\n' + gewaehlt.map(function (x) { return '- ' + x; }).join('\n') + '\nOrt des Objekts: ' : 'ich habe eine Anfrage zu einem Objekt.');
      return 'https://wa.me/491637221790?text=' + encodeURIComponent(t);
    };
    var aktualisieren = function () {
      var n = gewaehlt.length;
      if (zahl) { zahl.textContent = n; zahl.classList.remove('hupf'); void zahl.offsetWidth; zahl.classList.add('hupf'); }
      waLinks.forEach(function (a) { a.href = nachricht(); });
      if (leiste && leisteWa) { leiste.classList.toggle('voll', n > 0); $('.zahl', leiste).textContent = n; $('span', leisteWa).textContent = n ? 'Liste senden' : 'WhatsApp'; }
    };
    var ziel = function () {
      var a = document.getElementById('anfrage');
      if (a && a.offsetParent) { var last = chips.lastElementChild, r = (last || chips).getBoundingClientRect(); return last ? { x: r.right + 6, y: r.top } : { x: r.left, y: r.top }; }
      var r2 = leisteWa ? leisteWa.getBoundingClientRect() : { left: 0, width: 0, top: 0 }; return { x: r2.left + r2.width / 2 - 40, y: r2.top + 10 };
    };
    var fliegen = function (von, text, fertig) {
      if (ruhig || !Element.prototype.animate) { fertig(); return; }
      var f = document.createElement('span'); f.className = 'flieger'; f.textContent = text; f.setAttribute('aria-hidden', 'true'); document.body.appendChild(f);
      var z = ziel();
      var anim = f.animate([{ transform: 'translate(' + von.left + 'px,' + von.top + 'px)' }, { transform: 'translate(' + z.x + 'px,' + z.y + 'px) scale(.85)', opacity: .9 }], { duration: 650, easing: 'cubic-bezier(.5,0,.2,1)' });
      anim.onfinish = function () { f.remove(); fertig(); };
    };
    var umschalten = function (b) {
      var an = b.getAttribute('aria-pressed') !== 'true', text = $('.aufgabe__text', b).textContent;
      b.setAttribute('aria-pressed', an ? 'true' : 'false');
      if (an) {
        gewaehlt.push(text);
        fliegen($('.aufgabe__text', b).getBoundingClientRect(), text, function () {
          var li = document.createElement('li'); li.className = 'chip'; li.textContent = text; li.setAttribute('data-t', text); if (chips) chips.appendChild(li); aktualisieren();
        });
        document.dispatchEvent(new CustomEvent('gw:aufgabe', { detail: { text: text } }));
      } else {
        gewaehlt = gewaehlt.filter(function (x) { return x !== text; });
        var c = chips && chips.querySelector('[data-t="' + text.replace(/"/g, '') + '"]'); if (c) c.remove();
        aktualisieren();
      }
    };
    $$('.fuer button').forEach(function (k) {
      k.addEventListener('click', function () {
        var f = k.getAttribute('data-fuer');
        $$('.fuer button').forEach(function (x) { x.setAttribute('aria-pressed', x === k ? 'true' : 'false'); });
        var satz = document.getElementById('satz'); if (satz) satz.textContent = SAETZE[f] || '';
        var i = 0;
        $$('li', liste).forEach(function (li) {
          var s = (' ' + li.getAttribute('data-fuer') + ' ').indexOf(' ' + f + ' ') > -1;
          li.hidden = !s; li.classList.remove('rein');
          if (s && !ruhig) { void li.offsetWidth; li.style.setProperty('--k', i++); li.classList.add('rein'); }
        });
      });
    });
  }
})();
