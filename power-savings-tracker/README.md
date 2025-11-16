# ⚡ Power Savings Tracker

Ein einfaches Python-Tool zur Berechnung der Stromkosten-Ersparnis durch Solarstromerzeugung.

---

## 📖 Beschreibung

Dieses Tool berechnet die tägliche Stromkosten-Ersparnis basierend auf der erzeugten Solarstrom-Menge (kWh) und speichert die Historie in einer CSV-Datei.

---

## ✨ Features

- ✅ Berechnung der Ersparnis basierend auf aktuellem Strompreis
- ✅ Automatische CSV-Export mit Historie
- ✅ Header-Erstellung bei neuer Datei
- ✅ Datums-Stempel für jede Messung
- ✅ Input-Validierung (nur Zahlen)
- ✅ Error-Handling für ungültige Eingaben

---

## 🚀 Installation & Nutzung

### Voraussetzungen:
- Python 3.7 oder höher

### Ausführung:
```bash
python power_savings_tracker.py
```

### Bedienung:
1. Programm starten
2. Erzeugte kWh eingeben
3. Ersparnis wird angezeigt
4. Daten werden in `historie.csv` gespeichert
5. ENTER drücken zum Beenden

---

## 📊 Beispiel-Ausgabe

```
Wie viel kWh wurden erzeugt? 12.5

Am 16.11.25 beträgt die Strompreis-Ersparnis: 3.65€ 

Drücke ENTER, zum Schließen des Fensters.
```

---

## 📁 Datei-Struktur

### Erzeugte Dateien:
- **historie.csv** - Speichert alle Messungen mit Datum

### CSV-Format:
```csv
Datum; kWh; Ersparnis in €
16.11.25; 12.50; 3.65
17.11.25; 15.20; 4.43
```

---

## ⚙️ Konfiguration

### Strompreis anpassen:
```python
# Zeile 5 in power_savings_tracker.py:
price = 0.2916  # Aktueller Strompreis in €/kWh
```

**Aktueller Preis:** 0,2916 €/kWh (Stand: November 2025)

---

## 🛠️ Technische Details

### Genutzte Module:
- `datetime` - Datums-Verwaltung
- `os` - Dateisystem-Prüfung

### Funktionsweise:
1. Aktuelles Datum abrufen
2. kWh-Eingabe vom Nutzer
3. Ersparnis berechnen (kWh × Preis)
4. CSV-Datei prüfen (existiert / leer?)
5. Header einfügen falls nötig
6. Daten anhängen

---

## 📈 Erweiterungsmöglichkeiten

**Mögliche Verbesserungen:**
- [ ] Monats-/Jahres-Statistiken
- [ ] Grafische Auswertung (matplotlib)
- [ ] Automatischer Abruf von Wechselrichter-Daten
- [ ] Vergleich mit Vormonaten
- [ ] Export als PDF-Report
- [ ] Web-Interface mit Flask

---

## 🏠 Homelab-Integration

**Aktuell:** Manuelle Eingabe  
**Geplant:** Automatischer Abruf vom Wechselrichter via API

**Mein Setup:**
- Solaranlage auf dem Dach
- Wechselrichter mit Netzwerk-Anbindung
- Raspberry Pi 5 als Homelab-Server

---

## 📝 Entstehung

Dieses Tool war eines meiner ersten Python-Projekte beim Lernen von:
- Input/Output
- Variablen & Datentypen
- Datei-Operationen
- Error-Handling
- CSV-Export

**Teil von:** [Python Learning Journey](https://github.com/MCCMDave/python-learning)

---

## 💡 Lessons Learned

- **Try-Except:** Robuste Input-Validierung
- **With-Statement:** Sicherer Datei-Zugriff
- **F-Strings:** Formatierte Ausgaben
- **CSV-Handling:** Header-Verwaltung
- **OS-Modul:** Dateisystem-Checks

---

## 📊 Historie-Beispiel

Nach einem Monat sieht die CSV so aus:

```csv
Datum; kWh; Ersparnis in €
01.11.25; 8.50; 2.48
02.11.25; 12.30; 3.59
03.11.25; 15.80; 4.61
...
30.11.25; 11.20; 3.27

Gesamt: 340 kWh = 99.14€ Ersparnis! 💰
```

---

## 🔗 Verwandte Projekte

- [Service Monitor](../service-monitor/) - Homelab Service Überwachung
- [Python Learning](https://github.com/MCCMDave/python-learning) - Meine Lernreise

---

## 👨‍💻 Autor

**Dave Vaupel**  
Homelab-Enthusiast | Python-Lerner | Linux Essentials Certified

---

**Status:** ✅ Funktionsfähig | In produktiver Nutzung  
**Version:** 1.0  
**Letzte Änderung:** November 2025
