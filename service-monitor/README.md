# 🏠 Homelab Service Monitor

Ein Python-basiertes Monitoring-System zur Überwachung kritischer Services auf einem Raspberry Pi 5 Homelab.

---

## 📖 Beschreibung

Der Service Monitor überwacht wichtige Metriken (CPU, RAM, Laufzeit) von Homelab-Services und generiert Alarme bei kritischen Werten. Entwickelt für den produktiven Einsatz auf einem Raspberry Pi 5.

---

## ✨ Features

### Monitoring:
- ✅ **CPU-Auslastung** pro Service (Alarm ab 80%)
- ✅ **RAM-Nutzung** pro Service (Alarm ab 1000 MB)
- ✅ **Laufzeit** (Uptime) pro Service (Alarm unter 95%)
- ✅ **Status-Check** (OK / WARNUNG)

### Alarm-System:
- ✅ Automatische Alarm-Generierung
- ✅ Alarm-Historie mit Zeitstempel
- ✅ Detaillierte Alarm-Gründe
- ✅ Übersicht aller aktiven Alarme

### Statistiken:
- ✅ Durchschnittliche CPU-Auslastung
- ✅ Durchschnittliche RAM-Nutzung
- ✅ Gesamtübersicht aller Services

### Ausgabe:
- ✅ Formatierte Konsolen-Ausgabe mit Rahmen
- ✅ Farbcodierung (geplant)
- ✅ Übersichtliche Service-Details

---

## 🛠️ Überwachte Services

### Aktuell konfiguriert:
- **Nextcloud** - Self-hosted Cloud Storage
- **Pi-hole** - DNS-basierter Ad-Blocker
- **Tailscale** - VPN für sicheren Remote-Zugriff

### Service-Metriken (Beispiel):
```python
"Nextcloud": {
    "cpu": 42,           # CPU-Auslastung in %
    "ram": 212,          # RAM-Nutzung in MB
    "laufzeit": 99.8,    # Uptime in %
    "status": "aktiv"
}
```

---

## 🚀 Installation & Nutzung

### Voraussetzungen:
- Python 3.7 oder höher
- Keine externen Dependencies (nur Standard Library)

### Installation:
```bash
# Repository klonen
git clone https://github.com/MCCMDave/homelab-automation.git
cd homelab-automation/service-monitor

# Direkt ausführen
python homelab_service_monitor.py
```

### Eigene Services hinzufügen:
```python
# In homelab_service_monitor.py:
services = {
    "Nextcloud": { ... },
    "Pi-hole": { ... },
    
    # Deinen Service hinzufügen:
    "Mein-Service": {
        "cpu": 25,
        "ram": 150,
        "laufzeit": 98.5,
        "status": "aktiv"
    }
}
```

---

## 📊 Beispiel-Ausgabe

```
========================================================
=================== Service-Check-Test =================
========================================================
==                                                    ==
== Service: Nextcloud                                 ==
==   CPU: 42%                                         ==
==   RAM: 212MB                                       ==
==   Laufzeit: 99.8%                                  ==
==   Status: OK                                       ==
==                                                    ==
========================================================
==                                                    ==
== Service: Tailscale                                 ==
==   CPU: 82%                                         ==
==   RAM: 226MB                                       ==
==   Laufzeit: 92.2%                                  ==
==   Status: WARNUNG                                  ==
==                                                    ==
========================================================
==         ALARM: Tailscale - CPU-Auslastung         ==
==                   kritisch (82%)                   ==
========================================================
==                                                    ==
==               Gesamtauslastung                     ==
==           Durchschnitt CPU: 45.3%                  ==
==           Durchschnitt RAM: 189MB                  ==
==                                                    ==
==                    Alarme: 1                       ==
==                                                    ==
========================================================
```

---

## ⚙️ Konfiguration

### Alarm-Schwellwerte anpassen:

```python
# In service_check() Funktion:
def service_check(service_name, service_daten):
    cpu = service_daten["cpu"]
    ram = service_daten["ram"]
    laufzeit = service_daten["laufzeit"]
    
    # Schwellwerte hier anpassen:
    if cpu > 80:              # CPU-Schwelle (Standard: 80%)
        return "WARNUNG"
    elif ram > 1000:          # RAM-Schwelle (Standard: 1000 MB)
        return "WARNUNG"
    elif laufzeit < 95:       # Laufzeit-Schwelle (Standard: 95%)
        return "WARNUNG"
    else:
        return "OK"
```

