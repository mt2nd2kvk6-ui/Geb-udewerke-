# Relaunch 12/2026: Prüfbericht

Stand 25.11.2026 nach den Entscheidungen des Inhabers (Runde 2), Branch `claude/relaunch-2026-12`. Gemessen lokal mit `werkzeuge/dev_router.php` (bildet `htaccess.txt` nach). „Vorher“ = Live-Stand 16.11.2026 (0638e7d).

## Ergebnis

| Prüfung | Ergebnis |
|---|---|
| `werkzeuge/seo_pruefen.py` | 0 Befunde |
| `werkzeuge/links_pruefen.py` (Hauptkeyword-Anker zeigen nur auf ihre Seite) | 0 Befunde, 0 Ankertexte mit mehreren Zielen |
| `werkzeuge/preise_pruefen.py` (jeder Eurobetrag gegen preise.html) | 0 Befunde, 253 Beträge, kein Altwert |
| `layout_anwenden.py` zweiter Lauf | 0 Änderungen |
| 46 URLs: Status 200, Canonical wie am 16.11. | 46 von 46, 0 Abweichungen, auch mit UTM-Parametern |
| `auslieferung.php` heute und 60 Tage | 61 Tage, 0 Befunde. Die vier geplanten Beiträge liefern bis zu ihrem Datum 404 und erscheinen am 27.11., 01.12., 08.12. und 15.12.; vorher kein Link, Sitemap- oder llms.txt-Eintrag. Keine Seite verliert Inhalt. |
| Bedientest | 37 von 37 bestanden |
| Browser-Anfragen an fremde Server | keine (49 Seiten), Google erst nach Zustimmung |
| Suche „130 € netto“, „190 € netto“, „280 € netto“ in `website/` | 0 Treffer |
| Suche „0176 74025524“ in `website/` | nur `impressum.html` (Anrufnummer des Inhabers, Entscheidung 25.11.) |
| `[PRÜFEN]` in `website/` | 0 |

## Lighthouse mobil

| Seite | Performance | Barrierefreiheit | Best Practices | SEO | LCP | TBT | CLS |
|---|---|---|---|---|---|---|---|
| / | 99 → **97** | 100 → 100 | 100 → 100 | 100 → 100 | 2.1 s → 2.2 s | 70 ms → 130 ms | 0 → 0 |
| /hausmeisterservice.html | 98 → **99** | 100 → 100 | 100 → 100 | 100 → 100 | 2.5 s → 2.3 s | 50 ms → 0 ms | 0 → 0 |
| /kontakt.html | 100 → **99** | 100 → 100 | 100 → 100 | 100 → 100 | 1.8 s → 2.0 s | 40 ms → 0 ms | 0 → 0 |
| /winterdienst.html | 99 → **98** | 100 → 100 | 100 → 100 | 100 → 100 | 2.0 s → 2.3 s | 30 ms → 0 ms | 0 → 0 |
| /ratgeber/ | 96 → **96** | 100 → 100 | 100 → 100 | 100 → 100 | 2.7 s → 2.8 s | 0 ms → 0 ms | 0 → 0 |
| /ratgeber/raeum-und-streupflicht-bruchsal.html | 99 → **98** | 100 → 100 | 100 → 100 | 100 → 100 | 2.0 s → 2.4 s | 20 ms → 0 ms | 0 → 0 |

Ziel 95/100/100/100 erreicht. Nicht erreicht: LCP unter 1,8 s (auch vorher nicht). Auf der Startseite ist das LCP-Element der Cookie-Hinweis, auf den Unterseiten die H1; lokal ohne gzip und Cache für JavaScript gemessen, auf IONOS übernimmt das `htaccess.txt`.

## Seiten: Title, Description, Wortzahl

