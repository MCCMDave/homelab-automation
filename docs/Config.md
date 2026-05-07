# RASPBERRY PI SYSTEM-KONFIGURATION v2.3

## 📋 Quick Reference Commands

```bash
# SSH
ssh pi

# Nextcloud (lokal)
http://192.168.2.54:8080

# Nextcloud (Tailscale)
http://100.103.86.47:8080

# Pi-hole
http://192.168.2.54/admin

# Docker Status
docker ps
docker compose logs -f app
```

---

## Hardware & OS

- Raspberry Pi 5 (8GB RAM)
- 1TB SSD (geklont von SD-Karte)
- Raspberry Pi OS (Debian-basiert)
- Hostname: dave
- User: dave
- Auto-Login: Aktiv

---

## Netzwerk-Grundkonfiguration

- Router: Speedport Smart 4 (192.168.2.1)
- Pi statische IP: 192.168.2.54 (im Router zugewiesen)
- DHCP-Bereich Router: 192.168.2.100 - 192.168.2.230
- Verbindung: WLAN (Interface: wlan0, Connection: "preconfigured")
- MAC-Adresse: 2c:cf:67:a2:b2:a4
- Netzwerk-Manager: NetworkManager (NICHT dhcpcd!)

---

## DNS-Konfiguration

- Pi-hole läuft auf: 192.168.2.54:53
- Upstream DNS (Pi-hole): 1.1.1.1 (Cloudflare), 208.67.222.222 (OpenDNS)
- Pi selbst nutzt: 127.0.0.1 (eigenes Pi-hole)
- Router DNS-Weiterleitung: → 192.168.2.54
- Alle Netzwerkgeräte nutzen: Pi als DNS

### /etc/resolv.conf

```
nameserver 127.0.0.1
nameserver 8.8.8.8
```
- Datei ist mit chattr +i gesperrt gegen Überschreiben
- Hinweis: 8.8.8.8 ist Fallback, Pi-hole nutzt intern 1.1.1.1 und 208.67.222.222

### NetworkManager DNS-Konfiguration

/etc/NetworkManager/NetworkManager.conf:

```
[main]
plugins=ifupdown,keyfile
dns=default
[ifupdown]
managed=false
```

WLAN-Verbindung "preconfigured":
- ipv4.dns = 127.0.0.1 8.8.8.8
- ipv4.ignore-auto-dns = yes

---

## Pi-hole Konfiguration

- Status: Aktiv, Blocking enabled
- Web-Interface: http://192.168.2.54/admin
- Version: Neuere Version (nutzt pihole.toml statt setupVars.conf)
- Konfigurationsdatei: /etc/pihole/pihole.toml
- Upstream DNS: 1.1.1.1, 208.67.222.222
- DHCP Server: OFF (Router macht DHCP)
- Gravity DB: 48 MB (zuletzt aktualisiert: 12. Okt 04:22)

---

## Tailscale Konfiguration

- Exit Node: Aktiv
- Tailscale Hostname: pi
- Tailscale IP: 100.103.86.47
- Magic DNS: Deaktiviert (--accept-dns=false)
- SSH über Tailscale: Funktioniert

### Verbundene Geräte:

- Handy-Dave (Android): 100.91.187.1
- Laptop-Dave (Windows): 100.108.172.100
- PC-Dave (Windows): 100.105.141.15

**WICHTIG:** --accept-dns=false muss IMMER gesetzt bleiben!

### Nutzungsempfehlung:

- **Im Heimnetzwerk:** Tailscale AUSSCHALTEN (spart Akku, schnellere Verbindung)
- **Unterwegs:** Tailscale EINSCHALTEN (sicherer Zugriff auf Nextcloud + Pi)
- **Stand-PC:** Tailscale NICHT nötig (kann deinstalliert werden)

---

## SSH-Zugriff

### Lokal (Heimnetzwerk):

```bash
ssh pi          # Nutzt Alias aus ~/.ssh/config
ssh dave@dave   # Direkt über Hostname
ssh dave@192.168.2.54  # Direkt über IP
```

### Über Tailscale (unterwegs):

```bash
ssh dave@pi     # Tailscale Hostname
ssh dave@100.103.86.47  # Tailscale IP
```

### SSH Config (Stand-PC):

Pfad: `C:\Users\Startklar\.ssh\config`

```
Host pi
    HostName dave
    User dave
    IdentityFile ~/.ssh/id_ed25519
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null
```

