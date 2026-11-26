# Erzeugt flaechen_und_mieten.xlsx und massnahmen_und_kosten.xlsx. Aufruf: python3 tabellen.py
import json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as CL
H=Font(bold=True); T=Font(bold=True,size=14); EIN=PatternFill('solid',fgColor='FFF2B3'); KOPF=PatternFill('solid',fgColor='DDE3EA'); SUM=PatternFill('solid',fgColor='EEF0F2')
EUR='#,##0 "€"'; EUR2='#,##0.00 "€"'; M2='#,##0.00 "m²"'; PRZ='0.00 "%"'
def kopf(ws,r,cols):
    for i,c in enumerate(cols,1):
        x=ws.cell(r,i,c); x.font=H; x.fill=KOPF; x.alignment=Alignment(wrap_text=True,vertical='top')
def breit(ws,w):
    for i,v in enumerate(w,1): ws.column_dimensions[CL(i)].width=v
F=json.load(open('flaechen.json'))
# ===================== flaechen_und_mieten.xlsx =====================
wb=Workbook(); ws=wb.active; ws.title='Übersicht'
ws['A1']='Weiherer Straße 111, Ubstadt-Weiher: Wohnflächen und Mieten vorher und nachher'; ws['A1'].font=T
ws['A2']='Stand 26.11.2026. Gelbe Zellen sind Eingaben. Wohnfläche nach WoFlV; Rendite = Jahresnettokaltmiete × 100 / Kaufpreis (ohne PV-Erlöse, ohne Stellplätze).'
ws['A4']='Kaufpreis (Eingabe)'; ws['C4'].fill=EIN; ws['C4'].number_format=EUR; ws['A4'].font=H
ws['A5']='Modernisierungskosten brutto (aus massnahmen_und_kosten.xlsx, änderbar)'; ws['C5']=539242; ws['C5'].fill=EIN; ws['C5'].number_format=EUR
ws['A7']='Mietansätze netto kalt (Eingabe, Quellen im Blatt "Quellen Mieten")'; ws['A7'].font=H
ans=[('Vorher: Bestandswohnung unsaniert (Annahme, Ist-Miete unten eintragen)',9.50),('Vorher: große OG-Wohnung 132 m² unsaniert (Annahme)',9.00),
     ('Nachher: modernisierte Bestandswohnung EG/OG, Effizienzhaus',11.50),('Nachher: neue DG-Wohnung, Erstbezug, Neubaustandard',13.00)]
for i,(t,v) in enumerate(ans):
    ws.cell(8+i,1,t); c=ws.cell(8+i,3,v); c.fill=EIN; c.number_format='0.00 "€/m²"'
r=13; ws.cell(r,1,'VORHER (Bestand, 4 Wohnungen, Flächen laut Aufmaß)').font=H; r+=1
kopf(ws,r,['Wohnung','Lage','Wohnfläche','Ansatz €/m²','Ist-Miete €/Monat (Eingabe, falls bekannt)','Nettokaltmiete €/Monat','Nettokaltmiete €/Jahr']); r+=1
vor=[('W1','EG West',72.14,'C8'),('W2','EG Altbau',59.90,'C8'),('W3','EG Anbau Garten (Balkon 23,28 m² zu 1/4)',67.66,'C8'),('W4','ganzes OG',132.03,'C9')]
v0=r
for w,l,a,ref in vor:
    ws.cell(r,1,w); ws.cell(r,2,l); ws.cell(r,3,a).number_format=M2; ws.cell(r,4,f'={ref}').number_format=EUR2; ws.cell(r,5).fill=EIN; ws.cell(r,5).number_format=EUR2
    ws.cell(r,6,f'=IF(E{r}="",C{r}*D{r},E{r})').number_format=EUR2; ws.cell(r,7,f'=F{r}*12').number_format=EUR; r+=1
