<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# Sophos DHCP Toolkit
[![CI](https://github.com/uMax-Cyber/DHCPGuard/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/DHCPGuard/actions/workflows/ci.yml)


![Demo](screenshots/demo.svg)
Python toolkit for managing and diagnosing DHCP on Sophos Firewall via XML API. Includes scope discovery, lease analysis, conflict detection, and the critical "static lease in wrong scope" pattern that causes silent DHCP failures.

## Key Discovery: Silent DHCP Denial

Sophos with `ConflictDetection=Enable` **silently ignores** DHCP DISCOVER from a device that has a static lease in a DIFFERENT scope's configuration. No NAK, no error — just silence. The device loops for hours.

**Detection**: Compare static leases across ALL scopes. If a MAC has a static reservation in scope-A but sends DISCOVER on scope-B's interface, the server will not respond.

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/sophos_api.py` | Generic XML API wrapper (Get/Set/Filter) |
| `scripts/dhcp_scope_audit.py` | Dump all scopes with pools, statics, utilization |
| `scripts/lease_analyzer.py` | Parse syslog for lease events, detect anomalies |

## API Gotchas (from real deployment)

- Valid Get modules: `DHCP`, `DHCPServer`, `Interface`, `IPHost`, `FirewallRule`, `DHCPRelay`
- **NOT valid** (529 error): `Syslog`, `LogSettings`, `SystemSettings`, `VPNSSL`, `Route` — don't retry these
- `DHCPServer` returns ALL scopes with pools, statics, DNS, gateway, lease times
- `Interface` returns all VLAN gateway IPs — use for scope-to-VLAN mapping
- REST API v2 (`/console/api/v2/`) may be disabled even on recent SFOS versions

## License
MIT

## 📬 Contact

Questions? Reach out: **[allumaxmail@gmail.com](mailto:allumaxmail@gmail.com)**

---

<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>
