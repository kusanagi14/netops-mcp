"""Self-test cepat: panggil setiap tool tanpa agent."""
from __future__ import annotations

import json
import sys

from .clients.catalyst9500 import Catalyst9500Client
from .clients.catalyst_center import CatalystCenterClient
from .clients.fortigate import FortiGateClient
from .config import load_settings


def main() -> int:
    settings = load_settings()
    fg = FortiGateClient(settings.fortigate, settings)
    c95 = Catalyst9500Client(settings.catalyst9500, settings)
    cc = CatalystCenterClient(settings.catalyst_center, settings)

    checks = {
        "fortigate_system_status": fg.system_status,
        "fortigate_firewall_policies": fg.firewall_policies,
        "fortigate_interfaces": fg.interfaces,
        "fortigate_system_resource": fg.system_resource,
        "fortigate_ha_status": fg.ha_status,
        "fortigate_routing_table": fg.routing_table,
        "fortigate_bgp_neighbors": fg.bgp_neighbors,
        "fortigate_sessions": fg.sessions,
        "fortigate_vpn_ipsec": fg.vpn_ipsec,
        "fortigate_vpn_ssl": fg.vpn_ssl,
        "fortigate_dhcp_leases": fg.dhcp_leases,
        "fortigate_arp_table": fg.arp_table,
        "fortigate_policy_hit_count": fg.policy_hit_count,
        "fortigate_dns_health": fg.dns_health,
        "catalyst9500_version": c95.version,
        "catalyst9500_interfaces": c95.interfaces,
        "catalyst_center_devices": cc.devices,
        "catalyst_center_network_health": cc.network_health,
    }

    print("MOCK_MODE = " + str(settings.mock))
    print("")
    failures = 0
    for name, fn in checks.items():
        try:
            result = fn()
            count = len(result) if isinstance(result, (list, dict)) else "-"
            print("[OK]   " + name + "  (items/keys: " + str(count) + ")")
        except Exception as exc:
            failures += 1
            print("[FAIL] " + name + ": " + exc.__class__.__name__ + ": " + str(exc))

    print("")
    if failures:
        print(str(failures) + " tool gagal (lihat di atas).")
        return 1
    print("Semua tool OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
