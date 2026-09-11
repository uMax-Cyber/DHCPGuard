# DHCP Scope Audit Procedure

## Why DHCPServer Module is Critical
The `Interface` module does NOT show DHCP scope configurations. Only `DHCPServer` returns the full picture: pool ranges, static reservations, DNS servers, gateway assignments, lease times.

## Audit Checklist
1. **Pool utilization**: unique IPs issued (from logs) vs pool capacity
2. **Static lease scope match**: every MAC with a static reservation should be in the correct VLAN/scope
3. **Cross-scope MACs**: a MAC in multiple scopes = misconfiguration
4. **Lease time**: appropriate for device turnover (2-4h for dynamic environments)
5. **ConflictDetection**: enabled scopes silently deny cross-scope statics

## The Silent Denial Pattern
```
Device MAC: aa:bb:cc:dd:ee:ff
Static lease in scope-A: 10.0.1.50
Device sends DISCOVER on scope-B interface
→ Sophos sees static lease in wrong scope
→ ConflictDetection triggers
→ NO RESPONSE (not even NAK)
→ Device loops "connecting..." for hours
```