### SSH Keys:

- SSH Server: Aktiv
- SSH-Keys eingerichtet von:
  * Windows Laptop (laptop-dave)
  * Windows Desktop (pc-dave) - Ed25519 Key
- Passwortlose Anmeldung aktiv
- MOTD deaktiviert (.hushlogin)

---

## Docker Installation

- Docker Version: 20.10.24+dfsg1
- Docker Compose: v2.40.0
- User dave ist in docker-Gruppe (kann ohne sudo arbeiten)
- Dienst: docker.service (aktiv)

---

## Nextcloud Installation (Docker)

### Basis-Konfiguration

- Installation via Docker Compose
- Konfigurationspfad: `/home/dave/nextcloud/`
- docker-compose.yml: `/home/dave/nextcloud/docker-compose.yml`
- Web-Interface (lokal): http://192.168.2.54:8080
- Web-Interface (Tailscale): http://100.103.86.47:8080
- Version: Nextcloud 32.0.0 (latest)
- PHP: 8.3.26
- Datenbank: MariaDB 10.6

### Performance-Optimierungen (v2.3)

- ✅ APCu Memory Cache aktiviert (3-5x schneller)
- ✅ PHP Memory Limit: 512M
- ✅ PHP Upload Limit: 10G
- ✅ Cron-Job für Background-Tasks (alle 5 Minuten)
- ✅ Preview-Generierung optimiert (2048x2048, JPEG Quality 60)
- ✅ **MariaDB Performance-Tuning** (NEU in v2.3!)
  - InnoDB Buffer Pool: **1600 MB** (13x größer!)
  - Query Cache: **128 MB** (aktiviert)
  - Temp Tables: **128 MB**
  - Optimierte Log-Files
- ✅ **Database Indices optimiert** (NEU in v2.3!)
- ✅ **Performance: 38,6 Sek** für 474k Dateien (57% schneller!)

### Container

- **nextcloud-app-1**: Nextcloud Applikation (Port 8080 → 80)
- **nextcloud-db-1**: MariaDB Datenbank (Port 3306, nur intern)

### Verzeichnisstruktur

```
/home/dave/nextcloud/
├── docker-compose.yml          # Hauptkonfiguration
├── mariadb-config/             # MariaDB Custom Config (NEU v2.3!)
│   └── my.cnf                  # Performance-Tuning
├── html/                       # Nextcloud Installation
├── config/                     # Nextcloud Config-Dateien
├── apps/                       # Nextcloud Apps
└── db/                         # MariaDB Datenbank

/home/dave/Desktop/nextcloud/   # AKTIVES Datenverzeichnis
├── dave_admin/                 # User-Dateien
│   ├── files/                  # Hochgeladene Dateien
│   │   ├── Bilder/             # Nach Jahren + Monaten sortiert!
│   │   │   ├── 2014/
│   │   │   │   ├── 01-Januar/
│   │   │   │   ├── 02-Februar/
│   │   │   │   └── ...
│   │   │   ├── 2015/
│   │   │   ├── ...
│   │   │   └── 2025/
│   │   │       └── 10-Oktober/
│   │   ├── _Zu_Pruefen/        # Spam-Bilder zur Prüfung
│   │   ├── Gedichte/
│   │   ├── Musik/
│   │   ├── Projekte/
│   │   ├── Schriften + Konto/
│   │   ├── Schulung/
│   │   ├── Talk/
│   │   └── Video/
│   ├── cache/
│   └── files_trashbin/
├── appdata_oc359yhhnr30/       # App-Daten
├── .ncdata                     # Wichtig: Nextcloud Marker-Datei
├── .htaccess                   # Apache-Konfiguration
└── nextcloud.log               # Log-Datei
```

### Datenbank-Credentials

```
MYSQL_ROOT_PASSWORD: Elaine+Dave021222
MYSQL_USER: nextcloud
MYSQL_PASSWORD: E+D021222
MYSQL_DATABASE: nextcloud
MYSQL_HOST: db
```

### Nextcloud Admin-User

```
Username: dave_admin
Passwort: [in Passwort-Manager]
```

### Trusted Domains

- 100.103.86.47:8080 (Tailscale IP) - Für Zugriff von unterwegs
- 192.168.2.54:8080 (Lokale IP) - Für Zugriff im Heimnetzwerk

### Windows Desktop Client (Stand-PC)

