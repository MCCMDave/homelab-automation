# Homelab Automation

## About

Production-ready automation scripts for my Raspberry Pi 5 homelab infrastructure. This repository contains monitoring, maintenance, and operational scripts that keep my self-hosted services running smoothly.

## Infrastructure Overview

**Hardware:**
- Raspberry Pi 5 (8GB RAM)
- Running Raspberry Pi OS (Debian-based)

**Services:**
- **Nextcloud:** Self-hosted cloud storage and productivity suite
- **Pi-hole:** Network-wide ad blocking and DNS server
- **MariaDB:** Database backend for Nextcloud
- **Tailscale:** Secure mesh VPN for remote access

**Network:**
- Local access: 192.168.2.54
- Remote access via Tailscale VPN
- Docker containerization for service isolation

## Current Projects

### Monitoring Scripts (Planned)

**Purpose:** Automated health monitoring for critical services

**Planned Features:**
- Service uptime tracking
- Resource usage monitoring (CPU, RAM, disk)
- Automatic alerting for critical conditions
- Log analysis and reporting
- Performance metrics collection

**Status:** In development - moving from testing to production

### Backup Automation (Planned)

**Purpose:** Automated backup management for Nextcloud data

**Planned Features:**
- Scheduled Nextcloud data backups
- Database backup automation
- Off-site backup verification
- Retention policy management

**Status:** Design phase

### Maintenance Scripts (Planned)

**Purpose:** Routine maintenance automation

**Planned Features:**
- Automated system updates
- Log rotation management
- Disk space monitoring
- Service health checks

**Status:** Planning phase

## Learning Context

This homelab serves multiple purposes:
- **Practical Learning Lab:** Hands-on experience with cloud infrastructure concepts during my IHK Cloud IT Administrator certification
- **Portfolio Development:** Demonstrating real-world system administration and automation skills
- **Service Independence:** Self-hosted alternatives to commercial cloud services for privacy and learning

## Technologies & Skills

**Current Stack:**
- Docker & Docker Compose
- Linux system administration (Debian/Raspberry Pi OS)
- Bash scripting
- Python automation
- Networking (DNS, VPN, port forwarding)
- Version control (Git)

**Learning Focus:**
- Infrastructure as Code
- Monitoring and observability
- Backup and disaster recovery
- Security best practices
- Performance optimization

## Development Approach

**Workflow:**
1. Develop and test scripts on Windows WSL environment
2. Test in safe environment before production deployment
3. Deploy to Raspberry Pi production environment
4. Monitor and iterate based on real-world usage

**Documentation:**
- All production scripts include inline documentation
- Setup guides maintained separately in Nextcloud
- Configuration files version-controlled

## Project Principles

- **Stability First:** Production environment remains stable; experimental work stays in development
- **Documentation:** Comprehensive documentation for reproducibility
- **Incremental:** Small, tested changes over large rewrites
- **Learning-Oriented:** Understanding over quick fixes

## Performance Achievements

Current homelab optimization results:
- System runs 57% faster than initial setup
- MariaDB efficiently handles 500,000+ files
- Stable operation with minimal manual intervention

## Future Roadmap

**Short Term:**
- Migrate log monitoring script from development to production
- Implement automated service health checks
- Set up basic alerting system

**Medium Term:**
- Expand to Oracle Cloud Infrastructure (OCI) for additional capacity
- Implement comprehensive backup automation
- Add performance dashboards

**Long Term:**
- Full infrastructure as code implementation
- Advanced monitoring with visualization
- Multi-node orchestration

## Related Projects

For Python learning projects and initial script development, see my [python-learning](https://github.com/MCCMDave/python-learning) repository.

## Contact

For questions about the setup or collaboration opportunities, feel free to reach out via GitHub.

---

**Last Updated:** November 2025  
**Training Program:** Cloud IT Administrator (IHK) - Module 2 of 4