ws.cell(r,1,'Summe vorher').font=H; ws.cell(r,3,f'=SUM(C{v0}:C{r-1})').number_format=M2; ws.cell(r,6,f'=SUM(F{v0}:F{r-1})').number_format=EUR2; ws.cell(r,7,f'=SUM(G{v0}:G{r-1})').number_format=EUR
for c in range(1,8): ws.cell(r,c).fill=SUM
sv=r; r+=2
ws.cell(r,1,'NACHHER (Umbau, 7 Wohnungen, Flächen aus dem Modell, Blatt "Flächen nachher")').font=H; r+=1
kopf(ws,r,['Wohnung','Lage','Wohnfläche','Ansatz €/m²','Zimmer','Nettokaltmiete €/Monat','Nettokaltmiete €/Jahr']); r+=1
lage={'W1':('EG West, eigener Eingang Nord','2 Zi., Küche, Bad','C10'),'W2':('EG Altbau','2 Zi., Küche, Bad, Ankleide','C10'),'W3':('EG Anbau Garten, Balkon','2 Zi., Küche, Bad, Balkon','C10'),
 'W4':('OG West, Eingang Podest P1','3 Zi., Wohnküche, Bad','C10'),'W5':('OG Altbau, Eingang Laubengang','2 Zi., Küche/Essen, Bad, HWR','C10'),
 'W6':('DG West, neu','3 Zi., Wohnküche, Bad','C11'),'W7':('DG Ost, neu','2 Zi., Wohnküche, Bad','C11')}
n0=r
for w,(l,z,ref) in lage.items():
    ws.cell(r,1,w); ws.cell(r,2,l); ws.cell(r,3,f"=SUMIF('Flächen nachher'!A:A,A{r},'Flächen nachher'!C:C)").number_format=M2; ws.cell(r,4,f'={ref}').number_format=EUR2
    ws.cell(r,5,z); ws.cell(r,6,f'=C{r}*D{r}').number_format=EUR2; ws.cell(r,7,f'=F{r}*12').number_format=EUR; r+=1
ws.cell(r,1,'Summe nachher').font=H; ws.cell(r,3,f'=SUM(C{n0}:C{r-1})').number_format=M2; ws.cell(r,6,f'=SUM(F{n0}:F{r-1})').number_format=EUR2; ws.cell(r,7,f'=SUM(G{n0}:G{r-1})').number_format=EUR
for c in range(1,8): ws.cell(r,c).fill=SUM
sn=r; r+=2
ws.cell(r,1,'ERGEBNIS').font=H; r+=1
for t,f_,fmt in (('Wohnfläche vorher',f'=C{sv}',M2),('Wohnfläche nachher',f'=C{sn}',M2),('Mehrfläche',f'=C{sn}-C{sv}',M2),
                 ('Jahresnettokaltmiete vorher',f'=G{sv}',EUR),('Jahresnettokaltmiete nachher',f'=G{sn}',EUR),('Mehrmiete pro Jahr',f'=G{sn}-G{sv}',EUR),
                 ('Rendite vorher (Nettokaltmiete × 100 / Kaufpreis)',f'=IF(C4>0,G{sv}*100/C4,"Kaufpreis eingeben")',PRZ),
                 ('Rendite nachher (Nettokaltmiete × 100 / Kaufpreis)',f'=IF(C4>0,G{sn}*100/C4,"Kaufpreis eingeben")',PRZ),
                 ('Zusatzinfo: Rendite nachher auf Kaufpreis + Modernisierungskosten',f'=IF(C4>0,G{sn}*100/(C4+C5),"Kaufpreis eingeben")',PRZ),
                 ('Zusatzinfo: Mehrmiete × 100 / Modernisierungskosten',f'=IF(C5>0,(G{sn}-G{sv})*100/C5,"")',PRZ)):
    ws.cell(r,1,t); c=ws.cell(r,3,f_); c.number_format=fmt; c.font=H; r+=1