- Installiert und konfiguriert
- Verbindung: http://192.168.2.54:8080 (lokale IP)
- Sync-Ordner: C:\Users\Startklar\Desktop\Nextcloud\
- Automatische Synchronisation aktiv
- Sync-Test erfolgreich: <20 Sekunden in beide Richtungen! ✅
- Keine Konfliktdateien vorhanden ✅

### Android App (Xiaomi Poco)

- Installiert, aber Auto-Upload unzuverlässig (MIUI Batterie-Probleme)
- Manuelle Uploads funktionieren problemlos
- Use Tailscale DNS: DEAKTIVIERT (wichtig!)
- Batterieoptimierung: Deaktiviert
- Autostart: Aktiviert
- Upload-Zielordner: /Bilder/2025/10-Oktober/ (direkt ins richtige Jahr!)

### Wichtige Nextcloud-Befehle

```bash
# Container Status
docker ps

# Logs anzeigen
docker compose logs -f app

# Container neu starten
cd ~/nextcloud
docker compose restart

# Container stoppen/starten
docker compose down
docker compose up -d

# Nextcloud OCC-Befehle (Kommandozeilen-Tool)
docker exec -u www-data nextcloud-app-1 php occ status
docker exec -u www-data nextcloud-app-1 php occ files:scan --all
docker exec -u www-data nextcloud-app-1 php occ config:system:get trusted_domains

# Trusted Domain hinzufügen
docker exec -u www-data nextcloud-app-1 php occ config:system:set trusted_domains X --value=NEUE_IP

# Wartungsmodus
docker exec -u www-data nextcloud-app-1 php occ maintenance:mode --on
docker exec -u www-data nextcloud-app-1 php occ maintenance:mode --off

# Memory Cache prüfen
docker exec -u www-data nextcloud-app-1 php occ config:system:get memcache.local
```

---

## MariaDB Performance-Tuning (NEU in v2.3!)

### Custom my.cnf

**Pfad:** `/home/dave/nextcloud/mariadb-config/my.cnf`

**Wichtigste Optimierungen:**
- **InnoDB Buffer Pool:** 1600 MB (von 128 MB → 13x größer!)
- **Query Cache:** 128 MB (aktiviert, war OFF)
- **Temp Tables:** 128 MB (von 16 MB → 8x größer!)
- **Optimierte Log-Files:** Weniger Disk I/O

### Performance-Verbesserung

**Files-Scan (474.481 Dateien):**
- Vorher: ~90 Sekunden (geschätzt)
- Nachher: **38,6 Sekunden** = **57% schneller!** 🔥

### Docker Compose Integration

Die my.cnf wird als Volume in den DB-Container gemountet:

```yaml
db:
  volumes:
    - ./db:/var/lib/mysql
    - ./mariadb-config/my.cnf:/etc/mysql/conf.d/custom.cnf:ro
```

### MariaDB-Parameter prüfen

```bash
# InnoDB Buffer Pool Größe
docker exec nextcloud-db-1 mysql -u root -p"Elaine+Dave021222" -e "SHOW VARIABLES LIKE 'innodb_buffer_pool_size';"

# Query Cache Status
docker exec nextcloud-db-1 mysql -u root -p"Elaine+Dave021222" -e "SHOW VARIABLES LIKE 'query_cache%';"

# Alle wichtigen Parameter
docker exec nextcloud-db-1 mysql -u root -p"Elaine+Dave021222" -e "
SELECT 
  'innodb_buffer_pool_size' as Setting, 
  @@innodb_buffer_pool_size/1024/1024 as 'Value_MB'
UNION ALL SELECT 'query_cache_size', @@query_cache_size/1024/1024
UNION ALL SELECT 'max_connections', @@max_connections
UNION ALL SELECT 'tmp_table_size', @@tmp_table_size/1024/1024;
"
```

---

## Firewall (UFW)

- Status: Aktiv und beim Systemstart aktiviert
- Konfiguration:

| Port | Protokoll | Von | Zweck |
|------|-----------|-----|-------|
| 22 | TCP | Anywhere | SSH |
| 53 | TCP/UDP | Anywhere | Pi-hole DNS |
| 80 | TCP | Anywhere | Pi-hole Web-Interface |
| 8080 | TCP | 192.168.2.0/24 | Nextcloud (nur lokal!) |

**Resultat:** Nextcloud ist NUR aus dem lokalen Netzwerk direkt erreichbar. Von außen nur über Tailscale!

---

## Log2RAM (v2.2)

