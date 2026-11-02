<?php
/* Gebäudewerke Installer, Stand 29.10.2026 (b, mit Conversions)
   Entpackt die angehängte Website in diesen Ordner, legt die .htaccess an,
   entfernt alte JPG-Fotos, für die es eine WebP-Version gibt, und löscht sich danach selbst. */
@set_time_limit(300);
header('Content-Type: text/html; charset=utf-8');
header('Cache-Control: no-store');
header('X-Robots-Tag: noindex');
$ziel = __DIR__;
$meldungen = []; $fehler = [];

$daten = (string) file_get_contents(__FILE__, false, null, __COMPILER_HALT_OFFSET__);
$daten = base64_decode(preg_replace('/\s+/', '', $daten), true);
if ($daten === false || substr($daten, 0, 2) !== 'PK') { $fehler[] = 'Das Website-Paket in dieser Datei ist beschädigt. Bitte die Datei erneut hochladen.'; }

$anzahl = 0;
if (!$fehler) {
  $tmp = $ziel . '/gw-paket-' . bin2hex(random_bytes(4)) . '.zip';
  file_put_contents($tmp, $daten);
  if (class_exists('ZipArchive')) {
    $zip = new ZipArchive();
    if ($zip->open($tmp) === true) {
      for ($i = 0; $i < $zip->numFiles; $i++) {
        $name = $zip->getNameIndex($i);
        if ($name === false || strpos($name, '..') !== false || $name[0] === '/' || substr($name, -1) === '/') continue;
        $datei = $ziel . '/' . $name;
        if (!is_dir(dirname($datei)) && !@mkdir(dirname($datei), 0755, true)) { $fehler[] = 'Ordner konnte nicht angelegt werden: ' . dirname($name); continue; }
        $inhalt = $zip->getFromIndex($i);
        if ($inhalt === false || @file_put_contents($datei, $inhalt) === false) { $fehler[] = 'Datei konnte nicht geschrieben werden: ' . $name; continue; }
        @chmod($datei, 0644);
        $anzahl++;
      }
      $zip->close();
    } else { $fehler[] = 'Das Paket konnte nicht geöffnet werden.'; }
  } else {
    try { $p = new PharData($tmp); $p->extractTo($ziel, null, true); $anzahl = iterator_count(new RecursiveIteratorIterator($p)); }
    catch (Exception $e) { $fehler[] = 'Entpacken nicht möglich: ' . $e->getMessage(); }
  }
  @unlink($tmp);
}

if (!$fehler) {
  $meldungen[] = $anzahl . ' Dateien entpackt.';
  if (is_file($ziel . '/htaccess.txt') && @copy($ziel . '/htaccess.txt', $ziel . '/.htaccess')) $meldungen[] = 'Serverregeln (.htaccess) eingerichtet.';
  else $fehler[] = 'Die .htaccess konnte nicht angelegt werden.';
  $weg = 0;
  foreach (glob($ziel . '/assets/img/fotos/*.jpg') ?: [] as $jpg) {
    if (is_file(substr($jpg, 0, -4) . '.webp') && @unlink($jpg)) $weg++;
  }
  if ($weg) $meldungen[] = $weg . ' alte JPG-Fotos entfernt (WebP-Versionen sind vorhanden).';
  if (@unlink(__FILE__)) $meldungen[] = 'Installer hat sich selbst gelöscht.';
  else $fehler[] = 'Der Installer konnte sich nicht selbst löschen. Bitte diese Datei im Webspace Explorer löschen.';
}
$ok = !$fehler;
?><!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex"><title>Gebäudewerke Installation</title>
<style>body{font-family:system-ui,Arial,sans-serif;margin:0;background:#EEF1F4;color:#262F35}main{max-width:560px;margin:8vh auto;background:#fff;padding:28px 24px;border-top:6px solid #0D2B4F}h1{color:#0D2B4F;font-size:1.5rem;margin:0 0 1rem}li{margin:.4rem 0}.fehler{color:#9B1C1C}a{display:inline-block;margin-top:1rem;background:#0D2B4F;color:#fff;padding:.8rem 1.2rem;border-radius:6px;text-decoration:none;font-weight:700}</style></head>
<body><main><h1><?= $ok ? 'Fertig: Website ist installiert' : 'Installation nicht vollständig' ?></h1><ul>
<?php foreach ($meldungen as $m): ?><li><?= htmlspecialchars($m) ?></li><?php endforeach; ?>
<?php foreach ($fehler as $m): ?><li class="fehler"><?= htmlspecialchars($m) ?></li><?php endforeach; ?>
</ul><?php if ($ok): ?><a href="/">Zur Website</a><?php endif; ?></main></body></html>
<?php exit; __HALT_COMPILER();