| Seite | Title px | Description px | Wörter vorher → nachher | Anteil |
|---|---|---|---|---|
| / | 503 | 965 | 2330 → 3247 | 139 % |
| /bueroreinigung.html | 500 | 902 | 1134 → 1183 | 104 % |
| /einsatzgebiet.html | 426 | 897 | 1168 → 1252 | 107 % |
| /entruempelung.html | 531 | 902 | 1895 → 1939 | 102 % |
| /gartenpflege.html | 526 | 917 | 1519 → 1570 | 103 % |
| /gebaeudereinigung.html | 566 | 916 | 1856 → 1911 | 103 % |
| /hausmeisterservice.html | 509 | 934 | 2159 → 2218 | 103 % |
| /karriere.html | 504 | 912 | 378 → 400 | 106 % |
| /kleinreparaturen.html | 541 | 942 | 1310 → 1365 | 104 % |
| /kontakt.html | 526 | 896 | 971 → 971 | 100 % |
| /metallarbeiten-schloesser.html | 490 | 960 | 1285 → 1326 | 103 % |
| /preise.html | 523 | 968 | 1053 → 1070 | 102 % |
| /treppenhausreinigung.html | 569 → 540 | 983 | 1253 → 1297 | 104 % |
| /ueber-uns.html | 497 | 872 | 792 → 809 | 102 % |
| /winterdienst.html | 525 → 569 | 907 → 944 | 1736 → 1777 | 102 % |
| /wohnungsuebergabe.html | 569 | 915 | 1503 → 1541 | 103 % |
| /ratgeber/bauendreinigung-bruchsal.html | 517 | 924 | 522 → 533 | 102 % |
| /ratgeber/besichtigung-vorbereiten-vermietung.html | 422 | 888 | 495 → 505 | 102 % |
| /ratgeber/bueroreinigung-praxisreinigung-bruchsal.html | 410 | 945 | 583 → 594 | 102 % |
| /ratgeber/dienstleister-wechseln-hausmeister.html | 403 | 911 | – → 404 bis Erscheinen | geplant |
| /ratgeber/entruempelung-ablauf-bruchsal.html | 439 | 962 | 557 → 563 | 101 % |
| /ratgeber/gartenpflege-jahresvertrag-bruchsal.html | 472 | 990 | 584 → 590 | 101 % |
| /ratgeber/glasreinigung-bruchsal.html | 474 | 982 | 567 → 573 | 101 % |
| /ratgeber/grundreinigung-gewerbeboden-bruchsal.html | 520 | 922 | 521 → 534 | 102 % |
| /ratgeber/handwerkerkoordination-bruchsal.html | 492 | 948 | 496 → 502 | 101 % |
| /ratgeber/hausmeisterkosten-umlagefaehig.html | 517 | 939 | 612 → 618 | 101 % |
| /ratgeber/hausmeisterservice-hausverwaltung-bruchsal.html | 426 | 985 | 488 → 494 | 101 % |
| /ratgeber/hausmeisterservice-weg-bruchsal.html | 514 | 966 | – → 404 bis Erscheinen | geplant |
| /ratgeber/hecke-schneiden-erlaubt.html | 362 | 934 | 641 → 620 | 97 % |
| /ratgeber/ | 564 | 852 | 1009 → 1056 | 105 % |
| /ratgeber/kleinreparaturen-bruchsal.html | 496 | 910 | 528 → 544 | 103 % |
| /ratgeber/kosten-hausmeisterservice-bruchsal.html | 435 | 943 | – → 404 bis Erscheinen | geplant |
| /ratgeber/laub-gehweg-pflicht-bruchsal.html | 443 | 940 | 617 → 623 | 101 % |
| /ratgeber/muelltonnendienst-bruchsal.html | 442 | 938 | 626 → 632 | 101 % |
| /ratgeber/ortstermin-angebot-hausmeisterservice.html | 391 | 891 | 499 → 505 | 101 % |
| /ratgeber/raeum-und-streupflicht-bruchsal.html | 490 | 923 | 911 → 917 | 101 % |
| /ratgeber/schluesselverwaltung-bruchsal.html | 422 | 925 | 640 → 646 | 101 % |
| /ratgeber/stoerungsmeldung-gewerbeobjekt-bruchsal.html | 380 | 981 | 635 → 653 | 103 % |
| /ratgeber/streugut-entfernen-fruehjahr.html | 373 | 981 | 566 → 572 | 101 % |
| /ratgeber/streuprotokoll-winterdienst-bruchsal.html | 430 | 973 | 828 → 834 | 101 % |
| /ratgeber/sturmschaden-kontrolle-gebaeude.html | 365 | 925 | 523 → 531 | 102 % |
| /ratgeber/tiefgarage-keller-reinigung-bruchsal.html | 469 | 928 | 664 → 675 | 102 % |
| /ratgeber/treppenhaus-rettungsweg.html | 473 | 937 | – → 404 bis Erscheinen | geplant |
| /ratgeber/treppenhausreinigung-bruchsal.html | 377 | 963 | 561 → 567 | 101 % |
| /ratgeber/unkraut-pflaster-entfernen-bruchsal.html | 469 | 949 | 606 → 612 | 101 % |
| /ratgeber/winterdienst-beauftragen-bruchsal.html | 413 | 941 | 751 → 757 | 101 % |
| /ratgeber/wohnungsuebergabe-protokoll-bruchsal.html | 456 | 966 | 676 → 687 | 102 % |
| /ratgeber/zaehlerstaende-ablesen-jahreswechsel.html | 424 | 931 | 536 → 547 | 102 % |

## Geänderte Titles und Descriptions

| Seite | vorher | nachher |
|---|---|---|
| /impressum.html (Description) | Impressum der Gebäudewerke GbR, Allmend 2, 76707 Hambrücken: Kontakt, Telefon 0163 7221790, Gesellschafter und Angaben nach § 5 DDG. (905 px) | Impressum der Gebäudewerke GbR, Allmend 2, 76707 Hambrücken: Kontakt, Telefon 0176 74025524, Gesellschafter und Angaben nach § 5 DDG. (913 px) |
| /treppenhausreinigung.html (Title) | Treppenhausreinigung Bruchsal | Fester Plan, fester Wochentag (569 px) | Treppenhausreinigung Bruchsal | Plan und fester Wochentag (540 px) |
| /winterdienst.html (Title) | Winterdienst Bruchsal mit Einsatzprotokoll | Gebäudewerke (525 px) | Winterdienst Bruchsal ab 1.220 € netto/Saison | Einsatzprotokoll (569 px) |
| /winterdienst.html (Description) | Winterdienst in Bruchsal: Räumen und Streuen von Gehwegen, Zufahrten und Parkplätzen, Saison November bis März, jeder Einsatz protokolliert. (907 px) | Winterdienst in Bruchsal: Saisonpauschale ab 1.220 € netto bis 120 m², 1. November bis 31. März. Zu jedem Einsatz ein Protokoll. Ortstermin kostenlos. (944 px) |

