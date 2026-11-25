# Relaunch 12/2026: Konflikte 07.11. gegen 16.11. und offene [PRÜFEN]-Punkte

Stand 25.11.2026 (mit den Entscheidungen des Inhabers vom selben Tag), Branch `claude/relaunch-2026-12`.

## Was die drei Stände sind

| Kürzel | Commit | Branch | Inhalt |
|---|---|---|---|
| G | f38d527 | claude/gallant-einstein-ossqki (07.11.) | Neues Gestaltungssystem, interaktive Startseite, Seitenkopf der Leistungsseiten, Preisangleichung im Fließtext. War nie live. |
| L | 2ce60a1 | claude/live-stand-2026-11-10 (10.11.) | Kopie der Live-Seite. Inhalt in `<main>` ist Wort für Wort der Stand vor dem 07.11. (70c8eb2), nur fehlen Links auf damals geplante Ratgeber, weil `auslieferung.php` sie beim Ausliefern entfernt hatte. |
| V | 0638e7d | claude/vertrauen-menue-2026-11-16 (16.11.) | L plus: Telefon 0163 7221790, 17 Bewertungen, Trust-Symbole und Verzeichnisse, Pressemitteilung, Barrierefreiheit (Tabellen, Fußbereich, Trust-Karten), Menü-Fix. |
| N | 5b9d09e | claude/nice-planck-khtul6 (06.11.) | Consent Mode v2, `tracking.js`, QR-Codes, Tracking-Anleitung. |

Nachgewiesen mit einem Textvergleich je Seite (Inhalt von `<main>`, Title, Description, JSON-LD): Kopfdaten von G und L sind identisch bis auf `dateModified` der Startseite. Alle Unterschiede zwischen G und V fallen in die Gruppen unten. Nach dem Zusammenführen fehlt gegenüber V kein Satz außer den alten Preisen und den Button-Beschriftungen des alten Kontaktbands (Gestaltung, siehe K16).

## Konflikte und Entscheidung

Regel des Auftrags: Gestaltung, CSS, JavaScript und Interaktion aus G, Texte, Kontaktdaten, Bewertungen, Trust-Elemente, Barrierefreiheit und Menü aus V. Bei Konflikten in Texten gilt V.