ws.cell(r+1,1,'Hinweise: Die Vorher-Mieten sind Annahmen, weil die Ist-Mieten nicht vorlagen. Bei laufenden Mietverhältnissen gelten § 558 BGB (Vergleichsmiete) und § 559 BGB (Modernisierungsumlage 8 %, Kappung 3 €/m² in 6 Jahren); Beratung durch Haus & Grund oder Fachanwalt. Erstvermietung nach umfassender Modernisierung und neue DG-Wohnungen fallen nach § 556f BGB nicht unter die Mietpreisbremse (Geltung in Ubstadt-Weiher prüfen).')
breit(ws,[62,34,14,13,26,20,20])
# Flaechen nachher
w2=wb.create_sheet('Flächen nachher'); kopf(w2,1,['Wohnung','Raum','Wohnfläche WoFlV m²','Grundfläche m²','Methode'])
for i,e in enumerate(F['raeume'],2):
    w2.cell(i,1,e['whg']); w2.cell(i,2,e['raum']); w2.cell(i,3,e['flaeche']).number_format='0.00'; w2.cell(i,4,e['grund']).number_format='0.00'; w2.cell(i,5,e['quelle'])
i+=2; w2.cell(i,1,'Methode: unveränderte Räume mit Aufmaßwert, neue oder geänderte Räume aus den Planmaßen des Modells (Fertigmaß zwischen Wandoberflächen). Unter Dachschrägen: Flächen unter 1 m lichter Höhe 0, 1 bis 2 m zur Hälfte, ab 2 m voll (§ 4 WoFlV). Balkon zu 1/4 (§ 4 Nr. 4 WoFlV, bis zur Hälfte zulässig). Toleranz ca. ±2 % bis zum Aufmaß nach Fertigstellung.')
breit(w2,[10,26,20,16,70])
# Flaechen vorher
w3=wb.create_sheet('Flächen vorher'); kopf(w3,1,['Wohnung','Raum','Wohnfläche WoFlV m²','Quelle'])
VOR=[('W1','Flur',2.29),('W1','Wohnen/Schlafen mit Raumteiler',55.16),('W1','Bad',6.04),('W1','Küche',5.51),('W1','Abstellraum',3.14),
 ('W2','Wohnen',16.35),('W2','Schlafen',14.60),('W2','Küche',12.01),('W2','Flur',3.80),('W2','begehbarer Kleiderschrank',9.77),('W2','Bad',3.37),
 ('W3','Zugang',4.43),('W3','Küche',6.68),('W3','Wohnen/Essen',28.25),('W3','Schlafen',16.08),('W3','Bad',6.40),('W3','Balkon 23,28 m² zu 1/4',5.82),
 ('W4','Schlafen',14.01),('W4','Bad',5.07),('W4','Gästezimmer',12.71),('W4','Flur',8.79),('W4','Wohnen (West)',31.84),('W4','Raum 01',16.35),('W4','Raum 02',14.60),('W4','Küche',12.02),('W4','Hausflur',6.87),('W4','Raum 03',9.77)]
for i,(w,rn,a) in enumerate(VOR,2): w3.cell(i,1,w); w3.cell(i,2,rn); w3.cell(i,3,a).number_format='0.00'; w3.cell(i,4,'Aufmaß Nagel 24.09.2026')
breit(w3,[10,34,20,28])
# Quellen Mieten
w4=wb.create_sheet('Quellen Mieten'); kopf(w4,1,['Ort','Wert €/m²','Stand / Bezug','Quelle'])
Q=[('Ubstadt-Weiher',10.34,'Q1/2026, Wohnungen','https://www.immobilienpreise-2026.de/bw/ubstadt-weiher'),('Ubstadt-Weiher',10.64,'Durchschnitt 2026','https://www.immoportal.com/mietspiegel/ubstadt-weiher'),
   ('Ubstadt-Weiher',11.60,'Wohnungen bis 100 m², 2026','https://www.immoportal.com/mietspiegel/ubstadt-weiher'),('Ubstadt-Weiher',11.40,'Durchschnitt, Stand 09/2025','https://www.mietpreise.info/mietspiegel/ubstadt-weiher'),
   ('Ubstadt-Weiher','10,25 bis 14,25','Spanne Häuser','https://www.immobilienscout24.de/regional/de/baden-wuerttemberg/karlsruhe-kreis/ubstadt-weiher/'),
   ('Bruchsal',12.13,'ortsüblich, 2026','https://www.ohne-makler.net/mietspiegel/baden-wurttemberg/bruchsal/'),('Bruchsal',11.73,'Wohnungen 61 bis 90 m²','https://www.immoportal.com/mietspiegel/bruchsal'),
   ('Bruchsal',12.19,'Durchschnitt (5 Angebote)','https://www.mietpreise.info/mietspiegel/bruchsal')]
