(function () {
  var nav = document.getElementById('hauptnavigation');
  var schleier = document.querySelector('.nav-schleier');
  var oeffnen = document.getElementById('menue-oeffnen');
  var schliessen = document.querySelector('.nav__schliessen');

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
