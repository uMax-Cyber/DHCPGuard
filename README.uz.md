<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# Sophos DHCP vositasi

[![CI](https://github.com/uMax-Cyber/DHCPGuard/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/DHCPGuard/actions/workflows/ci.yml)

![Demo](screenshots/demo.svg)

Sophos Firewall dagi DHCP ni XML API orqali boshqarish va tashxislash uchun Python vositasi: scope larni aniqlash, lease tahlili, konfliktlarni aniqlash va — eng muhimi — DHCP ni jimgina ishdan chiqaradigan «statik lease notoʻgʻri scope da» muammosini aniqlash.

## Asosiy topilma: DHCP ning jimgina rad etilishi

`ConflictDetection=Enable` boʻlgan Sophos, boshqa scope konfiguratsiyasida statik lease i bor qurilmaning DHCP DISCOVER soʻroviga javob bermaydi. Na NAK, na xato — shunchaki jimlik. Qurilma soatlab urinaveradi.

**Qanday aniqlanadi:** barcha scope lardagi statik lease larni solishtiring. Agar MAC scope-A da statik rezervatsiyaga ega boʻlsa-yu, DISCOVER scope-B interfeysiga kelsa — server javob bermaydi.

## Skriptlar

| Skript | Vazifasi |
|--------|----------|
| `scripts/sophos_api.py` | XML API bilan ishlash uchun universal yordamchi (Get/Set/Filter) |
| `scripts/dhcp_scope_audit.py` | Barcha scope larni toʻliq chiqarib berish: poolar, statiklar, band qilinganlik |
| `scripts/lease_analyzer.py` | Syslog dan lease hodisalarini ajratib olib, anomalikalarni aniqlash |

## API ning nozik joylari (real joylashtirishdan olingan)

- Ishlaydigan Get modullari: `DHCP`, `DHCPServer`, `Interface`, `IPHost`, `FirewallRule`, `DHCPRelay`
- Ishlamaydiganlari (529 xatosi qaytaradi): `Syslog`, `LogSettings`, `SystemSettings`, `VPNSSL`, `Route` — bularni qayta soʻrashning foydasi yoʻq
- `DHCPServer` barcha scope larni poolari, statiklari, DNS, gateway va lease muddatlari bilan birga qaytaradi
- `Interface` barcha VLAN gateway IP larini beradi — scope va VLAN ni moslashtirishda ishlatiladi
- REST API v2 (`/console/api/v2/`) SFOS ning yangi versiyalarida ham oʻchirilgan holda kelishi mumkin

## Litsenziya
MIT

## 📬 Aloqa

Savollaringiz bormi? Yozing: **[allumaxmail@gmail.com](mailto:allumaxmail@gmail.com)**

---

<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>
