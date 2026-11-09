<?php
/* Gebäudewerke: Selbsteinrichtung nach dem Entpacken.
   Legt die Serverregeln (.htaccess) aus htaccess.txt an, falls sie noch fehlen.
   Wird automatisch beim ersten Seitenaufruf ausgeführt (assets/js/consent.js),
   zusätzlich von ratgeber/index.php und ratgeber/sitemap.php. Schreibt nur den
   festen Inhalt aus htaccess.txt, sonst nichts. */
if (!function_exists('gw_einrichten')) {
  function gw_einrichten() {
    $ziel = __DIR__ . '/.htaccess';
    $quelle = __DIR__ . '/htaccess.txt';
    if (!is_file($ziel) && is_file($quelle)) {
      @copy($quelle, $ziel);
    }
  }
}
gw_einrichten();
if (realpath($_SERVER['SCRIPT_FILENAME'] ?? '') === __FILE__) {
  header('Cache-Control: no-store');
  header('X-Robots-Tag: noindex');
  http_response_code(204);
}
