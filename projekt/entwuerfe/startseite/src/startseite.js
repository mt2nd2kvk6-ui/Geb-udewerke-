/* Gebäudewerke Startseite, Entwurf. Alle Inhalte stehen im HTML, das Skript ergänzt nur Live-Werte und Bewegung. */
(function () {
  'use strict';
  var ruhig = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- Vorschau: Unterseiten gibt es im Entwurf noch nicht ---------- */
  var toast = $('#toast'), toastZeit;
  function melden(t) { if (!toast) return; toast.textContent = t; toast.classList.add('an'); clearTimeout(toastZeit); toastZeit = setTimeout(function () { toast.classList.remove('an'); }, 2600); }
  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var h = a.getAttribute('href');
    if (/^(https?:|mailto:|tel:|#)/.test(h)) return;
    e.preventDefault(); melden('Vorschau: Diese Unterseite baue ich im nächsten Schritt.');
  });
  $$('form').forEach(function (f) { f.addEventListener('submit', function (e) { e.preventDefault(); if (f.reportValidity()) melden('Vorschau: Die Anfrage wird erst auf gebaeudewerke.de versendet.'); }); });

  /* ---------- Menü ---------- */
  var menue = $('#menue'), auf = $('[data-menue-auf]'), zu = $('[data-menue-zu]');
  function menueSetzen(o) {
    if (!menue) return;
    if (o) { menue.hidden = false; requestAnimationFrame(function () { menue.classList.add('offen'); }); if (zu) zu.focus(); }
    else { menue.classList.remove('offen'); setTimeout(function () { menue.hidden = true; }, 300); if (auf) auf.focus(); }
    if (auf) auf.setAttribute('aria-expanded', o ? 'true' : 'false');
    document.body.style.overflow = o ? 'hidden' : '';
  }
  if (auf) auf.addEventListener('click', function () { menueSetzen(true); });
  if (zu) zu.addEventListener('click', function () { menueSetzen(false); });
  if (menue) menue.addEventListener('click', function (e) { if (e.target.closest('a[href^="#"]')) menueSetzen(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && menue && !menue.hidden) menueSetzen(false); });

  /* ---------- Zeit in Bruchsal ---------- */
  var WT = ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'];
  var MON = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'];
  function berlin(d) {
    var t = {};
    new Intl.DateTimeFormat('de-DE', { timeZone: 'Europe/Berlin', year: 'numeric', month: 'numeric', day: 'numeric', hour: 'numeric', minute: 'numeric', hourCycle: 'h23', weekday: 'long' })
      .formatToParts(d).forEach(function (p) { t[p.type] = p.value; });
    return { j: +t.year, m: +t.month, t: +t.day, std: +t.hour, min: +t.minute, wt: WT.indexOf(t.weekday) };
  }
  var zwei = function (n) { return (n < 10 ? '0' : '') + n; };
  function uhrzeit(d) { var b = berlin(d); return zwei(b.std) + ':' + zwei(b.min); }
  function ostern(j) {
    var a = j % 19, b = Math.floor(j / 100), c = j % 100, d = Math.floor(b / 4), e = b % 4, f = Math.floor((b + 8) / 25), g = Math.floor((b - f + 1) / 3),
      h = (19 * a + b - d - g + 15) % 30, i = Math.floor(c / 4), k = c % 4, l = (32 + 2 * e + 2 * i - h - k) % 7, m = Math.floor((a + 11 * h + 22 * l) / 451);
    return new Date(Date.UTC(j, Math.floor((h + l - 7 * m + 114) / 31) - 1, ((h + l - 7 * m + 114) % 31) + 1));
  }
  function feiertagBW(b) {   // gesetzliche Feiertage in Baden-Württemberg
    var fest = ['1.1', '6.1', '1.5', '3.10', '1.11', '25.12', '26.12'];
    if (fest.indexOf(b.t + '.' + b.m) > -1) return true;
    var o = ostern(b.j), heute = Date.UTC(b.j, b.m - 1, b.t);
    return [-2, 1, 39, 50, 60].some(function (x) { return heute === o.getTime() + x * 864e5; });
  }
  function sonne(d, lat, lon) {   // Sonnenauf- und -untergang (vereinfachte NOAA-Formel)
    var r = Math.PI / 180, jd = d.getTime() / 864e5 + 2440587.5, n = Math.ceil(jd - 2451545 + 0.0008), js = n - lon / 360,
      M = (357.5291 + 0.98560028 * js) % 360, C = 1.9148 * Math.sin(M * r) + 0.02 * Math.sin(2 * M * r) + 0.0003 * Math.sin(3 * M * r),
      L = (M + C + 180 + 102.9372) % 360, jt = 2451545 + js + 0.0053 * Math.sin(M * r) - 0.0069 * Math.sin(2 * L * r),
      dek = Math.asin(Math.sin(L * r) * Math.sin(23.4397 * r)),
      w = Math.acos((Math.sin(-0.833 * r) - Math.sin(lat * r) * Math.sin(dek)) / (Math.cos(lat * r) * Math.cos(dek))) / r;
    var ms = function (j) { return new Date((j - 2440587.5) * 864e5); };
    return { auf: ms(jt - w / 360), unter: ms(jt + w / 360) };
  }
  var LAT = 49.1291927, LON = 8.5914434;

  /* ---------- Wetter und Warnungen vom DWD ---------- */
  var BESCHREIBUNG = { 'clear-day': 'klar', 'clear-night': 'klar', 'partly-cloudy-day': 'leicht bewölkt', 'partly-cloudy-night': 'leicht bewölkt', cloudy: 'bewölkt', fog: 'Nebel', wind: 'windig', rain: 'Regen', sleet: 'Schneeregen', snow: 'Schnee', hail: 'Hagel', thunderstorm: 'Gewitter' };
  function holen(url, ms) {
    var c = 'AbortController' in window ? new AbortController() : null;
    var t = setTimeout(function () { if (c) c.abort(); }, ms || 4000);
    return fetch(url, { cache: 'no-store', signal: c ? c.signal : undefined }).then(function (r) { clearTimeout(t); if (!r.ok) throw new Error(r.status); return r.json(); });
  }
  function vonBrightSky() {
    var q = '?lat=' + LAT + '&lon=' + LON + '&tz=Europe/Berlin';
    return Promise.all([holen('https://api.brightsky.dev/current_weather' + q), holen('https://api.brightsky.dev/alerts' + q).catch(function () { return { alerts: [] }; })])
      .then(function (r) {
        var w = r[0].weather || {}, s = (r[0].sources || [])[0] || {};
        return { temperatur: w.temperature, zustand: w.condition, icon: w.icon, wind: w.wind_speed_10, niederschlag: w.precipitation_60, zeit: w.timestamp, station: s.station_name,
          warnungen: (r[1].alerts || []).map(function (a) { return { ereignis: a.event_de, titel: a.headline_de, stufe: a.severity }; }) };
      });
  }
  var BEISPIEL = { beispiel: true, temperatur: 4, zustand: 'dry', icon: 'cloudy', wind: 9, niederschlag: 0, warnungen: [] };
  function wetterLaden() {
    return holen('wetter.php', 3000).catch(vonBrightSky).catch(function () { return BEISPIEL; });
  }

  /* ---------- Modell: Lichtkegel, Hotspots, Liste ---------- */
  var modell = $('#modell');
  var zonen = modell ? $$('.welt .zone', modell) : [];
  var punkte = modell ? $$('.punkt', modell) : [];
  var links10 = $$('.liste10 a');
  var unter = $('#unterzeile');
  var tour = ['keller', 'treppenhaus', 'wohnung', 'reparatur', 'buero', 'hausmeister', 'gewerbe', 'winter', 'metall', 'garten'];
  var ti = 0, pause = false;
  function zeigen(z) {
    if (!modell) return;
    modell.classList.toggle('fokus', !!z);
    var spot = $('.spot', modell); spot.innerHTML = '';
    zonen.forEach(function (g) { if (g.getAttribute('data-zone') === z) spot.appendChild(g.cloneNode(true)); });
    punkte.forEach(function (p) { p.classList.toggle('an', p.getAttribute('data-zone') === z); });
    links10.forEach(function (a) { a.classList.toggle('an', a.getAttribute('data-zone') === z); });
    var p = punkte.filter(function (p) { return p.getAttribute('data-zone') === z; })[0];
    if (p && unter) { $('b', unter).textContent = $('b', p).textContent; $('small', unter).textContent = $('small', p).textContent; }
  }
  if (modell) {
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
    var sichtbar = true;
    if ('IntersectionObserver' in window) new IntersectionObserver(function (e) { sichtbar = e[0].isIntersecting; }).observe(modell);
    if (!ruhig) setTimeout(function () { zeigen(tour[ti++]); setInterval(function () { if (!pause && sichtbar && !document.hidden) zeigen(tour[ti++ % tour.length]); }, 2600); }, 1500);
  }
  function wetterZustand(k) {
    if (!modell) return;
    ['w-schnee', 'w-glatt', 'w-regen', 'w-nebel', 'w-wind', 'nacht'].forEach(function (c) { modell.classList.toggle(c, k.indexOf(c) > -1); });
  }
  function zustandAusDaten(w, jetzt) {
    var k = [], ev = (w.warnungen || []).map(function (a) { return (a.ereignis || '').toUpperCase(); }).join(' ');
    var s = sonne(jetzt, LAT, LON);
    if (jetzt < s.auf || jetzt > s.unter) k.push('nacht');
    if (w.zustand === 'snow' || w.zustand === 'sleet' || /SCHNEE/.test(ev)) k.push('w-schnee', 'w-glatt');
    else if ((typeof w.temperatur === 'number' && w.temperatur <= 1) || /GLÄTTE|GLATTEIS|FROST/.test(ev)) k.push('w-glatt');
    if (w.zustand === 'rain' || w.zustand === 'thunderstorm' || w.zustand === 'hail') k.push('w-regen');
    if (w.zustand === 'fog') k.push('w-nebel');
    if ((w.wind || 0) >= 35 || /WIND|STURM|ORKAN|BÖEN/.test(ev)) k.push('w-wind');
    return k;
  }

  /* ---------- Karteikarten: Bruchsal heute ---------- */
  function setze(k, t) { $$('[data-heute="' + k + '"]').forEach(function (el) { el.textContent = t; }); }
  function saison(b) {
    var heute = Date.UTC(b.j, b.m - 1, b.t);
    var start = b.m >= 11 ? Date.UTC(b.j, 10, 1) : Date.UTC(b.j - 1, 10, 1), ende = b.m >= 11 ? Date.UTC(b.j + 1, 2, 31) : Date.UTC(b.j, 2, 31);
    if (heute >= start && heute <= ende) return { laeuft: true, tag: Math.round((heute - start) / 864e5) + 1, von: Math.round((ende - start) / 864e5) + 1 };
    return { laeuft: false, noch: Math.round((Date.UTC(b.j, 10, 1) - heute) / 864e5) };
  }
  function erreichbar(b) {
    var u = zwei(b.std) + ':' + zwei(b.min), wt = b.wt >= 1 && b.wt <= 5 && !feiertagBW(b);
    if (b.std >= 17) return { kurz: 'Notdienst jetzt erreichbar bis 24 Uhr', lang: 'Jetzt ' + u + ': Notdienst erreichbar bis 24 Uhr' };
    if (wt && b.std >= 7) return { kurz: 'Büro besetzt bis 17 Uhr, danach Notdienst', lang: 'Jetzt ' + u + ': Büro besetzt bis 17 Uhr' };
    return { kurz: 'Notdienst wieder ab 17 Uhr', lang: 'Jetzt ' + u + ': WhatsApp schreiben, ' + (wt ? 'Rückruf ab 7 Uhr' : 'Notdienst ab 17 Uhr') };
  }
  function regelnSetzen(jetzt, w) {
    var b = berlin(jetzt), so = b.wt === 0 || feiertagBW(b), sa = b.wt === 6;
    var bis = so ? '9 Uhr' : sa ? '8 Uhr' : '7 Uhr', tagname = so && b.wt !== 0 ? 'Feiertag' : WT[b.wt];
    setze('kopf', 'Bruchsal · ' + WT[b.wt] + ', ' + b.t + '. ' + MON[b.m - 1] + ' ' + b.j);
    setze('datum', WT[b.wt].slice(0, 2) + ' ' + zwei(b.t) + '.' + zwei(b.m) + '.');
    setze('zeit', zwei(b.std) + ':' + zwei(b.min) + ' Uhr');
    setze('raeumen', 'Heute (' + tagname + '): Gehwege geräumt und gestreut bis ' + bis + ', Pflicht endet um 20 Uhr');
    setze('raeumen2', 'heute bis ' + bis + ', bei Schnee und Glätte');
    var sz = saison(b);
    setze('saison', sz.laeuft ? 'Saison läuft, Tag ' + sz.tag + ' von ' + sz.von + ' (1. November bis 31. März)' : 'Nächste Saison ab 1. November, in ' + sz.noch + ' Tagen');
    setze('saison-kurz', sz.laeuft ? 'Saison läuft · Tag ' + sz.tag : 'Saison ab 1. November');
    var schonzeit = (b.m >= 3 && b.m <= 9);
    var frost = typeof w.temperatur === 'number' && w.temperatur <= 0;
    setze('hecke', schonzeit ? 'Bis 30. September nur schonender Form- und Pflegeschnitt' : 'Starker Rückschnitt erlaubt bis Ende Februar, an frostfreien Tagen' + (frost ? ' (heute Frost, besser warten)' : ''));
    setze('hecke-kurz', schonzeit ? 'Heckenschnitt heute: nur schonend bis 30. September' : 'Heckenschnitt heute: starker Rückschnitt erlaubt' + (frost ? ', bei Frost warten' : ''));
    var s = sonne(jetzt, LAT, LON);
    setze('sonne', 'Aufgang ' + uhrzeit(s.auf) + ', Untergang ' + uhrzeit(s.unter));
    var er = erreichbar(b); setze('erreichbar', er.lang); setze('notdienst', er.kurz);
    var nj = Math.round((Date.UTC(b.j + 1, 0, 1) - Date.UTC(b.j, b.m - 1, b.t)) / 864e5);
    setze('jahreswechsel', 'Noch ' + nj + ' Tage bis zum Jahreswechsel: Zählerstände planen');
  }
  function wetterSetzen(w) {
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
    setze('status', w.beispiel ? 'Beispielwerte in der Vorschau' : 'Live');
    setze('quelle', w.beispiel ? 'Beispiel' : 'DWD'); setze('quelle2', w.beispiel ? 'Beispiel' : 'DWD');
    $$('[data-heute="quelle"],[data-heute="quelle2"],[data-heute="status"]').forEach(function (el) { el.classList.toggle('beispiel', !!w.beispiel); });
    var chip = $('#live-chip');
    if (chip) {
      chip.classList.toggle('beispiel', !!w.beispiel);
      chip.innerHTML = w.beispiel ? 'Bruchsal · Wetter live auf gebaeudewerke.de' : 'Bruchsal jetzt ' + grad + ', ' + text + (warn.length ? ' · <b>' + warn[0] + '</b>' : '') + ' · DWD';
    }
  }
  var daten = BEISPIEL;
  function alles() { var j = new Date(); regelnSetzen(j, daten); if (!testModus) wetterZustand(zustandAusDaten(daten, j)); }
  var testModus = false;
  wetterLaden().then(function (w) { daten = w; wetterSetzen(w); alles(); });
  regelnSetzen(new Date(), daten);
  setInterval(alles, 30000);
  $$('.wettertest button').forEach(function (k) {
    k.addEventListener('click', function () {
      $$('.wettertest button').forEach(function (x) { x.setAttribute('aria-pressed', x === k ? 'true' : 'false'); });
      var t = k.getAttribute('data-test');
      testModus = t !== 'live';
      wetterZustand(t === 'schnee' ? ['w-schnee', 'w-glatt'] : t === 'regen' ? ['w-regen'] : t === 'nacht' ? ['nacht'] : t === 'sturm' ? ['w-wind', 'w-regen', 'nacht'] : zustandAusDaten(daten, new Date()));
    });
  });

  /* ---------- Karteikarten: Register ---------- */
  var tabs = $$('.register [role="tab"]');
  function karte(tab, fokus) {
    tabs.forEach(function (t) {
      var an = t === tab;
      t.setAttribute('aria-selected', an ? 'true' : 'false'); t.tabIndex = an ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).classList.toggle('aktiv', an);
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

  /* ---------- Was steht an? ---------- */
  var liste = $('#aufgaben'), chips = $('#chips'), zahl = $('#zahl');
  var leiste = $('.mobilleiste'), leisteWa = leiste && $('.btn--wa', leiste);
  if (leisteWa) { var zz = document.createElement('span'); zz.className = 'zahl'; leisteWa.appendChild(zz); }
  var waLinks = [$('#wa-senden'), leisteWa, $('.kopf__wa')].filter(Boolean);
  var gewaehlt = [];
  var SAETZE = {
    alles: 'Zehn Leistungen, ein Team, eigenes Personal.',
    hv: 'Ein Ansprechpartner für mehrere Objekte, umlagefähige Positionen getrennt.',
    privat: 'Für alle, die nicht selbst vor Ort sein können oder keine Zeit dafür haben.',
    buero: 'Gereinigt wird, wenn Ihr Betrieb ruht. Nach schriftlichem Plan.',
    gewerbe: 'Ein Vertrag, ein Ansprechpartner, ein fester Meldeweg für Störungen.'
  };
  if (liste) {
    $$('.aufgabe', liste).forEach(function (b) {
      var w = document.createElement('span'); w.className = 'wisch'; w.setAttribute('aria-hidden', 'true');
      var innen = document.createElement('span'); innen.className = 'wisch__innen';
      Array.prototype.forEach.call(b.children, function (k) { innen.appendChild(k.cloneNode(true)); });
      w.appendChild(innen); b.appendChild(w);
      b.addEventListener('click', function () { umschalten(b); });
    });
  }
  function nachricht() {
    var t = 'Hallo Gebäudewerke, ' + (gewaehlt.length ? 'bei uns steht an:\n' + gewaehlt.map(function (x) { return '- ' + x; }).join('\n') + '\nOrt des Objekts: ' : 'ich habe eine Anfrage zu einem Objekt.');
    return 'https://wa.me/491637221790?text=' + encodeURIComponent(t);
  }
  function aktualisieren() {
    var n = gewaehlt.length;
    if (zahl) { zahl.textContent = n; zahl.classList.remove('hupf'); void zahl.offsetWidth; zahl.classList.add('hupf'); }
    waLinks.forEach(function (a) { a.href = nachricht(); });
    if (leiste) { leiste.classList.toggle('voll', n > 0); $('.zahl', leiste).textContent = n; $('span', leisteWa).textContent = n ? 'Liste senden' : 'WhatsApp'; }
  }
  function ziel() {
    var a = $('#anfrage');
    if (a && a.offsetParent) { var last = chips.lastElementChild, r = (last || chips).getBoundingClientRect(); return last ? { x: r.right + 6, y: r.top } : { x: r.left, y: r.top }; }
    var r2 = leisteWa.getBoundingClientRect(); return { x: r2.left + r2.width / 2 - 40, y: r2.top + 10 };
  }
  function fliegen(von, text, fertig) {
    if (ruhig || !Element.prototype.animate) { fertig(); return; }
    var f = document.createElement('span'); f.className = 'flieger'; f.textContent = text; document.body.appendChild(f);
    var z = ziel();
    var anim = f.animate([{ transform: 'translate(' + von.left + 'px,' + von.top + 'px)' }, { transform: 'translate(' + z.x + 'px,' + z.y + 'px) scale(.85)', opacity: .9 }], { duration: 650, easing: 'cubic-bezier(.5,0,.2,1)' });
    anim.onfinish = function () { f.remove(); fertig(); };
  }
  function umschalten(b) {
    var an = b.getAttribute('aria-pressed') !== 'true', text = $('.aufgabe__text', b).textContent;
    b.setAttribute('aria-pressed', an ? 'true' : 'false');
    if (an) {
      gewaehlt.push(text);
      fliegen($('.aufgabe__text', b).getBoundingClientRect(), text, function () {
        var li = document.createElement('li'); li.className = 'chip'; li.textContent = text; li.setAttribute('data-t', text); chips.appendChild(li); aktualisieren();
      });
    } else {
      gewaehlt = gewaehlt.filter(function (x) { return x !== text; });
      var c = chips.querySelector('[data-t="' + text + '"]'); if (c) c.remove();
      aktualisieren();
    }
  }
  $$('.fuer button').forEach(function (k) {
    k.addEventListener('click', function () {
      var f = k.getAttribute('data-fuer');
      $$('.fuer button').forEach(function (x) { x.setAttribute('aria-pressed', x === k ? 'true' : 'false'); });
      $('#satz').textContent = SAETZE[f];
      var i = 0;
      $$('li', liste).forEach(function (li) {
        var s = (' ' + li.getAttribute('data-fuer') + ' ').indexOf(' ' + f + ' ') > -1;
        li.hidden = !s; li.classList.remove('rein');
        if (s && !ruhig) { void li.offsetWidth; li.style.setProperty('--k', i++); li.classList.add('rein'); }
      });
    });
  });

  /* ---------- Bewertungen: Laufband ---------- */
  $$('[data-laufband]').forEach(function (band) {
    var gruppe = $('.laufband__gruppe', band), knopf = band.parentElement.querySelector('.laufband__knopf');
    if (ruhig || !gruppe) return;
    var kopie = gruppe.cloneNode(true); kopie.setAttribute('aria-hidden', 'true');   // Kopie nur für die Endlosschleife, nicht im HTML
    $$('[role="img"]', kopie).forEach(function (e) { e.removeAttribute('role'); e.removeAttribute('aria-label'); });
    gruppe.parentNode.appendChild(kopie);
    band.classList.add('laufband--laeuft');
    band.style.setProperty('--dauer', Math.max(40, gruppe.scrollWidth / 30) + 's');
    if (knopf) {
      knopf.hidden = false;
      knopf.addEventListener('click', function () { var p = band.classList.toggle('laufband--pause'); $('span', knopf).textContent = p ? 'Laufband fortsetzen' : 'Laufband anhalten'; });
    }
  });

  /* ---------- Ablauf: Linie zeichnet sich beim Hineinscrollen ---------- */
  var ab = $('#ablauf-liste');
  if (ab && 'IntersectionObserver' in window) new IntersectionObserver(function (e, o) { if (e[0].isIntersecting) { ab.classList.add('sichtbar'); o.disconnect(); } }, { threshold: .4 }).observe(ab);
  else if (ab) ab.classList.add('sichtbar');

  /* ---------- Zwei-Klick-Karte ---------- */
  $$('[data-karte-laden]').forEach(function (k) {
    k.addEventListener('click', function () { melden('Vorschau: Google Maps lädt erst auf gebaeudewerke.de, nach Ihrem Klick.'); });
  });
})();