for i,q in enumerate(Q,2):
    for j,v in enumerate(q,1): w4.cell(i,j,v)
w4.cell(len(Q)+3,1,'Einordnung: Für Ubstadt-Weiher wurde kein qualifizierter Mietspiegel gefunden; die Werte sind Angebotsmieten aus Portalen (abgerufen 26.11.2026). Ansatz nachher: 11,50 €/m² für modernisierte Bestandswohnungen (oberes Drittel der Ortswerte, Effizienzhaus, neues Bad), 13,00 €/m² für Erstbezug im DG (über dem Ortsdurchschnitt, unter Bruchsal-Neubau). Vor Vermietung mit aktuellen Angeboten abgleichen.')
breit(w4,[18,16,30,90])
wb.save('flaechen_und_mieten.xlsx')
# ===================== massnahmen_und_kosten.xlsx =====================
BA={0:'BA 0 Planung, Genehmigung, Förderantrag',1:'BA 1 Dach, DG-Wohnungen, Erschließung, Technik',2:'BA 2 Gebäudehülle (Gerüst aus BA 1)',3:'BA 3 OG leerziehen, teilen, sanieren (W4, W5)',4:'BA 4 EG nacheinander (W1, W2, W3)',5:'BA 5 Außenanlagen'}
# (BA, Maßnahme, Menge, Einheit, Material €/Einheit, Fremdleistung € gesamt, Eigenleistung, Lohnwert EL €, Begründung, Gewerk/Nachweis, förderfähig BEG, Bemerkung)
K=[(0,'Entwurf, Bauantrag, Detailplanung (LPH 1 bis 4, Teile LPH 5)',1,'psch',0,21000,'nein',0,'Bauvorlageberechtigung erforderlich','Architekt oder Bauvorlageberechtigter (Pflicht)','teilweise','HOAI-Orientierung, Kostenbasis ca. 450 T€'),
 (0,'Tragwerksplanung: Aufstockung auf Mauerwerk 1949, Dachstuhl, Laubengangdecke, Abfangung, Stahltreppen',1,'psch',0,10000,'nein',0,'statischer Nachweis','Statiker (Pflicht)','nein',''),
 (0,'Bautechnische Prüfung (Gebäudeklasse 4)',1,'psch',0,4500,'nein',0,'','Prüfingenieur (bei GK 4 in BW prüfen)','nein',''),
 (0,'Brandschutznachweis GK 4, Rettungswege, Außentreppen',1,'psch',0,4000,'nein',0,'','Brandschutzplaner (Pflicht)','nein',''),
 (0,'Schallschutznachweis DIN 4109',1,'psch',0,1800,'nein',0,'','Bauphysiker','nein',''),
 (0,'Energieeffizienz-Experte: iSFP, Effizienzhaus- oder EM-Nachweis, Antrag, Baubegleitung, Bestätigung nach Durchführung',1,'psch',0,8500,'nein',0,'Fördervoraussetzung','Energieeffizienz-Experte dena-Liste (Pflicht)','ja','Baubegleitung gesondert gefördert'),
 (0,'Vermessung, amtlicher Lageplan, Abstandsflächen',1,'psch',0,2200,'nein',0,'','Vermesser (Pflicht für Bauantrag)','nein',''),
 (0,'Gebühren Baugenehmigung und Abnahmen',1,'psch',0,3800,'nein',0,'','Baurechtsamt','nein',''),
 (0,'Schadstoffprüfung Dach und Fassade (Asbest, alte Mineralwolle)',1,'psch',0,900,'nein',0,'','Sachverständiger','nein','Faserzement aus 1966 möglich'),
 (1,'Gerüst Fassade und Dach, Standzeit ca. 4 Monate, auch für WDVS',620,'m²',0,11200,'nein',0,'Gerüstbau ist Fachfirma','Gerüstbauer','teilweise',''),
 (1,'Abbruch Dachstuhl und Deckung, Entsorgung',1,'psch',3200,0,'ja',6000,'einfache Arbeit, Container','','teilweise','Schadstoffe vorher klären'),
 (1,'Kniestock, Giebel, Brandwand Ost aufmauern, Ringbalken',75,'m²',48,2500,'teilweise',4500,'Mauern in Eigenleistung, Ringbalken mit Fachbetrieb','Statik, Bauleitung','nein',''),
 (1,'Dachstuhl neu: KVH/BSH, Pfetten, Abbund, Richten, Kran',13,'m³',680,14000,'nein',0,'Abbund und Richten nur mit Zimmerer realistisch','Zimmerer, Statiker','nein',''),
 (1,'Sichtschalung, Dampfbremse, Aufsparrendämmung PIR 160 mm, Unterdeckung',165,'m²',78,0,'ja',6600,'Systemaufbau nach Herstellerdetail','Bestätigung EEE','ja','U ca. 0,14 W/m²K'),
 (1,'Dachdeckung Betondachstein anthrazit, Lattung, First, Ortgang',165,'m²',40,0,'ja',6000,'machbar mit Erfahrung, Fachregeln Dachdecker','','ja',''),
 (1,'Metalldächer Zwerchhaus, Gaube, Schleppdach, Kehlen, Wandanschlüsse',50,'m²',75,6500,'nein',0,'Dichtheit an Kehlen und Anschlüssen','Klempner oder Dachdecker','ja',''),
 (1,'Dachrinnen, Fallrohre, Schneefang',1,'psch',1800,1200,'teilweise',800,'','Klempner','teilweise',''),
 (1,'Dachflächenfenster 78/118 mit Eindeckrahmen',4,'Stk',950,0,'ja',1200,'Einbau nach Herstelleranleitung','','ja','Uw ≤ 1,0'),
 (1,'Fenster DG, Zwerchhaus, Gaube, 3-fach, Uw ≤ 0,95',7.5,'m²',520,1500,'teilweise',600,'Montage RAL durch Fensterbauer','Fensterbauer','ja',''),
 (1,'Wohnungseingangstüren W6, W7 außen, RC2, Ud ≤ 1,3',2,'Stk',2300,600,'nein',0,'Dichtheit, Gewährleistung','Tischler oder Fensterbauer','ja',''),
 (1,'Laubengang und Eingangszone: Flachdach rückbauen, Stahlbetondecke tiefer neu, Abfangträger',22,'m²',60,6800,'nein',0,'tragende Bauteile','Bauunternehmen, Statik','nein','löst Höhenkonflikt OG-Fenster'),
 (1,'Laubengang: Gefälledämmung, Abdichtung, Stelzlager, Platten, Entwässerung',22,'m²',125,1800,'teilweise',900,'Abdichtung durch Fachbetrieb','Dachdecker','ja',''),
 (1,'Flachdach über W3: Dämmung PIR 180 mm, Abdichtung 2-lagig, Kies',80,'m²',58,4200,'teilweise',1500,'Dämmung in Eigenleistung, Abdichtung Fachbetrieb','Dachdecker','ja','U ca. 0,13 W/m²K'),
 (1,'Hoftreppe feuerverzinkt, zweiläufig, 27 Steigungen, Podest P1, Zwischenpodest, Geländer, Fundamente',1,'psch',23000,3500,'teilweise',2000,'Fundamente in Eigenleistung, Montage mit Kran','Schlosser/Stahlbau, Statik','nein','Laufbreite 1,10 m'),
 (1,'Treppe zum DG feuerverzinkt, 14 Steigungen, Podest P2, Geländer, Vordächer',1,'psch',12500,2000,'teilweise',1200,'','Schlosser/Stahlbau','nein','Laufbreite 1,03 m'),
 (1,'DG Trockenestrich, Trittschalldämmung, Fußbodenheizung Trockensystem',117,'m²',85,0,'ja',3500,'Systemverlegung','Heizungsbauer: Druckprobe, Abgleich','ja',''),
 (1,'DG Trockenbau: Innenwände, Ergänzung Wohnungstrennwand, Vorwände',70,'m²',38,0,'ja',2800,'','Brandschutzdetail Trennwand','nein',''),
 (1,'DG Bäder: bodengleiche Dusche, WC, Waschtisch, Fliesen, Anschlüsse',2,'Stk',4800,1800,'teilweise',3000,'Anschlüsse und Abnahme Installateur','Installateur','nein',''),
 (1,'DG Elektroinstallation, Unterverteilung, Netzwerk',2,'Whg',2600,2400,'teilweise',2000,'Schlitze und Leerrohre in Eigenleistung','Elektrofachbetrieb (Pflicht)','nein',''),
 (1,'DG Lüftung: Abluftventilatoren Bad und Küche, Außenluftdurchlässe',2,'Whg',1100,300,'ja',600,'Elektroanschluss durch Elektriker','Lüftungskonzept DIN 1946-6','ja',''),
 (1,'DG Böden Vinyl, Innentüren, Maler',117,'m²',55,0,'ja',5000,'','','nein',''),
 (1,'Wärmepumpe Luft/Wasser ca. 18 kW Monoblock, Speicher, Hydraulik, Regelung, Fundament',1,'psch',21000,9000,'nein',0,'Förderung und Gewährleistung nur mit Fachbetrieb; Monoblock ohne Kältekreisarbeiten vor Ort','Heizungsbauer (Pflicht), Kälteschein nur bei Split','ja','Schallgutachten Aufstellort'),
 (1,'Steigleitungen Heizung, Trinkwasser, Zirkulation, Wohnungsübergaben mit Wärmemengenzähler',7,'Whg',1100,3500,'teilweise',1500,'','Installateur','teilweise',''),
 (1,'Zählerschrank, Hausanschlussverstärkung, Allgemeinstrom',1,'psch',3500,3500,'nein',0,'','Elektrofachbetrieb, Netzbetreiber','nein',''),
 (1,'Photovoltaik 5,6 kWp (13 Module), Wechselrichter, Montage',5.6,'kWp',900,2000,'teilweise',1200,'Modulmontage in Eigenleistung möglich','Elektrofachbetrieb, Netzbetreiber','nein','nicht BEG; KfW 270 möglich'),
 (1,'Decken Altbau EG/OG und OG/DG auf F60 ertüchtigen (GKF von unten)',132,'m²',34,4600,'nein',0,'zugelassenes System mit Bescheinigung','Trockenbau-Fachbetrieb, Brandschutzplaner','nein','Voraussetzung GK 4'),
 (1,'Schornsteine stilllegen, über Dach rückbauen, Schacht für Leitungen nutzen',1,'psch',400,600,'teilweise',800,'','Schornsteinfeger (Abnahme)','nein',''),
 (2,'Fenster EG und OG tauschen, 3-fach, Uw ≤ 0,95, RAL-Montage',35.5,'m²',520,6200,'nein',0,'bewohnte Wohnungen, Nachweis für Förderung','Fensterbauer','ja',''),
 (2,'Haustür Hauseingang und Eingang W1, Ud ≤ 1,3',2,'Stk',2900,800,'nein',0,'','Tischler','ja',''),
 (2,'Wohnungseingangstüren W4, W5 außen, RC2',2,'Stk',2300,600,'nein',0,'','Tischler','ja',''),
 (2,'WDVS EPS 032, 160 mm, mineralischer Oberputz hell, Brandriegel',300,'m²',52,2500,'ja',18000,'zugelassenes System; Schulung Hersteller, Kontrolle EEE','Bestätigung EEE','ja','U ca. 0,18 W/m²K; Brandriegel bei GK 4'),
 (2,'Sockel: Perimeterdämmung XPS, Sockelputz dunkel',108,'m²',42,0,'ja',5000,'','','ja',''),
 (2,'Fensterbänke außen Aluminium, Laibungen',40,'Stk',45,0,'ja',1200,'','','ja',''),
 (2,'Kellerdecke und Decke über Garagen von unten dämmen, 120 mm',255,'m²',26,0,'ja',3800,'einfach, ohne Spezialwerkzeug','','ja','U ca. 0,25 W/m²K'),
 (3,'OG teilen: Durchgang schließen, Treppe EG/OG und Bodentreppe ausbauen, Deckenöffnungen schließen',1,'psch',2200,1500,'teilweise',2500,'Deckenschluss nach Statik','Statik','nein',''),
 (3,'W4 und W5 Bäder neu',2,'Stk',4600,1800,'teilweise',3000,'','Installateur','nein',''),
 (3,'W4 und W5 Fußbodenheizung Fräs- oder Dünnschichtsystem',133,'m²',32,3300,'teilweise',2000,'Fräsen durch Fachbetrieb, Verlegen in Eigenleistung','Heizungsbauer','ja',''),
 (3,'W4 und W5 Elektro, Lüftung, Böden, Türen, Maler',2,'Whg',7500,2400,'teilweise',7000,'','Elektrofachbetrieb','teilweise',''),
 (4,'W1, W2, W3 Bäder neu',3,'Stk',4400,5400,'teilweise',9000,'','Installateur','nein',''),
 (4,'W1, W2, W3 Fußbodenheizung Fräs- oder Dünnschichtsystem',205,'m²',32,5100,'teilweise',3000,'','Heizungsbauer','ja',''),
 (4,'W1, W2, W3 Elektro, Lüftung, Böden, Türen, Maler, Trennwand W1',3,'Whg',7500,3600,'teilweise',10500,'','Elektrofachbetrieb','teilweise',''),
 (4,'Wohnungseingangstüren W2, W3 zum Hausflur, Schallschutz',2,'Stk',950,300,'teilweise',200,'','Tischler','nein',''),
 (4,'Hausflur, Hauseingangstreppe, Technikraum renovieren',1,'psch',1800,0,'ja',1500,'','','nein',''),
 (5,'Hof Pflaster ergänzen, 3 Stellplätze markieren',80,'m²',38,0,'ja',2400,'','','nein','Lage nach Lageplan'),
 (5,'Fahrradüberdachung 14 Plätze',1,'psch',2600,0,'ja',600,'','','nein',''),
 (5,'Regenwasseranschlüsse, Schächte',1,'psch',900,600,'teilweise',500,'','','nein','')]
