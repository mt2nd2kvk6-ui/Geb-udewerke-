<?php
/* Lokaler Testserver, bildet die Regeln aus website/htaccess.txt nach.
   Start (im Projektordner):  php -S 127.0.0.1:8080 -t website werkzeuge/dev_router.php
   HTML wird wie mit mod_deflate auf dem Server komprimiert ausgeliefert. */
$web = realpath(__DIR__ . '/../website');
$pfad = rawurldecode(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH));
chdir($web);
function gw_dev_gzip() {
  if (strpos($_SERVER['HTTP_ACCEPT_ENCODING'] ?? '', 'gzip') !== false) ob_start('ob_gzhandler');
}
if ($pfad === '/' || (preg_match('~^/((?:ratgeber/)?[a-z0-9-]+\.html|llms\.txt)$~', $pfad) && $pfad !== '/404.html' && is_file($web . $pfad))) {
  gw_dev_gzip();
  require $web . '/auslieferung.php';
  return true;
}
if ($pfad === '/ratgeber/' || $pfad === '/ratgeber') {
  gw_dev_gzip();
  $_SERVER['SCRIPT_FILENAME'] = $web . '/ratgeber/index.php';
  require $web . '/ratgeber/index.php';
  return true;
}
if (substr($pfad, -4) === '.php' && is_file($web . $pfad)) {
  $_SERVER['SCRIPT_FILENAME'] = $web . $pfad;
  require $web . $pfad;
  return true;
}
if (is_file($web . $pfad)) return false;
gw_dev_gzip();
http_response_code(404);
header('Content-Type: text/html; charset=utf-8');
readfile($web . '/404.html');
return true;