| Nr. | Wo | 07.11. (G) | 16.11. (V) | Entscheidung |
|---|---|---|---|---|
| K1 | Startseite, H1 | „Hausmeister und Reinigung in Bruchsal. Vom Keller bis zum Gartentor.“ | „Hausmeister, Reinigung und Außenanlagen in Bruchsal mit einem Ansprechpartner“ | H1 aus V. „Vom Keller bis zum Gartentor.“ bleibt als große Gestaltungszeile unter der H1, ist aber nicht Teil der H1. |
| K2 | Startseite, Einstieg | Kurzer Einstieg, 22 Wörter | Einleitung mit 54 Wörtern | Oben der kurze Einstieg (Vorgabe höchstens 25 Wörter ganz oben). Der Text aus V steht unverändert als Kurzantwort am Anfang von „Unsere Leistungen“. Wie bei den Leistungsseiten am 07.11. Bestätigt vom Inhaber am 25.11. |
| K3 | Startseite, Hero | Gebäudemodell | Foto mit Wochenprotokoll (6 Einträge, Bildunterschrift) | Modell aus G. Das Protokoll aus V (alle 6 Einträge, „Wohnanlage mit 12 Einheiten, Bruchsal“, Bildunterschrift) steht jetzt auf der Karteikarte „Hausverwaltung“ statt der gekürzten 4 Einträge aus G. |
| K4 | Startseite, Leistungen | „Zehn Leistungen. Ein Vertrag.“, eigene Kurztexte, Karten mit „Im Modell: …“ | „Unsere Leistungen für Wohn- und Gewerbeimmobilien“, Kurztexte, Fotos | Überschrift, Einleitung, H3 und Kurztexte aus V (Preis 449 € auf 382 € korrigiert), Kartenaufbau und Reihenfolge aus G, ohne Fotos. Linktexte aus G („Hausmeisterservice in Bruchsal“ usw.). |
| K5 | Startseite, Zusagen | Gekürzte Zusagen im Abschnitt Ablauf | Eigener Abschnitt „Woran Sie uns messen können“ | Eigener Abschnitt mit Überschrift und Texten aus V. |
| K6 | Startseite, Ablauf | „Vier Schritte. Ein Festpreis.“, Schritt 4 „Festpreis und Start“ | „Lernen Sie uns beim Ortstermin kennen“, Schritt 4 „Angebot und Start“ | Texte aus V. |
| K7 | Startseite, Team | „Vier Mann. Eigenes Personal.“ mit Einleitung „Wir sind vier Mann zwischen 30 und 40 …“ | „Das Team hinter Ihrem Objekt“ mit eigener Einleitung | Texte aus V, Link „Mehr über uns“. „Vier Mann, eigenes Personal“ bleibt als kleine Zeile über der Überschrift. |
| K8 | Startseite, Einsatzgebiet | Kürzerer Text | Text mit Referenzorten (Bruchsal, Bad Schönborn, Östringen) | Texte aus V, Kartenschema aus G. |
| K9 | Startseite, Auf einen Blick | Ein zusammengefasster Absatz, Datenblatt | Kurzantwort, zweiter Absatz, zwei Buttons, Datenblatt | Texte aus V, Preise im Datenblatt korrigiert (111 € statt 130 €, 1.220 € statt 1.435 €), Bewertungen 17. |
| K10 | Startseite, Ratgeber | H2 „Pflichten, Fristen, Kosten.“ | „Aus dem Ratgeber“ (dort nur als Absatz formatiert), Teaser mit Fotos | Text aus V, jetzt als H2. Kartenaufbau ohne Fotos aus G. |
| K11 | Startseite, Fragen | H2 „Kurz gefragt. Klar beantwortet.“ | H2 „Häufige Fragen“, alte Preise | H2 aus V, Fragen in beiden gleich, Preise 111/162/238 € (wie G und JSON-LD). |
| K12 | Startseite, Kontakt | „Rufen Sie an.“, große Nummer, Formular „Oder kurz schreiben“ | „Kontakt aufnehmen“ mit Satz, Buttons „Direkt anrufen“, Formular „Kurze Anfrage“ | Überschrift, Satz, Datenliste und Formulartitel aus V. Große Nummer statt Button „Direkt anrufen“ (Gestaltung G). Formularfelder unverändert. |
| K13 | Autorenbox der Ratgeber | Nur „Meisterbrief“ bei Fatih Altun, sonst keine Qualifikation | Qualifikation bei allen vier (z. B. „Gelernter Metallbauer, Erfahrung im Stahl- und Gerüstbau“) | V, wie auf der Teamseite. Bestätigt vom Inhaber am 25.11. |
| K14 | Leistungsseiten, Seitenkopf | Kurzer Einstieg, Anrufen und WhatsApp, Modell mit Zone im Licht | Kurzantwort, Foto, drei Buttons | Seitenkopf aus G (Auftrag). Kurzantwort und Foto aus V stehen unverändert am Anfang des ersten Abschnitts. |
| K15 | Vier geplante Ratgeber | Datum 27.11. bis 15.12. | wie G | Auftrag Punkt 7 sah eine Verschiebung auf den 15.01.2027 vor. Entscheidung Inhaber 25.11.: Die Daten bleiben wie ursprünglich (27.11., 01.12., 08.12., 15.12.), Datumszeile, Title und `plan.json` unverändert. Alle erschienenen Ratgeber zeigen „Zuletzt geprüft am 25.11.2026“ (Meta `artikel-geprueft`), die vier geplanten nicht. |
| K16 | Kontaktband aller Seiten | Große Nummer, „WhatsApp schreiben“, „Anfrage per Formular“, Zeile mit Sternen und Zeiten | Buttons „Anfrage senden“, „Telefonisch anfragen“, „WhatsApp-Nachricht schreiben“ | G (Gestaltung, kommt aus `layout_anwenden.py`). |
| K17 | Ratgeber-Teaser auf 13 Seiten | Links auf damals geplante Beiträge vorhanden | fehlen (beim Live-Import entfernt) | G. `auslieferung.php` blendet geplante Beiträge weiterhin bis zu ihrem Datum aus. Damit erscheinen z. B. die Links auf die am 13.11., 17.11., 20.11. und 24.11. erschienenen Beiträge wieder. |
| K18 | Ratgeber Mülltonnendienst | 77 € netto, 92 € brutto | 90 €, 107 € | G (Wert aus preise.html). |
| K19 | Fußbereich und Mobilleiste | „Telefon:“, Mobilleiste Anrufen/WhatsApp | „Telefon und WhatsApp:“, Leiste „Bewerten Sie uns“, Schnellkontakt, Mobilleiste mit drei Knöpfen | Text „Telefon und WhatsApp“ und Leiste „Bewerten Sie uns“ (mit Presse) aus V, Mobilleiste aus G. |
| K20 | Startseite, Vertrauensangaben | Liste unter den Buttons (Google, Eigenes Personal, Notdienst) | Liste im Hero und blauer Faktenstreifen | Texte aus V: Liste im Hero (4 Punkte), Faktenstreifen als Band unter dem Hero. |
| K21 | Startseite, Zielgruppen | fehlt | „Für Hausverwaltungen, Eigentümer und Gewerbe“ | Übernommen. |
| K22 | Trust-Abschnitt „Geprüft gelistet und bewertet“ | fehlt | Startseite, Über uns, Kontakt; Presse auf Winterdienst | Texte und Links aus V. CSS-Klassen umbenannt (`.verzeichnisse`), weil `.vertrauen` im Gestaltungssystem G der Vertrauensstreifen ist. Animationen auf transform und opacity umgestellt (V animierte Farbe und Schatten). |
| K23 | Schriften | Mona Sans, JetBrains Mono | Archivo | G. Archivo und die Instrument Serif aus N werden nicht mehr geladen. |