- Status: Aktiv ✅
- RAM-Disk Größe: 128M
- Mountpoint: /var/log
- Effekt: 80-90% weniger SSD-Schreibzyklen
- RAM-Auslastung: ~52% (ca. 66MB von 128MB)
- Installation: /etc/log2ram.conf
- Service: log2ram.service (enabled, active)

**Vorteile:**
- Massiv verlängerte SSD-Lebensdauer
- Schnellere Log-Zugriffe
- Automatische Log-Rotation in RAM

---

## Backup-System (v2.2)

### Automatisches Nextcloud-Backup

- Script: `/home/dave/Desktop/scripts/nextcloud_backup.sh`
- Backup-Verzeichnis: `/home/dave/Desktop/backups/`
- Intervall: Wöchentlich (Sonntag 2:00 Uhr)
- Rotation: 7 Tage (ältere Backups werden automatisch gelöscht)

**Was wird gesichert:**
- ✅ Datenbank (MariaDB Dump)
- ✅ Config-Dateien
- ✅ docker-compose.yml
- ✅ mariadb-config/my.cnf (NEU v2.3!)
- ✅ Komprimiert als .tar.gz
- ✅ Log-Datei mit Backup-Historie

**NICHT gesichert:**
- ❌ User-Dateien (Bilder, Videos) → Diese werden durch Windows Desktop Client synchronisiert

**Backup manuell starten:**
```bash
/home/dave/Desktop/scripts/nextcloud_backup.sh
```

---

## Foto-Management (v2.2)

### Scripts-Übersicht

Alle Scripts liegen in: `/home/dave/Desktop/scripts/`

#### 1. Spam-Filter Script
**Script:** `filter_spam_photos.sh`

**Funktion:**
- Findet "Guten Morgen"-Bilder, Memes, WhatsApp-Weiterleitungen
- Analysiert: Dateigröße, EXIF-Daten, Bildformat, Dateinamen
- Verschiebt verdächtige Bilder nach `/Bilder/_Zu_Pruefen/`
- Score-basiert: Score ≥2 = verdächtig

**Erkennungsmerkmale:**
- Dateigröße < 100KB
- Keine EXIF-Daten (kein Camera Model)
- Quadratisches Format (1:1)
- Screenshot-/WhatsApp-Namen

**Ausführen:**
```bash
/home/dave/Desktop/scripts/filter_spam_photos.sh
```

**Letzter Lauf:** 14. Oktober 2025 - 3.727 Bilder verschoben

---

#### 2. Jahr-Sortierung Script
**Script:** `sort_photos_by_year.sh`

**Funktion:**
- Sortiert Bilder im Hauptordner nach Jahren
- Geschwindigkeit: ~15 Minuten für 43.000 Dateien
- Sortierung nach: Dateiname (z.B. 20140517_xxx.jpg → 2014/)

**Nutzung:**
- Für neue unsortierte Bilder im Hauptordner
- Läuft vor der Monats-Sortierung

**Ausführen:**
```bash
/home/dave/Desktop/scripts/sort_photos_by_year.sh
```

---

#### 3. Monats-Sortierung Script
**Script:** `sort_photos_by_months.sh`

**Funktion:**
- Sortiert Bilder nach Jahren UND Monaten
- Struktur: `/2024/` → `/2024/01-Januar/`, `/2024/02-Februar/`, etc.
- Löscht automatisch leere Jahr-Ordner
- Geschwindigkeit: ~15-20 Minuten

**Sortierlogik:**
1. Dateiname (20240315_xxx.jpg → März 2024)
2. EXIF-Daten als Fallback
3. Datei-Änderungsdatum als letzter Fallback

**Ausführen:**
```bash
/home/dave/Desktop/scripts/sort_photos_by_months.sh
```

---

### Aktueller Stand der Foto-Sammlung

**Struktur:**
```
/Bilder/
├── 2014/
│   ├── 01-Januar/
│   ├── 02-Februar/
│   └── ...
├── 2015/
│   ├── 01-Januar/
│   └── ...
├── _Zu_Pruefen/     # Spam-Bilder zur manuellen Prüfung
└── Unbekannt/       # Bilder ohne erkennbares Datum
```

**Statistik:**
- ✅ ~47.000 Bilder verwaltet
- ✅ Nach Jahren sortiert (2014-2025)
- ✅ Nach Monaten sortiert
- ✅ 3.727 Spam-Bilder gefiltert
- ✅ Leere Ordner automatisch gelöscht

