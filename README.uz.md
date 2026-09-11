<div align="center">

[![English](https://img.shields.io/badge/README-English-blue)](README.md)
[![Русский](https://img.shields.io/badge/README-Русский-red)](README.ru.md)
[![Oʻzbekcha](https://img.shields.io/badge/README-Oʻzbekcha-green)](README.uz.md)

</div>

# Sophos DHCP vositasi

[![CI](https://github.com/uMax-Cyber/DHCPGuard/actions/workflows/ci.yml/badge.svg)](https://github.com/uMax-Cyber/DHCPGuard/actions/workflows/ci.yml)

![Demo](screenshots/demo.svg)

Sophos Firewall da DHCP ni boshqarish va tashxislash uchun Python vositasi — XML API orqali ishlaydi. Scope larni aniqlash, ijaralarni (lease) tahlil qilish, konfliktlarni aniqlash hamda jimgina DHCP ishdan chiqishiga olib keladigan «notoʻgʻri scopedagi statik ijarа» shakllanishini aniqlashni oʻz ichiga oladi.

## Asosiy kashfiyot: jimgina DHCP rad etilishi

`ConflictDetection=Enable` bilan ishlaydigan Sophos, boshqa scope konfiguratsiyasida statik ijarasi bor qurilmaning DHCP DISCOVER soʻrovini **jimgina e'tiborsiz qoldiradi**. NAK yoʻq, xato yoʻq — faqat jimlik. Qurilmalar soatlab aylanaveradi.

**Aniqlash usuli**: barcha scope lardagi statik ijaralarni solishtiring. Agar MAC manzilning scope-A dagi statik rezervatsiyasi boʻlsa, lekin DISCOVER scope-B interfeysiga kelsa — server javob bermaydi.

## Skriptlar

| Skript | Vazifasi |
|--------|----------|
| `scripts/sophos_api.py` | Universal XML API oʻrami (Get/Set/Filter) |
| `scripts/dhcp_scope_audit.py` | Barcha scope larni chiqarish: poolar, statiklar, band qilinganlik |
| `scripts/lease_analyzer.py` | Syslog dan lease hodisalarini ajratib olish, anomaliyalarni aniqlash |

## API ning nozik joylari (real joylashtirishdan)

- Haqiqiy Get modullari: `DHCP`, `DHCPServer`, `Interface`, `IPHost`, `FirewallRule`, `DHCPRelay`
- **Haqiqiy EMAS** (529 xatosi): `Syslog`, `LogSettings`, `SystemSettings`, `VPNSSL`, `Route` — bularni qayta soʻramang
- `DHCPServer` barcha scope larni poolar, statiklar, DNS, gateway va ijarа muddatlari bilan qaytaradi
- `Interface` barcha VLAN gateway IP larini qaytaradi — scope ↔ VLAN moslash uchun ishlating
- REST API v2 (`/console/api/v2/`) SFOS ning yangi versiyalarida ham oʻchirilgan boʻlishi mumkin

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
