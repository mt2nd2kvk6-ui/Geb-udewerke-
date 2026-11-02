<?php
/* Gebäudewerke: liefert die statischen Seiten aus.
   Ratgeberbeiträge mit einem Datum in der Zukunft (ratgeber/plan.json) antworten mit 404.
   Links auf diese Beiträge werden bis zum Veröffentlichungstag aus allen Seiten entfernt.
   Neue Beiträge einfach hochladen: das Datum steht im Beitrag (meta artikel-datum).
   ratgeber/plan.json wird automatisch neu erzeugt, sobald ein Beitrag neuer ist. */
date_default_timezone_set('Europe/Berlin');
$gw_basis = __DIR__;

function gw_404($basis) {
  http_response_code(404);
  header('Content-Type: text/html; charset=utf-8');
  header('X-Robots-Tag: noindex');
  readfile($basis . '/404.html');
  exit;
}

$gw_pfad = rawurldecode((string) parse_url($_SERVER['REQUEST_URI'] ?? '/', PHP_URL_PATH));
if ($gw_pfad === '/auslieferung.php') { header('Location: https://gebaeudewerke.de/', true, 301); exit; }
$gw_datei = ($gw_pfad === '/' || $gw_pfad === '') ? 'index.html' : ltrim($gw_pfad, '/');
if (!preg_match('~^(?:(?:ratgeber/)?[a-z0-9-]+\.html|llms\.txt)$~', $gw_datei) || !is_file($gw_basis . '/' . $gw_datei)) {
  gw_404($gw_basis);
}

$gw_heute = date('Y-m-d');
$gw_planpfad = $gw_basis . '/ratgeber/plan.json';
$gw_beitraege = glob($gw_basis . '/ratgeber/*.html') ?: [];
$gw_neuester = 0;
foreach ($gw_beitraege as $gw_b) { $gw_neuester = max($gw_neuester, (int) @filemtime($gw_b)); }
$gw_plan = null;
if (is_file($gw_planpfad) && filemtime($gw_planpfad) >= $gw_neuester) {
  $gw_plan = json_decode((string) @file_get_contents($gw_planpfad), true);
}
if (!is_array($gw_plan)) {
  $gw_plan = [];
  foreach ($gw_beitraege as $gw_b) {
    $gw_n = basename($gw_b, '.html');
    if ($gw_n === '' || $gw_n[0] === '_') continue;
    $gw_k = (string) @file_get_contents($gw_b, false, null, 0, 20000);
    if (preg_match('/<meta name="artikel-datum" content="(\d{4}-\d{2}-\d{2})"/', $gw_k, $gw_t)) $gw_plan[$gw_n] = $gw_t[1];
  }
  ksort($gw_plan);
  @file_put_contents($gw_planpfad, json_encode($gw_plan, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES), LOCK_EX);
}
$gw_geplant = [];
if (is_array($gw_plan)) {
  foreach ($gw_plan as $gw_slug => $gw_datum) {
    if (is_string($gw_datum) && $gw_datum > $gw_heute) $gw_geplant[] = $gw_slug;
  }
}
if (preg_match('~^ratgeber/([a-z0-9-]+)\.html$~', $gw_datei, $gw_m) && in_array($gw_m[1], $gw_geplant, true)) {
  gw_404($gw_basis);
}

$gw_inhalt = file_get_contents($gw_basis . '/' . $gw_datei);
if ($gw_geplant) {
  $gw_muster = implode('|', array_map(function ($s) { return preg_quote($s, '~'); }, $gw_geplant));
  if ($gw_datei === 'llms.txt') {
    $gw_inhalt = preg_replace('~^[^\n]*gebaeudewerke\.de/ratgeber/(?:' . $gw_muster . ')\.html[^\n]*\n?~m', '', $gw_inhalt);
  } else {
    $gw_href = 'href="(?:https://gebaeudewerke\.de)?/?ratgeber/(?:' . $gw_muster . ')\.html"';
    $gw_inhalt = preg_replace('~<li><a\b[^>]*\s' . $gw_href . '[^>]*>.*?</a></li>~s', '', $gw_inhalt);
    $gw_inhalt = preg_replace('~<p><a\b[^>]*\s' . $gw_href . '[^>]*>.*?</a></p>~s', '', $gw_inhalt);
    $gw_inhalt = preg_replace('~<a\b[^>]*\s' . $gw_href . '[^>]*>(.*?)</a>~s', '$1', $gw_inhalt);
    $gw_leer = '<li><a href="/ratgeber/">Zur Ratgeber-Übersicht</a></li>';
    $gw_inhalt = str_replace(['<ul class="weitere"></ul>', '<ul></ul>'], ['<ul class="weitere">' . $gw_leer . '</ul>', '<ul>' . $gw_leer . '</ul>'], $gw_inhalt);
  }
}

header('Content-Type: ' . ($gw_datei === 'llms.txt' ? 'text/plain' : 'text/html') . '; charset=utf-8');
header('Cache-Control: no-cache');
echo $gw_inhalt;