## Bedientest

| Prüfung | Ergebnis |
|---|---|
| Tastatur: Modell-Punkt per Tab erreichbar | bestanden |
| Tastatur: Enter wählt Zone (aria-pressed) | bestanden |
| Tastatur: Infozeile verlinkt Winterdienst | bestanden: Winterdienst Bruchsal |
| Tastatur: Tab geht zum nächsten Bedienelement | bestanden: metall |
| Modell: 10 Buttons mit Beschriftung | bestanden: Entrümpelung Keller, Dachboden, Wohnung / Treppenhausreinigung fester Wochentag, Aushang mit Datum / Büro- und Praxisreinigung vor Arbeitsbe |
| Modell: Hausmeister verlinkt mit „Hausmeisterservice Bruchsal“ | bestanden |
| Karteikarten: 6 Reiter mit role=tab | bestanden |
| Karteikarten: Pfeil rechts wechselt auf Hausverwaltung | bestanden: r-hv visible |
| Aufgaben: Leertaste wählt Aufgabe, WhatsApp-Text enthält sie | bestanden: https://wa.me/491637221790?text=Hallo Gebäudewerke, bei uns steht an: - Treppenhaus reinigen Ort des Objekts:  |
| Aufgaben: Filter „Gewerbe“ zeigt passende Aufgaben | bestanden: 8 von 22 |
| Rundgang: Knopf vorhanden und nach Auswahl angehalten | bestanden: Rundgang fortsetzen |
| Touch: Tippen auf Modell-Punkt wählt Zone | bestanden |
| Touch: Infozeile zeigt Gartenpflege-Link | bestanden |
| Touch: Zielgröße mindestens 24 px | bestanden: 26x26 |
| Touch: Aufgabe antippen zählt in der Mobilleiste | bestanden |
| Touch: Reiter Winterdienst antippbar | bestanden |
| Handy: kein horizontales Scrollen (390 px) | bestanden: 390 |
| Reduzierte Bewegung: kein automatischer Rundgang | bestanden: aktive Zonen: 0 |
| Reduzierte Bewegung: Pause-Knopf bleibt verborgen | bestanden |
| Reduzierte Bewegung: Laufband steht (keine Kopie) | bestanden |
| Reduzierte Bewegung: Siegel ohne Animation | bestanden: none |
| Ohne JS: alle 6 Karteikarten sichtbar | bestanden: 6 |
| Ohne JS: alle 22 Aufgaben sichtbar | bestanden: 22 |
| Ohne JS: Reiter ausgeblendet | bestanden |
| Ohne JS: Modell-Buttons ausgeblendet, Infozeile mit Link da | bestanden |
| Ohne JS: Leistungsliste unter dem Modell sichtbar | bestanden: 10 |
| Ohne JS: Heute in Bruchsal mit festen Texten | bestanden |
| wetter.php 500: fester Text | bestanden: wetter gerade nicht abrufbar / Amtliche Warnungen für Bruchsal auf dwd.de |
| wetter.php fehler: fester Text | bestanden: wetter gerade nicht abrufbar / Amtliche Warnungen für Bruchsal auf dwd.de |
| Ohne Zustimmung: keine Anfrage an Google | bestanden |
| Consent Mode v2: Standard alles denied | bestanden: [["consent","default",{"ad_storage":"denied","ad_user_data":"denied","ad_personalization":"denied","analytics_storage":"denied","wait_for_up |
| Mit Zustimmung: consent update granted | bestanden |
| Mit Zustimmung: whatsapp_klick mit position | bestanden: {"position":"kopf","link_text":"WhatsApp","seite":"/","transport_type":"beacon"} |
| Mit Zustimmung: verzeichnis_klick mit position | bestanden: {"position":"fuss","verzeichnis":"geolokal.de","seite":"/","transport_type":"beacon"} |
| Mit Zustimmung: anruf_klick mit position | bestanden: {"position":"kontaktblock","link_text":"0163 7221790","seite":"/","transport_type":"beacon"} |
| Mit Zustimmung: generate_lead auf danke.html | bestanden: {"formular":"anfrage","position":"inhalt","seite":"/danke.html","transport_type":"beacon"} |
| Mit Zustimmung: email_klick mit position | bestanden: {"position":"kontaktblock","link_text":"info@gebaeudewerke.de","seite":"/kontakt.html","transport_type":"beacon"} |

## Konflikte und Entscheidungen

Konflikte K1 bis K23 und die Entscheidungen des Inhabers vom 25.11.2026 (P1 bis P8) stehen in `konflikte.md`.

