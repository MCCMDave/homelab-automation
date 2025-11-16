# 🏠 Homelab Automation Scripts

**[🇩🇪 Deutsche Version](README_DE.md)** | 🇬🇧 English Version

---

Python tools for automating my Raspberry Pi 5 homelab infrastructure.

---

## 🎯 Overview

This repository contains production-ready automation scripts for monitoring and managing my 24/7 homelab environment. All tools are actively used and battle-tested in a production setup.

---

## 🛠️ Tools

### Service Monitor
Monitors running services and alerts on critical issues.

**Features:**
- CPU, RAM, and uptime monitoring
- Alarm system with history tracking
- Categorized service checks
- Formatted console output

**Monitored Services:**
- Nextcloud (private cloud storage)
- Pi-hole (DNS-based ad blocker)
- Tailscale (secure VPN)

**[→ View Service Monitor](service-monitor/)**

---

### Power Savings Tracker
Calculates electricity cost savings from solar power generation.

**Features:**
- Daily tracking with CSV export
- Automatic timestamping
- Cost calculation based on kWh
- Historical data storage

**[→ View Power Savings Tracker](power-savings-tracker/)**

---

## 🏠 My Homelab Setup

**Hardware:**
- Raspberry Pi 5 (8GB RAM)
- 1TB SSD via USB 3.0
- PoE+ HAT for power delivery

**Software Stack:**
- Raspberry Pi OS (Debian-based)
- Docker & Docker Compose
- Nextcloud 28
- Pi-hole 5.x
- Tailscale VPN

**Performance:**
- 24/7 uptime (6+ months)
- Managing 42,000+ photos
- 57% performance improvement through optimization
- Sub-minute scan times

---

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/MCCMDave/homelab-automation.git
cd homelab-automation

# Navigate to specific tool
cd service-monitor
# or
cd power-savings-tracker

# Run script
python3 script_name.py
```

---

## 🔗 Related Projects

- **[python-learning](https://github.com/MCCMDave/python-learning)** - Learning Python through practical projects
- **[windows-automation](https://github.com/MCCMDave/windows-automation)** - PowerShell automation scripts

---

## 💡 Learning Journey

These tools were developed as part of my Python learning journey. They started as educational assignments and evolved into production-ready tools that I use daily.

**From learning project to production:**
- Assignment 1 → Service Monitor
- Solar tracking exercise → Power Savings Tracker

**[→ See my learning path](https://github.com/MCCMDave/python-learning)**

---

## 🛠️ Tech Stack

- Python 3.13
- Standard Library only (no external dependencies)
- Docker (for homelab services)
- Linux (Raspberry Pi OS)

---

## 📊 Project Status

- ✅ **Service Monitor:** Production-ready, actively monitoring
- ✅ **Power Savings Tracker:** Production-ready, daily use
- 🔄 **Future Tools:** Backup automation, log analysis

---

## 📄 License

MIT License - Free to use for your own homelab!

---

## 👨‍💻 Author

**David Vaupel**  
Homelab Enthusiast | Python Developer | Linux Essentials Certified

📧 Contact via GitHub Issues  
💼 [LinkedIn](https://www.linkedin.com/in/david-vaupel)

---

**Status:** ✅ In Production | Actively Maintained  
**Last Updated:** November 2025