wb=Workbook(); ws=wb.active; ws.title='Maßnahmen'
ws['A1']='Weiherer Straße 111: Maßnahmen und Kosten (Kostenschätzung brutto, Preisstand 11/2026, ohne Angebote, Genauigkeit ca. ±25 %)'; ws['A1'].font=T
kopf(ws,3,['Nr','Bauabschnitt','Maßnahme','Menge','Einheit','Material €/Einheit','Material €','Fremdleistung €','Kosten gesamt €','Eigenleistung','Lohnwert Eigenleistung €','Begründung Eigenleistung','Gewerk, Fachfirmen- oder Nachweispflicht','BEG-förderfähig','Bemerkung'])
r=4
for n,(b,m,q,e,pm,fr,el,lw,beg,gw,fo,bem) in enumerate(K,1):
    vals=[n,BA[b],m,q,e,pm,f'=D{r}*F{r}',fr,f'=G{r}+H{r}',el,lw,beg,gw,fo,bem]
    for j,v in enumerate(vals,1):
        c=ws.cell(r,j,v); c.alignment=Alignment(wrap_text=True,vertical='top')
        if j in (6,7,8,9,11): c.number_format=EUR
    r+=1
last=r-1
breit(ws,[5,26,58,8,7,12,12,13,14,11,13,34,34,12,26])
ws.freeze_panes='D4'
w2=wb.create_sheet('Bauabschnitte'); w2['A1']='Summen nach Bauabschnitten'; w2['A1'].font=T
kopf(w2,3,['Bauabschnitt','Material €','Fremdleistung €','Kosten gesamt €','Lohnwert Eigenleistung €','davon förderfähig (Kosten mit "ja") €','kumuliert €'])
rr=4
for k,t in BA.items():
    w2.cell(rr,1,t)
    for j,col in ((2,'G'),(3,'H'),(4,'I'),(5,'K')): w2.cell(rr,j,f"=SUMIF(Maßnahmen!$B$4:$B${last},$A{rr},Maßnahmen!{col}$4:{col}${last})").number_format=EUR
    w2.cell(rr,6,f'=SUMIFS(Maßnahmen!$I$4:$I${last},Maßnahmen!$B$4:$B${last},$A{rr},Maßnahmen!$N$4:$N${last},"ja")').number_format=EUR
    w2.cell(rr,7,f'=SUM($D$4:D{rr})').number_format=EUR; rr+=1
