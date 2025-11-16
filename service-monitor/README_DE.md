# 🏠 Homelab Service Monitor

🇩🇪 Deutsche Version | **[🇬🇧 English Version](README.md)**

---

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

---

## 🛠️ Überwachte Services

**Aktuell konfiguriert:**
- **Nextcloud** - Self-hosted Cloud Storage
- **Pi-hole** - DNS-basierter Ad-Blocker
- **Tailscale** - VPN für sicheren Remote-Zugriff

---

## 🚀 Installation & Nutzung

### Voraussetzungen:
- Python 3.7 oder höher
- Keine externen Abhängigkeiten (nur Standard Library)

### Installation:
```bash
git clone https://github.com/MCCMDave/homelab-automation.git
cd homelab-automation/service-monitor
python3 homelab_service_monitor.py
```

### Eigene Services hinzufügen:
```python
# In homelab_service_monitor.py:
services = {
    "Dein-Service": {
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
====================================================
=============== Service-Check ======================
====================================================
==                                                ==
== Service: Nextcloud                            ==
==   CPU: 42%                                    ==
==   RAM: 212MB                                  ==
==   Laufzeit: 99.8%                             ==
==   Status: OK                                  ==
==                                                ==
====================================================
==                                                ==
== Service: Tailscale                            ==
==   CPU: 82%                                    ==
==   RAM: 226MB                                  ==
==   Laufzeit: 92.2%                             ==
==   Status: WARNUNG                             ==
==                                                ==
====================================================
==    ALARM: Tailscale - CPU kritisch (82%)     ==
====================================================
```

---

## ⚙️ Konfiguration

### Alarm-Schwellwerte anpassen:

```python
def service_check(service_name, service_daten):
    if cpu > 80:         # CPU-Schwelle (Standard: 80%)
        return "WARNUNG"
    elif ram > 1000:     # RAM-Schwelle (Standard: 1000 MB)
        return "WARNUNG"
    elif laufzeit < 95:  # Laufzeit-Schwelle (Standard: 95%)
        return "WARNUNG"
```

---

## 📈 Geplante Features

**Nächste Version (v2.0):**
- [ ] Automatisches Auslesen echter Service-Metriken
- [ ] Integration mit `systemctl status`
- [ ] E-Mail/Telegram-Benachrichtigungen
- [ ] Historische Daten mit SQLite
- [ ] Web-Dashboard mit Flask
- [ ] Grafische Auswertung (matplotlib)
- [ ] JSON/CSV-Export
- [ ] YAML-Konfigurations-Datei

---

## 🏠 Mein Homelab-Setup

**Hardware:**
- Raspberry Pi 5 (8GB RAM)
- 1TB SSD über USB 3.0
- PoE+ HAT für Stromversorgung

**Software:**
- Raspberry Pi OS (Debian-basiert)
- Docker für Service-Container
- Nextcloud 28
- Pi-hole 5.x
- Tailscale VPN

**Performance:**
- 24/7 Uptime (6+ Monate)
- Verwaltung von 42.000+ Fotos
- 57% Performance-Verbesserung

---

## 💡 Lernreise

Dieses Tool entstand als **Assignment 1** während meiner Python-Lernreise und wurde für den produktiven Einsatz weiterentwickelt.

**Lern-Version:** [python-learning/phase1.5-oop](https://github.com/MCCMDave/python-learning/tree/main/phase1.5-oop)  
**Produktiv-Version:** Dieses Repo

---

## 🛠️ Tech Stack

- Python 3.13
- Nur Standard Library
- Dictionaries zur Datenverwaltung
- Listen für Alarm-Historie

---

## 🔗 Verwandte Projekte

- [Power Savings Tracker](../power-savings-tracker/) - Solarstrom-Ersparnis
- [Python Learning](https://github.com/MCCMDave/python-learning) - Meine Lernreise
- [Windows Automation](https://github.com/MCCMDave/windows-automation) - PowerShell-Scripts

---

## 👨‍💻 Autor

**David Vaupel**  
Homelab-Enthusiast | Python-Entwickler | Linux Essentials Zertifiziert

📧 Kontakt via GitHub Issues  
💼 [LinkedIn](https://www.linkedin.com/in/david-vaupel)

---

**Status:** ✅ Im Produktivbetrieb | Aktiv gewartet  
**Version:** 1.0  
**Letzte Aktualisierung:** November 2025
