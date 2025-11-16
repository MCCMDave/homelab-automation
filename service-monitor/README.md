# 🏠 Homelab Service Monitor

**[🇩🇪 Deutsche Version](README_DE.md)** | 🇬🇧 English Version

---

A Python-based monitoring system for critical services on a Raspberry Pi 5 homelab.

---

## 📖 Description

The Service Monitor tracks important metrics (CPU, RAM, uptime) of homelab services and generates alarms for critical values. Developed for production use on a Raspberry Pi 5.

---

## ✨ Features

### Monitoring:
- ✅ **CPU usage** per service (alarm at 80%+)
- ✅ **RAM usage** per service (alarm at 1000+ MB)
- ✅ **Uptime** per service (alarm below 95%)
- ✅ **Status check** (OK / WARNING)

### Alarm System:
- ✅ Automatic alarm generation
- ✅ Alarm history with timestamps
- ✅ Detailed alarm reasons
- ✅ Overview of all active alarms

### Statistics:
- ✅ Average CPU usage
- ✅ Average RAM usage
- ✅ Overall service summary

---

## 🛠️ Monitored Services

**Currently configured:**
- **Nextcloud** - Self-hosted cloud storage
- **Pi-hole** - DNS-based ad blocker
- **Tailscale** - VPN for secure remote access

---

## 🚀 Installation & Usage

### Requirements:
- Python 3.7 or higher
- No external dependencies (Standard Library only)

### Installation:
```bash
git clone https://github.com/MCCMDave/homelab-automation.git
cd homelab-automation/service-monitor
python3 homelab_service_monitor.py
```

### Add Your Own Services:
```python
# In homelab_service_monitor.py:
services = {
    "Your-Service": {
        "cpu": 25,
        "ram": 150,
        "laufzeit": 98.5,
        "status": "aktiv"
    }
}
```

---

## 📊 Example Output

```
====================================================
================ Service Check ====================
====================================================
==                                                ==
== Service: Nextcloud                            ==
==   CPU: 42%                                    ==
==   RAM: 212MB                                  ==
==   Uptime: 99.8%                               ==
==   Status: OK                                  ==
==                                                ==
====================================================
==                                                ==
== Service: Tailscale                            ==
==   CPU: 82%                                    ==
==   RAM: 226MB                                  ==
==   Uptime: 92.2%                               ==
==   Status: WARNING                             ==
==                                                ==
====================================================
==     ALARM: Tailscale - CPU critical (82%)    ==
====================================================
```

---

## ⚙️ Configuration

### Adjust Alarm Thresholds:

```python
def service_check(service_name, service_daten):
    if cpu > 80:         # CPU threshold (default: 80%)
        return "WARNUNG"
    elif ram > 1000:     # RAM threshold (default: 1000 MB)
        return "WARNUNG"
    elif laufzeit < 95:  # Uptime threshold (default: 95%)
        return "WARNUNG"
```

---

## 📈 Planned Features

**Next Version (v2.0):**
- [ ] Automatic reading of real service metrics
- [ ] Integration with `systemctl status`
- [ ] Email/Telegram notifications
- [ ] Historical data with SQLite
- [ ] Web dashboard with Flask
- [ ] Graphical analysis (matplotlib)
- [ ] JSON/CSV export
- [ ] YAML configuration file

---

## 🏠 My Homelab Setup

**Hardware:**
- Raspberry Pi 5 (8GB RAM)
- 1TB SSD via USB 3.0
- PoE+ HAT for power

**Software:**
- Raspberry Pi OS (Debian-based)
- Docker for service containers
- Nextcloud 28
- Pi-hole 5.x
- Tailscale VPN

**Performance:**
- 24/7 uptime (6+ months)
- Managing 42,000+ photos
- 57% performance improvement

---

## 💡 Learning Journey

This tool started as **Assignment 1** during my Python learning journey and evolved into a production-ready tool.

**Learning Version:** [python-learning/phase1.5-oop](https://github.com/MCCMDave/python-learning/tree/main/phase1.5-oop)  
**Production Version:** This repo

---

## 🛠️ Tech Stack

- Python 3.13
- Standard Library only
- Dictionaries for data management
- Lists for alarm history

---

## 🔗 Related Projects

- [Power Savings Tracker](../power-savings-tracker/) - Solar power savings
- [Python Learning](https://github.com/MCCMDave/python-learning) - My learning journey
- [Windows Automation](https://github.com/MCCMDave/windows-automation) - PowerShell scripts

---

## 👨‍💻 Author

**David Vaupel**  
Homelab Enthusiast | Python Developer | Linux Essentials Certified

📧 Contact via GitHub Issues  
💼 [LinkedIn](https://www.linkedin.com/in/david-vaupel)

---

**Status:** ✅ In Production | Actively Maintained  
**Version:** 1.0  
**Last Updated:** November 2025