**Best Practice für neue Uploads:**
- Direkt in richtigen Monat hochladen: `/Bilder/2025/10-Oktober/`
- Vermeiden: Bilder direkt in `/Bilder/` (Hauptordner)

---

## Cronjobs

### Aktive Cronjobs (dave User)

```bash
# ============================================
# CLEANUP
# ============================================
# Nextcloud Backup-Ordner löschen (einmalig, 17. Oktober 2025, 10:00 Uhr)
0 10 17 10 * DISPLAY=:0 notify-send 'Nextcloud Backup löschen' 'rm -rf /home/dave/nextcloud/data.backup'

# ============================================
# BACKUPS
# ============================================
# Nextcloud Backup (wöchentlich Sonntag 2:00 Uhr)
0 2 * * 0 /home/dave/Desktop/scripts/nextcloud_backup.sh

# ============================================
# SYSTEM UPDATES
# ============================================
# System-Updates (wöchentlich Sonntag 3:00 Uhr)
0 3 * * 0 /home/dave/Desktop/scripts/updates.sh

# ============================================
# NEXTCLOUD
# ============================================
# Nextcloud Background-Tasks (alle 5 Minuten)
*/5 * * * * docker exec -u www-data nextcloud-app-1 php cron.php
```

### Cronjobs verwalten

```bash
# Alle Cronjobs anzeigen
crontab -l

# Cronjobs bearbeiten
crontab -e

# Alle Cronjobs löschen
crontab -r
```

---

## Automatisches Update-Script

Pfad: `/home/dave/Desktop/scripts/updates.sh`

Das Script führt automatisch aus:
1. Raspberry Pi OS Updates
2. Pi-hole Updates
3. Docker Image Updates (Nextcloud + MariaDB)
4. Nextcloud Container Neustart
5. Tailscale Updates

Wird jeden Sonntag um 3:00 Uhr via Cronjob ausgeführt.

---

## GNOME Keyring

- Konfiguration: Ohne Passwort (wegen Auto-Login)
- Keine Abfrage beim Start

---

## Redis Cache - NICHT EMPFOHLEN (v2.3)

**Status:** Versuch in v2.3, aber wieder entfernt

**Warum entfernt:**
- ❌ PHP Session-Handler Konflikte
- ❌ Login funktionierte nicht
- ❌ Zusätzliche Komplexität ohne stabilen Mehrwert
- ❌ Debugging aufwändig

**Entscheidung:**
- ✅ APCu + MariaDB-Tuning ist bereits exzellent
- ✅ 57% Performance-Gewinn ohne Redis
- ✅ Stabil und zuverlässig
- ✅ Einfacher zu warten

**Falls du Redis später nochmal probieren willst:**
- Erfordert zusätzliche PHP Session-Handler Konfiguration
- Benötigt ENV-Variablen: `PHP_SESSION_HANDLER` und `PHP_SESSION_SAVE_PATH`
- Nur empfehlenswert wenn du Erfahrung mit Redis hast

---

## 📝 Changelog

### v2.3 (14. Oktober 2025)

**MariaDB Performance-Tuning:**
- ✅ Custom my.cnf erstellt (`/home/dave/nextcloud/mariadb-config/my.cnf`)
- ✅ InnoDB Buffer Pool: 128 MB → **1600 MB** (13x größer!)
- ✅ Query Cache aktiviert: **128 MB** (war OFF)
- ✅ Temp Tables: 16 MB → **128 MB** (8x größer)
- ✅ Database Indices optimiert
- ✅ Performance: **38,6 Sek** für 474k Dateien (57% schneller!)

**Redis-Versuch:**
- ❌ Redis für Sessions: Login-Probleme (PHP Session-Handler)
- ✅ Entscheidung: Redis komplett entfernt
- ✅ APCu + MariaDB-Tuning reicht völlig aus
- ℹ️  Dokumentiert als "nicht empfohlen"

**System-Status:**
- ✅ Nextcloud läuft stabil
- ✅ Login funktioniert einwandfrei
- ✅ Performance exzellent (57% schneller als v2.2)
- ✅ RAM-Auslastung: ~1,5 GB / 8 GB (81% frei!)
- ✅ Nur 2 Container (app + db) - schlank & stabil

**Dokumentation:**
- ✅ pi-config auf v2.3 aktualisiert
- ✅ MariaDB-Tuning dokumentiert
- ✅ Redis als "nicht empfohlen" markiert
- ✅ Troubleshooting erweitert

