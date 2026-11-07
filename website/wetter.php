<?php
/* Gebäudewerke: aktuelles Wetter und amtliche Warnungen für Bruchsal.
   Quelle: Deutscher Wetterdienst, abgerufen über die freie Schnittstelle Bright Sky (api.brightsky.dev).
   Der Server holt die Daten, der Browser der Besucher spricht nur mit gebaeudewerke.de.
   Keine personenbezogenen Daten, Zwischenspeicher 15 Minuten. */
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: public, max-age=600');
header('X-Robots-Tag: noindex');

$basis = getenv("GW_WETTER_BASIS") ?: 'https://api.brightsky.dev';   // nur für lokale Tests änderbar
$lat = 49.1291927;
$lon = 8.5914434;
$speicher = sys_get_temp_dir() . '/gw-wetter-bruchsal.json';

if (is_file($speicher) && time() - filemtime($speicher) < 900 && !getenv('GW_WETTER_BASIS')) {
  readfile($speicher);
  exit;
}

function gw_holen($url) {
  if (function_exists('curl_init')) {
    $c = curl_init($url);
    curl_setopt_array($c, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 4, CURLOPT_CONNECTTIMEOUT => 3, CURLOPT_USERAGENT => 'gebaeudewerke.de']);
    $r = curl_exec($c);
    $ok = $r !== false && curl_getinfo($c, CURLINFO_HTTP_CODE) === 200;
    curl_close($c);
    return $ok ? json_decode($r, true) : null;
  }
  $ctx = stream_context_create(['http' => ['timeout' => 4, 'header' => "User-Agent: gebaeudewerke.de\r\n"]]);
  $r = @file_get_contents($url, false, $ctx);
  return $r ? json_decode($r, true) : null;
}

$q = '?lat=' . $lat . '&lon=' . $lon . '&tz=Europe/Berlin';
$wetter = gw_holen($basis . '/current_weather' . $q);
$warnungen = gw_holen($basis . '/alerts' . $q);

if (!$wetter || empty($wetter['weather'])) {
  if (is_file($speicher)) { readfile($speicher); exit; }   // lieber alte Werte als keine
  echo '{"fehler":"Wetterdaten derzeit nicht verfügbar"}';   // Status 200, die Seite zeigt dann ihre festen Angaben
  exit;
}

$w = $wetter['weather'];
$quelle = $wetter['sources'][0] ?? [];
$aus = [
  'temperatur'   => $w['temperature'] ?? null,
  'zustand'      => $w['condition'] ?? null,
  'icon'         => $w['icon'] ?? null,
  'wind'         => $w['wind_speed_10'] ?? null,
  'niederschlag' => $w['precipitation_60'] ?? null,
  'zeit'         => $w['timestamp'] ?? null,
  'station'      => $quelle['station_name'] ?? null,
  'warnungen'    => [],
  'gebiet'       => $warnungen['location']['name'] ?? null,
  'quelle'       => 'Deutscher Wetterdienst',
];
foreach (($warnungen['alerts'] ?? []) as $a) {
  $aus['warnungen'][] = ['ereignis' => $a['event_de'] ?? '', 'titel' => $a['headline_de'] ?? '', 'stufe' => $a['severity'] ?? ''];
}
$json = json_encode($aus, JSON_UNESCAPED_UNICODE);
if (!getenv('GW_WETTER_BASIS')) @file_put_contents($speicher, $json);   // Testläufe schreiben keinen Zwischenspeicher
echo $json;
