# 🏠 Homelab Automatisierungs-Scripts

🇩🇪 Deutsche Version | **[🇬🇧 English Version](README.md)**

---

Python-Tools zur Automatisierung meiner Raspberry Pi 5 Homelab-Infrastruktur.

---

## 🎯 Überblick

Dieses Repository enthält produktionsreife Automatisierungs-Scripts zur Überwachung und Verwaltung meiner 24/7 Homelab-Umgebung. Alle Tools sind aktiv im Einsatz und im Produktivbetrieb getestet.

---

## 🛠️ Tools

### Service Monitor
Überwacht laufende Services und alarmiert bei kritischen Problemen.

**Features:**
- CPU-, RAM- und Laufzeit-Überwachung
- Alarm-System mit Historie
- Kategorisierte Service-Checks
- Formatierte Konsolen-Ausgabe

**Überwachte Services:**
- Nextcloud (Private Cloud-Storage)
- Pi-hole (DNS-basierter Ad-Blocker)
- Tailscale (Sicheres VPN)

**[→ Zum Service Monitor](service-monitor/)**

---

### Power Savings Tracker
Berechnet Stromkosten-Ersparnis durch Solarstromerzeugung.

**Features:**
- Tägliches Tracking mit CSV-Export
- Automatische Zeitstempel
- Kostenberechnung basierend auf kWh
- Historische Datenspeicherung

**[→ Zum Power Savings Tracker](power-savings-tracker/)**

---

## 🏠 Mein Homelab-Setup

**Hardware:**
- Raspberry Pi 5 (8GB RAM)
- 1TB SSD via USB 3.0
- PoE+ HAT für Stromversorgung

**Software-Stack:**
- Raspberry Pi OS (Debian-basiert)
- Docker & Docker Compose
- Nextcloud 28
- Pi-hole 5.x
- Tailscale VPN

**Performance:**
- 24/7 Uptime (6+ Monate)
- Verwaltung von 42.000+ Fotos
- 57% Performance-Verbesserung durch Optimierung
- Scan-Zeiten unter einer Minute

---

## 📦 Installation

```bash
# Repository klonen
git clone https://github.com/MCCMDave/homelab-automation.git
cd homelab-automation

# Zu spezifischem Tool navigieren
cd service-monitor
# oder
cd power-savings-tracker

# Script ausführen
python3 script_name.py
```

---

## 🔗 Verwandte Projekte

- **[python-learning](https://github.com/MCCMDave/python-learning)** - Python lernen durch praktische Projekte
- **[windows-automation](https://github.com/MCCMDave/windows-automation)** - PowerShell-Automatisierungs-Scripts

---

## 💡 Lernreise

Diese Tools wurden als Teil meiner Python-Lernreise entwickelt. Sie starteten als Bildungsaufgaben und entwickelten sich zu produktionsreifen Tools, die ich täglich nutze.

**Von Lernprojekt zu Produktivbetrieb:**
- Assignment 1 → Service Monitor
- Solar-Tracking-Übung → Power Savings Tracker

**[→ Siehe meinen Lernpfad](https://github.com/MCCMDave/python-learning)**

---

## 🛠️ Tech Stack

- Python 3.13
- Nur Standard Library (keine externen Abhängigkeiten)
- Docker (für Homelab-Services)
- Linux (Raspberry Pi OS)

---

## 📊 Projekt-Status

- ✅ **Service Monitor:** Produktionsreif, aktiv im Monitoring-Einsatz
- ✅ **Power Savings Tracker:** Produktionsreif, tägliche Nutzung
- 🔄 **Zukünftige Tools:** Backup-Automatisierung, Log-Analyse

---

## 📄 Lizenz

MIT License - Frei nutzbar für dein eigenes Homelab!

---

## 👨‍💻 Autor

**David Vaupel**  
Homelab-Enthusiast | Python-Entwickler | Linux Essentials Zertifiziert

📧 Kontakt via GitHub Issues  
💼 [LinkedIn](https://www.linkedin.com/in/david-vaupel)

---

**Status:** ✅ Im Produktivbetrieb | Aktiv gewartet  
**Letzte Aktualisierung:** November 2025