### v2.2 (14. Oktober 2025)

**Foto-Management:**
- ✅ Bilder-Ordner Problem gelöst (43.345 Bilder)
- ✅ Jahr-Sortier-Script erstellt und getestet (~15 Min Laufzeit)
- ✅ Spam-Filter-Script erstellt und ausgeführt (3.727 Bilder gefiltert)
- ✅ Monats-Sortier-Script erstellt und ausgeführt
- ✅ Automatisches Löschen leerer Ordner
- ✅ Drei Foto-Management Scripts verfügbar

**Backup & Sicherheit:**
- ✅ Log2RAM installiert und aktiviert (128MB)
- ✅ SSD-Schreibzyklen um 80-90% reduziert
- ✅ Automatisches Nextcloud-Backup-Script erstellt
- ✅ Wöchentliche Backups (Sonntag 2:00 Uhr)
- ✅ 7-Tage Backup-Rotation

**Nextcloud Optimierungen:**
- ✅ Preview-Generierung optimiert (2048x2048, JPEG 60)
- ✅ Windows Desktop Client Sync getestet (<20 Sek!)
- ✅ Keine Konfliktdateien vorhanden
- ✅ Bi-direktionale Sync funktioniert perfekt

**System:**
- ✅ Crontab aufgeräumt und strukturiert
- ✅ System-Neustart durchgeführt (neuer Kernel aktiv)
- ✅ Dokumentation aktualisiert (v2.2)
- ✅ Alle Scripts dokumentiert und getestet

### v2.1 (13. Oktober 2025)

**Performance-Optimierungen:**
- ✅ APCu Memory Cache aktiviert (3-5x schnellere Nextcloud)
- ✅ PHP Memory Limit auf 512M erhöht
- ✅ PHP Upload Limit auf 10G erhöht
- ✅ Nextcloud Cron-Job eingerichtet (alle 5 Minuten)
- ✅ Cron in Nextcloud Web-Interface aktiviert

**Security:**
- ✅ UFW Firewall aktiviert und konfiguriert
- ✅ Nextcloud Port 8080 nur aus lokalem Netzwerk erreichbar

**Nextcloud Client Setup:**
- ✅ Windows Desktop Client auf Stand-PC installiert
- ✅ Verbindung über lokale IP (192.168.2.54:8080)
- ✅ Automatische Synchronisation aktiv
- ✅ Ordnerstruktur bereinigt: "Photos" → "Handy" (44.000 Bilder)

**SSH Verbesserungen:**
- ✅ SSH Config eingerichtet mit Alias "pi"
- ✅ Ed25519 Key hinterlegt (passwortlos)
- ✅ MOTD deaktiviert (.hushlogin)
- ✅ Keine "yes" Abfrage mehr (StrictHostKeyChecking no)

**Tailscale DNS Problem gelöst:**
- ✅ "Use Tailscale DNS" auf Android deaktiviert
- ✅ Android Auto-Upload Problem identifiziert (Xiaomi MIUI)
- ✅ Workaround: Windows Desktop Client für zuverlässige Sync

**Dokumentation:**
- ✅ Systemkonfiguration aktualisiert auf v2.1
- ✅ Cronjobs übersichtlich kommentiert
- ✅ TODO-Liste für nächste Optimierungen erstellt

### v2.0 (12. Oktober 2025)

- Initial Setup

---

## ⚠️ WICHTIGE TROUBLESHOOTING-HINWEISE

### DNS-Probleme

- NetworkManager überschreibt DNS → Änderungen mit nmcli vornehmen
- NIEMALS dhcpcd verwenden (existiert nicht auf diesem System)
- /etc/resolv.conf ist gesperrt mit chattr +i
- Bei DNS-Schleife: Prüfe ob Pi sich selbst (127.0.0.1) oder Router (192.168.2.1) nutzt

### Pi-hole spezifisch

- Neue Pi-hole Version nutzt pihole.toml (nicht mehr setupVars.conf)
- Konfigurationsänderungen über Web-Interface oder direkt in pihole.toml
- DNS-Settings prüfen: `sudo cat /etc/pihole/pihole.toml | grep -A 3 "upstreams"`

### Tailscale & DNS

- Tailscale MUSS mit --accept-dns=false laufen
- "Use Tailscale DNS" in Android App MUSS deaktiviert sein
- Im Heimnetzwerk Tailscale besser ausschalten (spart Akku, schnellere Verbindung)