w2.cell(rr,1,'Summe netto Maßnahmen').font=H
for j in range(2,7): w2.cell(rr,j,f'=SUM({CL(j)}4:{CL(j)}{rr-1})').number_format=EUR
s1=rr; rr+=1
w2.cell(rr,1,'Unvorhergesehenes 10 %'); w2.cell(rr,4,f'=D{s1}*0.1').number_format=EUR; rr+=1
w2.cell(rr,1,'Gesamtkosten brutto inkl. Reserve').font=H; w2.cell(rr,4,f'=D{s1}+D{s1+1}').number_format=EUR; w2.cell(rr,4).font=H; tot=rr; rr+=1
w2.cell(rr,1,'Eigenleistungsanteil (Lohnwert / (Kosten + Lohnwert))'); w2.cell(rr,4,f'=E{s1}/(D{s1}+E{s1})').number_format='0.0 %'; rr+=2
w2.cell(rr,1,'Finanzierungsrahmen').font=H; rr+=1
w2.cell(rr,1,'Bankrahmen Modernisierung'); w2.cell(rr,4,100000).number_format=EUR; w2.cell(rr,4).fill=EIN; bk=rr; rr+=1
w2.cell(rr,1,'durch Bankrahmen gedeckt bis einschließlich'); w2.cell(rr,4,f'=IF(G4>D{bk},"nicht einmal BA 0",IF(G5>D{bk},"BA 0 und Teil von BA 1",IF(G6>D{bk},"BA 0 und BA 1","weiter")))'); rr+=1
w2.cell(rr,1,'Finanzierungslücke nach Bankrahmen'); w2.cell(rr,4,f'=D{tot}-D{bk}').number_format=EUR; rr+=2
w2.cell(rr,1,'Die Lücke ist mit KfW-Förderkredit, weiterem Bankdarlehen, Eigenkapital oder Zuschüssen (BEG EM) zu schließen. Ablauf und Förderwege siehe modernisierungsplan.md.')
breit(w2,[52,16,16,18,22,30,16])
w3=wb.create_sheet('Annahmen')
for i,t in enumerate(['Preise brutto inkl. 19 % MwSt (Vermietung: kein Vorsteuerabzug), Preisstand 11/2026, eigene Erfahrungswerte, keine Angebote eingeholt.',
 'Mengen aus dem Modell umbau_geometrie.py (Dachfläche ca. 215 m², Fassade ca. 300 m² netto, Fenster ca. 47 m² zuzüglich 4 Dachfenster).',
 'Lohnwert Eigenleistung = was eine Firma für die selbst erbrachte Arbeit berechnen würde; nicht in den Kosten enthalten.',
 'Förderfähig "ja": energetische Maßnahme nach BEG (Einzelmaßnahme oder Effizienzhaus); Eigenleistung nur mit Materialkosten und Bestätigung des Energieeffizienz-Experten.',
 'Nicht enthalten: Kaufnebenkosten, Finanzierungskosten, Mietausfall, Umzugshilfen für Mieter, Küchenmöbel, Außenanlagen über das Genannte hinaus.'],1):
    w3.cell(i,1,t)
breit(w3,[150])
wb.save('massnahmen_und_kosten.xlsx'); print('ok')
