<?php
require_once dirname(__DIR__) . '/einrichtung.php';
/* Gebäudewerke Ratgeber: Sitemap aller Beiträge, wird automatisch erzeugt. */
date_default_timezone_set('Europe/Berlin');
header('Content-Type: application/xml; charset=utf-8');
echo '<?xml version="1.0" encoding="UTF-8"?>' . "\n";
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' . "\n";
foreach (glob(__DIR__ . '/*.html') as $d) {
  $n = basename($d);
  if ($n[0] === '_') continue;
  $s = file_get_contents($d, false, null, 0, 20000);
  if (!preg_match('/<meta\s+name="artikel-datum"\s+content="(\d{4}-\d{2}-\d{2})"/', $s, $m)) continue;
  if ($m[1] > date('Y-m-d')) continue;   // geplante Beiträge erst ab ihrem Datum melden
  $l = preg_match('/<meta\s+name="artikel-aktualisiert"\s+content="(\d{4}-\d{2}-\d{2})"/', $s, $m2) ? $m2[1] : $m[1];
  echo '  <url><loc>https://gebaeudewerke.de/ratgeber/' . htmlspecialchars($n) . '</loc><lastmod>' . $l . '</lastmod></url>' . "\n";
}
echo '</urlset>' . "\n";