### Nextcloud spezifisch

- **Datenverzeichnis**: Alle User-Dateien liegen in `/home/dave/Desktop/nextcloud/`
- **Container Namen**: `nextcloud-app-1` und `nextcloud-db-1` (nicht `app` und `db`)
- **.ncdata Datei**: Muss im Datenverzeichnis existieren, sonst Fehlermeldung
- **Berechtigungen**: Datenverzeichnis muss www-data:www-data gehören
- **Port**: 8080 (nicht Standard-80)
- **Zugriff**: Im Heimnetzwerk über 192.168.2.54:8080, unterwegs über 100.103.86.47:8080

### Nextcloud Desktop Client

- **Lokal:** Nutzt http://192.168.2.54:8080
- **Unterwegs:** Tailscale auf PC aktivieren, dann funktioniert Sync über Tailscale IP
- **Problem "Offline":** Client nutzt falsche IP → Konto mit richtiger IP neu einrichten
- **Sync-Test:** Erstelle Testdatei, sollte in <20 Sekunden synchronisiert werden

### Docker & Nextcloud

- Logs prüfen: `docker compose logs -f app`
- Container Status: `docker ps`
- Bei Problemen: `docker compose down && docker compose up -d`
- Niemals Daten direkt in Containern ändern, immer über gemountete Volumes
- docker-compose.yml nicht mit `version: '3'` Zeile verwenden (obsolet)

### MariaDB Performance-Tuning (NEU v2.3!)

- **my.cnf Änderungen:** Erfordern Container-Neustart
- **InnoDB Buffer Pool:** Nicht größer als 80% des freien RAMs setzen
- **Query Cache:** Bei Problemen auf 64M reduzieren
- **Container startet nicht:** Logs prüfen (`docker compose logs db`)
- **Syntax-Fehler in my.cnf:** Datei prüfen, Container ohne Config starten
- **Performance-Check:** `docker exec nextcloud-db-1 mysql -u root -p"Elaine+Dave021222" -e "SHOW VARIABLES LIKE 'innodb_buffer_pool_size';"`

### Log2RAM

- Status prüfen: `systemctl status log2ram`
- RAM-Disk prüfen: `df -h | grep log2ram`
- Bei Problemen: `sudo systemctl restart log2ram`
- Logs landen in: /var/log (im RAM!)

### Backup-System

- Backups prüfen: `ls -lh /home/dave/Desktop/backups/`
- Log-Datei: `/home/dave/Desktop/backups/backup.log`
- Manueller Test: `/home/dave/Desktop/scripts/nextcloud_backup.sh`
- Restore: Backup entpacken und Datenbank importieren

### Foto-Sortierung

- **Bilder landen im Hauptordner:** Script manuell starten
- **Beste Praxis:** Neue Bilder direkt in richtigen Jahr-Ordner hochladen
- **Berechtigungen:** Alle Ordner müssen www-data:www-data gehören
- **Nach Sortierung:** Nextcloud-Scan durchführen

### Redis-Probleme (v2.3 Lessons Learned)

- **Login hängt:** Wahrscheinlich Session-Handler Problem
- **PHP Session-Handler:** Muss auf "files" stehen, nicht "redis"
- **Lösung:** Redis aus config.php entfernen, Container ohne Redis starten
- **Prüfen:** `docker exec nextcloud-app-1 php -i | grep session.save_handler`
- **Empfehlung:** Redis nur nutzen wenn du Erfahrung damit hast!

### Nach Systemänderungen (Klonen, Updates etc.)

- resolv.conf prüfen: `cat /etc/resolv.conf`
- NetworkManager DNS-Settings prüfen: `nmcli connection show "preconfigured"`
- Pi-hole Status: `pihole status`
- Tailscale Status: `tailscale status`
- Docker Status: `docker ps`
- Nextcloud Status: `docker compose logs app | tail -30`
- Log2RAM Status: `systemctl status log2ram`
- MariaDB Config: `docker exec nextcloud-db-1 cat /etc/mysql/conf.d/custom.cnf`

### Bekannte Lösungen

**Problem:** DNS-Schleife nach Klonen  
**Lösung:** /etc/resolv.conf manuell setzen, mit chattr +i sperren, nmcli DNS konfigurieren

**Problem:** Schlüsselbund-Abfrage  
**Lösung:** `rm -rf ~/.local/share/keyrings/*`, Neustart, leeres Passwort setzen

