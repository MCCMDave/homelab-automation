# 🖥️ Homelab-Service-Monitor

**Autor:** David Vaupel | **Status:** Produktiv | **Sprache:** Python 3.13

---

## 🎯 Was macht dieses Projekt?

Ein intelligentes Monitoring-System für meinen Raspberry Pi, das kontinuierlich die wichtigsten Services überwacht und bei kritischen Zuständen automatisch Alarm schlägt. Das Programm analysiert Nextcloud, Pi-hole und Tailscale auf drei zentrale Metriken: CPU-Auslastung, RAM-Verbrauch und Uptime-Prozentsatz.

Das besondere an diesem Monitor: Er zeigt nicht nur Probleme an, sondern erstellt auch eine vollständige Alarm-Historie mit echten Zeitstempeln. Jeder kritische Zustand wird dokumentiert und kann später nachvollzogen werden. Das Dashboard gibt mir auf einen Blick Auskunft über den Gesundheitszustand meines Homelabs!

---

## ⚙️ Wie funktioniert es?

Das System nutzt ein Dictionary zur Verwaltung der Service-Daten und eine Liste für die Alarm-Historie. Sobald ein Service die definierten Schwellwerte überschreitet (CPU > 80%, RAM > 1000MB, Laufzeit < 95%), wird automatisch ein Alarm mit echtem Zeitstempel über das datetime-Modul generiert.

Die Architektur ist modular aufgebaut: Jede Funktion hat eine klare Aufgabe. `service_check()` prüft die Werte, `alarm_generator()` erstellt die Alarme, `durchschnitt()` berechnet die Gesamtauslastung und `alles_zeigen()` orchestriert das komplette Dashboard. Die Ausgabe erfolgt mit zentrierter Formatierung für optimale Lesbarkeit im Terminal.

---

## 📋 Installation & Start

### Hauptprogramm starten:
```bash
python david_vaupel_assignment1.py
```

Das Dashboard zeigt alle Services, deren aktuelle Metriken und die komplette Alarm-Historie auf einen Blick an.

### Test-Suite ausführen:
```bash
python test_assignment1.py
```

Die Test-Suite prüft einzelne Funktionen isoliert - perfekt zum Debuggen oder wenn ich neue Features hinzufüge. Sie testet:
- Service-Checks für alle drei Services
- Alarm-Generierung und -Speicherung
- Durchschnittsberechnungen

---

## 🏗️ Projektstruktur
```
assignment1/
│
├── david_vaupel_assignment1.py    # Haupt-Programm
├── test_assignment1.py            # Test-Suite
└── README_assignment1.md          # Diese Datei
```

**Warum zwei Dateien?**
Die Trennung von Haupt-Code und Tests hält den Code sauber und professionell. Die Test-Datei importiert die Funktionen aus der Haupt-Datei und kann diese isoliert testen, ohne das komplette Dashboard zu starten.

---

## 🔧 Technische Highlights

**Datenstrukturen:**
- Dictionary für Service-Verwaltung (verschachtelt mit Metriken)
- Liste für chronologische Alarm-Historie
- Tuple für Rückgabe von Durchschnittswerten

**Module & Features:**
- `datetime` für echte Zeitstempel im Format "TT.MM.JJ um HH:MM:SS Uhr"
- String-Formatierung mit `.center()` für perfekt zentrierte Ausgabe
- f-Strings für dynamische Texte
- Modularer Aufbau mit wiederverwendbaren Funktionen

**Schwellwerte & Logik:**
- CPU > 80% → WARNUNG
- RAM > 1000MB → WARNUNG  
- Uptime < 95% → WARNUNG
- If-elif-else Ketten für Statusprüfung

**Überwachte Services:**
- **Nextcloud:** Dateiserver und Cloud-Lösung
- **Pi-hole:** DNS-basierter Ad-Blocker
- **Tailscale:** VPN-Tunnel für sicheren Zugriff

---

## 💡 Gelernte Konzepte

Bei diesem Projekt habe ich mehrere wichtige Python-Konzepte vertieft:

**Dictionaries & verschachtelte Strukturen:** Die Services sind als Dictionary organisiert, wobei jeder Service selbst wieder ein Dictionary mit Metriken enthält. Das ermöglicht strukturierten Zugriff mit `services["Nextcloud"]["cpu"]`.

**Listen-Operationen:** Die `alarm_historie` ist eine Liste, die dynamisch mit `.append()` erweitert wird. Später iteriere ich mit `for alarm in alarm_historie` darüber.

**Modulare Funktionen:** Jede Funktion hat genau eine Aufgabe (Single Responsibility Principle). Das macht den Code testbar und wartbar.

**String-Formatierung:** Die zentrierte Ausgabe nutzt `.center(breite, füllzeichen)` kombiniert mit f-Strings für dynamische Werte.

**Tuple Unpacking:** Die `durchschnitt()` Funktion gibt zwei Werte als Tuple zurück, die ich mit `durch_cpu, durch_ram = durchschnitt()` elegant entpacke.

**Modul-Import:** Die Test-Datei demonstriert wie man Funktionen aus anderen Python-Dateien importiert - wichtig für größere Projekte!

---

## 🚀 Mögliche Erweiterungen

Ideen für zukünftige Versionen:

- **CSV-Export:** Alarm-Historie in Datei speichern für langfristige Analyse
- **Echte Daten:** Integration mit `psutil` für Live-Daten vom Pi
- **Threshold-Konfiguration:** Schwellwerte in Config-Datei auslagern
- **Email-Alerts:** Bei kritischen Alarmen automatisch benachrichtigen
- **Web-Dashboard:** Flask-Integration für Browser-Zugriff
- **Grafische Darstellung:** Charts mit matplotlib für Trend-Analyse

---

## 🎓 Warum dieses Projekt?

Dieses Monitoring-System ist mein erster Schritt in Richtung Homelab-Automatisierung mit Python. Bisher habe ich hauptsächlich Bash-Scripts für meinen Raspberry Pi geschrieben, aber Python bietet viel mehr Möglichkeiten für strukturierten, wartbaren Code.

Das Projekt zeigt auch meinen Lernfortschritt: Von einfachen Variablen und Schleifen hin zu komplexeren Datenstrukturen und modularer Architektur. Der anfängerfreundliche Docstring-Stil hilft mir dabei, später schnell zu verstehen was jede Funktion macht - ohne im Code nach Details suchen zu müssen.

---

## 📊 Status & Nächste Schritte

**Aktueller Status:** ✅ Voll funktionsfähig  
**Getestet auf:** Python 3.13.9 (Windows) & 3.13.7 (Windows)  
**Nächster Schritt:** Integration mit echten Daten vom Raspberry Pi

---

**Erstellt:** 07.11.2025  
**Letzte Aktualisierung:** 09.11.2025  
**Teil von:** Dave's Python-Lern-Projekt