---

## 🔄 Automatisierung (Geplant)

### Cron-Job für regelmäßige Checks:

```bash
# Jede Stunde ausführen:
0 * * * * cd /home/dave/homelab-automation/service-monitor && python3 homelab_service_monitor.py >> /var/log/service-monitor.log 2>&1
```

### Systemd Service (Alternative):

```ini
[Unit]
Description=Homelab Service Monitor
After=network.target

[Service]
Type=simple
User=dave
ExecStart=/usr/bin/python3 /home/dave/homelab-automation/service-monitor/homelab_service_monitor.py
Restart=always

[Install]
WantedBy=multi-user.target
```

---

## 📈 Geplante Features

**Nächste Version (v2.0):**
- [ ] Automatisches Auslesen echter Service-Metriken
- [ ] Integration mit `systemctl status`
- [ ] E-Mail/Telegram-Benachrichtigungen bei Alarmen
- [ ] Historische Daten mit SQLite
- [ ] Web-Dashboard mit Flask
- [ ] Grafische Auswertung (matplotlib)
- [ ] Export als JSON/CSV
- [ ] Konfiguration via YAML-Datei

---

## 🏗️ Architektur

### Funktionen:
- `service_check()` - Prüft einen Service auf Probleme
- `alarm_generator()` - Erstellt Alarm-Einträge
- `durchschnitt()` - Berechnet Durchschnittswerte
- `alles_zeigen()` - Haupt-Ausgabe-Funktion

### Datenstrukturen:
- `services` (dict) - Service-Konfiguration
- `alarm_historie` (list) - Alle generierten Alarme

---

## 🧪 Testing

```python
# Test einzelner Funktionen:
python test_homelab_monitor.py

# Manueller Test im Script:
if __name__ == "__main__":
    alles_zeigen()
```

---

## 📝 Entstehung

Dieses Tool entstand als **Assignment 1** während meines Python-Lernprojekts und wurde für den produktiven Einsatz weiterentwickelt.

**Lern-Version:** [python-learning/phase1.5-oop](https://github.com/MCCMDave/python-learning/tree/main/phase1.5-oop)  
**Produktiv-Version:** Dieses Repo

---

## 🛠️ Verwendete Technologien

- **Python 3.13** - Programmiersprache
- **Standard Library** - Keine externen Dependencies
- **datetime** - Zeitstempel für Alarme
- **Dictionaries** - Service-Daten-Verwaltung
- **Listen** - Alarm-Historie

---

## 🏠 Mein Homelab-Setup

**Hardware:**
- Raspberry Pi 5 (8GB RAM)
- 1TB SSD über USB 3.0
- PoE+ HAT für Stromversorgung

**Software:**
- Raspberry Pi OS (Debian-based)
- Docker für Service-Container
- Nextcloud 28
- Pi-hole 5.x
- Tailscale VPN

**Netzwerk:**
- Lokales Netzwerk mit statischer IP
- Tailscale für Remote-Zugriff
- Pi-hole als DNS-Server

---

## 🔗 Verwandte Projekte

- [Power Savings Tracker](../power-savings-tracker/) - Solarstrom-Ersparnis
- [Python Learning](https://github.com/MCCMDave/python-learning) - Meine Lernreise
- [Windows Automation](https://github.com/MCCMDave/windows-automation) - PowerShell Scripts

---

## 💡 Lessons Learned

- **Dictionaries** zur strukturierten Datenhaltung
- **Funktionen** zur Code-Modularisierung
- **Error-Handling** für robuste Tools
- **Formatierung** für professionelle Ausgaben
- **Tuple-Returns** für mehrere Rückgabewerte

---

## 🤝 Beitragen

Verbesserungsvorschläge und Pull Requests sind willkommen!

**Besonders gesucht:**
- Integration echter Service-Metriken
- Benachrichtigungs-System
- Web-Dashboard
- Weitere Service-Templates

---

## 📄 Lizenz

MIT License - Frei nutzbar für eigene Homelabs!

---

## 👨‍💻 Autor

**Dave Vaupel**  
Homelab-Enthusiast | Python-Entwickler | Linux Essentials Certified

📧 Kontakt via GitHub Issues  
🏠 Homelab: Raspberry Pi 5 + Nextcloud + Pi-hole + Tailscale

---

**Status:** ✅ Produktiv im Einsatz  
**Version:** 1.0  
**Letzte Aktualisierung:** November 2025  
**Python:** 3.13+
