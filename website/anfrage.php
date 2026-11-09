<?php
/* Gebäudewerke: Versand des Kontaktformulars an info@gebaeudewerke.de */
declare(strict_types=1);
if (function_exists('mb_internal_encoding')) { mb_internal_encoding('UTF-8'); }
date_default_timezone_set('Europe/Berlin');

const EMPFAENGER = 'info@gebaeudewerke.de';
const ABSENDER   = 'info@gebaeudewerke.de';

function kuerzen(string $v, int $max): string {
    return function_exists('mb_substr') ? mb_substr($v, 0, $max) : substr($v, 0, $max);
}
function kodiert(string $v): string { return '=?UTF-8?B?' . base64_encode($v) . '?='; }
function weiter(string $ziel): void { header('Location: ' . $ziel, true, 303); exit; }
function feld(string $k, int $max = 2000): string {
    $v = (isset($_POST[$k]) && is_string($_POST[$k])) ? trim($_POST[$k]) : '';
    return kuerzen($v, $max);
}
function zeile(string $v): string { return trim(preg_replace('/[\r\n\t]+/', ' ', $v) ?? ''); }

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') { weiter('kontakt.html'); }
if (feld('webseite') !== '') { weiter('danke.html'); }   // Spamschutz: verstecktes Feld

$name      = zeile(feld('name', 120));
$firma     = zeile(feld('firma', 160));
$email     = zeile(feld('email', 200));
$telefon   = zeile(feld('telefon', 60));
$ort       = zeile(feld('ort', 160));
$art       = zeile(feld('objektart', 80));
$groesse   = zeile(feld('groesse', 80));
$seite     = zeile(feld('seite', 40));
$nachricht = feld('nachricht', 5000);
$ds        = isset($_POST['datenschutz']);
$leistungen = [];
if (isset($_POST['leistungen']) && is_array($_POST['leistungen'])) {
    foreach ($_POST['leistungen'] as $l) { if (is_string($l)) { $leistungen[] = zeile(kuerzen($l, 80)); } }
}

if ($name === '' || $nachricht === '' || !$ds || filter_var($email, FILTER_VALIDATE_EMAIL) === false) {
    weiter('anfrage-fehler.html');
}

$leer = fn(string $v): string => $v === '' ? '-' : $v;
$text  = "Neue Anfrage über gebaeudewerke.de\n\n";
$text .= "Name: {$name}\nFirma: {$leer($firma)}\nE-Mail: {$email}\nTelefon: {$leer($telefon)}\n";
$text .= "Ort des Objekts: {$leer($ort)}\nObjektart: {$leer($art)}\nGröße oder Einheiten: {$leer($groesse)}\n";
$text .= "Leistungen: " . ($leistungen ? implode(', ', $leistungen) : '-') . "\n";
$text .= "Gesendet über: {$leer($seite)}\nZeitpunkt: " . date('d.m.Y H:i') . " Uhr\n\nNachricht:\n{$nachricht}\n";

$betreff = kodiert('Neue Anfrage über die Website: ' . $name);
$header = [
    'From'                      => kodiert('Website Gebäudewerke') . ' <' . ABSENDER . '>',
    'Reply-To'                  => $email,
    'MIME-Version'              => '1.0',
    'Content-Type'              => 'text/plain; charset=UTF-8',
    'Content-Transfer-Encoding' => '8bit',
];

$ok = mail(EMPFAENGER, $betreff, $text, $header, '-f' . ABSENDER);
weiter($ok ? 'danke.html' : 'anfrage-fehler.html');
