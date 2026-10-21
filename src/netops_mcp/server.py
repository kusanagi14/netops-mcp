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
def catalyst9500_version() -> dict:
    """Info versi & identitas Catalyst 9500 (hostname, IOS-XE version, model, serial, uptime)."""
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
    """Status konfigurasi NetOps MCP: mode mock & perangkat mana yang sudah dikonfigurasi."""
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
