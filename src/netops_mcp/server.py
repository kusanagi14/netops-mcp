"""Entrypoint NetOps MCP Server (transport stdio). Semua tool READ-ONLY."""
from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from .clients.catalyst9500 import Catalyst9500Client
from .clients.catalyst_center import CatalystCenterClient
from .clients.fortigate import FortiGateClient
from .config import load_settings

settings = load_settings()

mcp = FastMCP("netops")

_fortigate = FortiGateClient(settings.fortigate, settings)
_cat9500 = Catalyst9500Client(settings.catalyst9500, settings)
_catcenter = CatalystCenterClient(settings.catalyst_center, settings)


@mcp.tool()
def fortigate_system_status() -> dict:
    """Ambil status sistem FortiGate (hostname, versi firmware, serial, model, uptime)."""
    return _fortigate.system_status()


@mcp.tool()
def fortigate_firewall_policies() -> list[dict]:
    """Daftar kebijakan firewall FortiGate (id, nama, src/dst interface & address, action, status)."""
    return _fortigate.firewall_policies()


@mcp.tool()
def fortigate_interfaces() -> list[dict]:
    """Daftar interface FortiGate beserta status link dan alamat IP-nya."""
    return _fortigate.interfaces()


@mcp.tool()
def fortigate_system_resource() -> dict:
    """Diagnose beban sistem FortiGate: penggunaan CPU, memory, jumlah sesi, uptime, disk."""
    return _fortigate.system_resource()


@mcp.tool()
def fortigate_ha_status() -> Any:
    """Status High Availability FortiGate (role primary/secondary, sinkronisasi antar peer)."""
    return _fortigate.ha_status()


@mcp.tool()
def fortigate_routing_table() -> list[dict]:
    """Tabel routing IPv4 aktif FortiGate (diagnose next-hop dan reachability)."""
    return _fortigate.routing_table()


@mcp.tool()
def fortigate_bgp_neighbors() -> Any:
    """Status BGP neighbor FortiGate (diagnose peering: state, uptime, prefix diterima)."""
    return _fortigate.bgp_neighbors()


@mcp.tool()
def fortigate_sessions(count: int = 20) -> Any:
    """Daftar sesi firewall aktif FortiGate untuk diagnose trafik (batasi dengan count, default 20)."""
    return _fortigate.sessions(count=count)


@mcp.tool()
def fortigate_vpn_ipsec() -> Any:
    """Status tunnel IPsec VPN FortiGate (up/down, RX/TX, remote gateway) untuk diagnose site-to-site VPN."""
    return _fortigate.vpn_ipsec()


@mcp.tool()
def fortigate_vpn_ssl() -> Any:
    """Daftar user SSL-VPN FortiGate yang sedang terhubung."""
    return _fortigate.vpn_ssl()


@mcp.tool()
def fortigate_dhcp_leases() -> Any:
    """Daftar lease DHCP aktif FortiGate (diagnose assignment IP ke client)."""
    return _fortigate.dhcp_leases()


@mcp.tool()
def fortigate_arp_table() -> Any:
    """Tabel ARP FortiGate (diagnose reachability L2/L3)."""
    return _fortigate.arp_table()


@mcp.tool()
def fortigate_policy_hit_count() -> list[dict]:
    """Hit count per firewall policy FortiGate (diagnose policy yang aktif vs tidak terpakai)."""
    return _fortigate.policy_hit_count()


@mcp.tool()
def fortigate_dns_health() -> Any:
    """Status server DNS FortiGate (diagnose resolusi nama)."""
    return _fortigate.dns_health()


@mcp.tool()
def catalyst9500_version() -> dict:
    """Info versi dan identitas Catalyst 9500 (hostname, IOS-XE version, model, serial, uptime)."""
    return _cat9500.version()


@mcp.tool()
def catalyst9500_interfaces() -> list[dict]:
    """Status interface Catalyst 9500 (admin/oper status) via RESTCONF."""
    return _cat9500.interfaces()


@mcp.tool()
def catalyst_center_devices() -> list[dict]:
    """Inventory perangkat yang dikelola Catalyst Center (hostname, IP, platform, versi, reachability, role)."""
    return _catcenter.devices()


@mcp.tool()
def catalyst_center_network_health() -> dict:
    """Ringkasan kesehatan jaringan dari Catalyst Center (skor, jumlah perangkat sehat/tidak)."""
    return _catcenter.network_health()


@mcp.tool()
def netops_status() -> dict[str, Any]:
    """Status konfigurasi NetOps MCP: mode mock dan perangkat mana yang sudah dikonfigurasi."""
    return {
        "mock_mode": settings.mock,
        "tls_verify": settings.tls_verify,
        "devices": {
            "fortigate": settings.fortigate.configured,
            "catalyst9500": settings.catalyst9500.configured,
            "catalyst_center": settings.catalyst_center.configured,
        },
    }


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