**Problem:** Geräte kommen nicht ins Internet trotz Pi-hole  
**Lösung:** Auf Mobilgeräten "Privates DNS" ausschalten (Android) oder DNS manuell setzen (iOS)

**Problem:** Pi-hole Konfiguration finden  
**Lösung:** Neuere Versionen nutzen /etc/pihole/pihole.toml statt setupVars.conf

**Problem:** Nextcloud "Zugriff über nicht vertrauenswürdige Domain"  
**Lösung:** `docker exec -u www-data nextcloud-app-1 php occ config:system:set trusted_domains X --value=IP_ADRESSE`

**Problem:** Nextcloud "Datenverzeichnis ist ungültig"  
**Lösung:** Prüfe ob .ncdata Datei im Datenverzeichnis existiert und korrekte Berechtigungen hat

**Problem:** Nextcloud-Dateien nicht in Desktop-Ordner sichtbar  
**Lösung:** Prüfe docker-compose.yml Volume-Mapping und Berechtigungen (www-data:www-data)

**Problem:** Docker Container startet nicht  
**Lösung:** Logs prüfen mit `docker compose logs app`, oft Berechtigungs- oder Port-Probleme

**Problem:** Android Auto-Upload startet nicht (Xiaomi/Poco)  
**Lösung:** MIUI hat aggressive Batterie-Optimierung. Workaround: Manueller Upload oder Windows Desktop Client nutzen

**Problem:** Nextcloud Desktop Client zeigt "offline"  
**Lösung:** Prüfe ob richtige IP konfiguriert ist (lokal: 192.168.2.54:8080, nicht Tailscale IP). Ggf. Konto neu einrichten.

**Problem:** Bilder-Ordner in Nextcloud Web-Interface öffnet nicht  
**Lösung:** Zu viele Dateien im Ordner (>40.000). Lösung: Bilder in Unterordner sortieren (nach Jahren/Monaten)

**Problem:** Nextcloud Sync sehr langsam  
**Lösung:** Preview-Generierung optimieren, APCu Cache prüfen, MariaDB-Tuning prüfen, Log2RAM aktiv?

**Problem:** Log2RAM startet nicht nach Installation  
**Lösung:** System-Neustart erforderlich! `sudo reboot`

**Problem:** Backup-Script schlägt fehl  
**Lösung:** Wartungsmodus prüfen, Docker Container Status prüfen, Berechtigungen im Backup-Verzeichnis

**Problem:** MariaDB Container startet nicht nach my.cnf Änderung  
**Lösung:** Syntax in my.cnf prüfen, Logs checken: `docker compose logs db`

**Problem:** Nextcloud Login hängt nach Config-Änderungen  
**Lösung:** Browser-Cache komplett leeren (Cookies + Cache), Inkognito-Modus testen

**Problem:** Redis verursacht Login-Probleme  
**Lösung:** Redis aus config entfernen, Container ohne Redis neu starten, PHP Session-Handler prüfen

---

## 🎯 Nächste Schritte (TODO)

### 📱 Punkt 3: Client-Setup vervollständigen (Optional)

- [ ] Windows Laptop: Desktop Client mit beiden IPs (lokal + Tailscale)
- [ ] Android: Auto-Upload akzeptieren als manuellen Prozess

### 🔧 Punkt 4: Weitere Optimierungen (Optional, später)

- [ ] Externes Backup auf USB-HDD einrichten
- [ ] HTTPS mit Nginx Reverse Proxy (für Zugriff von überall ohne Tailscale)
- [ ] Monitoring Dashboard (z.B. Grafana)
- [ ] Collabora/OnlyOffice für Office-Dokumente
- [ ] Preview-Generation für bestehende Fotos im Hintergrund

### 🧹 Maintenance (Laufend)

- [ ] Nach 17. Oktober: Cleanup-Cronjob aus Crontab entfernen
- [ ] Backup-System monatlich testen (Restore-Test)
- [ ] Foto-Sortierung: Neue Uploads direkt in richtige Jahr-Ordner
- [ ] MariaDB Performance gelegentlich prüfen

---

**Letzte Aktualisierung:** 14. Oktober 2025, 22:00 Uhr  
**Version:** v2.3  
**Status:** ✅ Produktiv & Hochoptimiert (57% schneller!)  
**Nächste geplante Überprüfung:** Nach Laptop-Client Setup oder bei Bedarf