Außerdem korrigiert (kein Konflikt, Fehler in beiden Ständen): Im Ratgeber „Hecke schneiden“ stand der erste Satz der Kurzantwort seit dem 06.11. viermal hintereinander (Ursache: `meta_anwenden.py` war nicht idempotent, jetzt behoben).

## Entscheidungen zu den [PRÜFEN]-Punkten (Inhaber, 25.11.2026)

| Nr. | Punkt | Entscheidung | Umsetzung |
|---|---|---|---|
| P1 | Verschiebung der vier Ratgeber | Daten bleiben wie ursprünglich. „Zuletzt geprüft“ für alle erschienenen auf heute. | Verschiebung zurückgenommen, 27 Ratgeber mit „Zuletzt geprüft am 25.11.2026“. |
| P2 | Google-Bewertungen | Aktuelle Bewertungen genau übernehmen. | Abruf 25.11.2026 per OpenSEO: 17 Bewertungen, Schnitt 5,0, alle Texte wörtlich; bei Estelle Klinger steht jetzt auch „⭐⭐⭐⭐⭐“ vor dem Text wie bei Google. |
| P3 | Einsatzgebiet | Ja, und Karlsruhe ebenfalls. | Kraichtal, Weingarten (Baden), Linkenheim-Hochstetten, Eggenstein-Leopoldshafen und Stadt Karlsruhe in Text, Listen, FAQ, JSON-LD, llms.txt und Kartenschema. |
| P4 | Räumzeiten und Laubpflicht | Werte wie auf der Website übernehmen, keine Satzung nötig. | Hinweise [PRÜFEN] entfernt, Werte unverändert. |
| P5 | Telefonnummer | 0163 7221790 ist die einzige Nummer; im Impressum als Anrufnummer 0176 74025524. | Impressum: Telefon 0176 74025524, daneben „Telefon und WhatsApp für Anfragen“ 0163 7221790. Google-Profil zeigt laut Abruf vom 25.11. bereits 0163 7221790. |
| P6 | Qualifikationen in der Autorenbox | In Ordnung. | wie K13 |
| P7 | Datumszeile | siehe P1 | – |
| P8 | Einstieg der Startseite | In Ordnung. | wie K2 |

Offene [PRÜFEN]-Punkte in `website/`: keine.
