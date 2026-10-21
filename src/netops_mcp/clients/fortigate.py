"""Client FortiGate (FortiOS REST API). Semua operasi READ-ONLY (monitoring & diagnose)."""
from __future__ import annotations

from typing import Any

from ..config import DeviceConfig, Settings
from ..mocks import fixtures
from .base import BaseClient, DeviceError


class FortiGateClient:
    def __init__(self, cfg: DeviceConfig, settings: Settings) -> None:
        self._cfg = cfg
        self._settings = settings

    def _client(self) -> BaseClient:
        if not self._cfg.configured:
            raise DeviceError(
                "FortiGate belum dikonfigurasi. Set FORTIGATE_HOST & FORTIGATE_API_TOKEN, "
                "atau jalankan dengan NETOPS_MOCK=true."
            )
        return BaseClient(
            self._cfg.host or "",
            tls_verify=self._settings.tls_verify,
            timeout=self._settings.http_timeout,
            headers={"Authorization": "Bearer " + str(self._cfg.api_token)},
        )

    def _monitor(self, path: str, params: dict | None = None) -> Any:
        with self._client() as c:
            data = c.get("/api/v2/monitor/" + path.lstrip("/"), params=params or {})
            if isinstance(data, dict) and "results" in data:
                return data["results"]
            return data

    def _cmdb(self, path: str, params: dict | None = None) -> Any:
        with self._client() as c:
            data = c.get("/api/v2/cmdb/" + path.lstrip("/"), params=params or {})
            if isinstance(data, dict) and "results" in data:
                return data["results"]
            return data

    # ---- dasar ----
    def system_status(self) -> dict:
        if self._settings.mock:
            return fixtures.FORTIGATE_SYSTEM_STATUS
        return self._monitor("system/status")

    def firewall_policies(self) -> list[dict]:
        if self._settings.mock:
            return fixtures.FORTIGATE_FIREWALL_POLICIES
        return self._cmdb("firewall/policy")

    def interfaces(self) -> list[dict]:
        if self._settings.mock:
            return fixtures.FORTIGATE_INTERFACES
        results = self._monitor("system/interface")
        if isinstance(results, dict):
            return [dict({"name": k}, **v) for k, v in results.items()]
        return results

    # ---- diagnose / monitoring (read-only) ----
    def system_resource(self) -> dict:
        if self._settings.mock:
            return fixtures.FORTIGATE_RESOURCE
        return self._monitor("system/resource/usage")

    def ha_status(self) -> Any:
        if self._settings.mock:
            return fixtures.FORTIGATE_HA_STATUS
        return self._monitor("system/ha-statistics")

    def routing_table(self) -> list[dict]:
        if self._settings.mock:
            return fixtures.FORTIGATE_ROUTES
        return self._monitor("router/ipv4")

    def bgp_neighbors(self) -> Any:
        if self._settings.mock:
            return fixtures.FORTIGATE_BGP_NEIGHBORS
        return self._monitor("router/bgp/neighbors")

    def sessions(self, count: int = 20) -> Any:
        if self._settings.mock:
            return fixtures.FORTIGATE_SESSIONS[:count]
        return self._monitor("firewall/session", params={"count": count})

    def vpn_ipsec(self) -> Any:
        if self._settings.mock:
            return fixtures.FORTIGATE_IPSEC
        return self._monitor("vpn/ipsec")

    def vpn_ssl(self) -> Any:
        if self._settings.mock:
            return fixtures.FORTIGATE_SSLVPN
        return self._monitor("vpn/ssl")

    def dhcp_leases(self) -> Any:
        if self._settings.mock:
            return fixtures.FORTIGATE_DHCP
        return self._monitor("system/dhcp")

    def arp_table(self) -> Any:
        if self._settings.mock:
            return fixtures.FORTIGATE_ARP
        return self._monitor("network/arp")

    def policy_hit_count(self) -> list[dict]:
        if self._settings.mock:
            return fixtures.FORTIGATE_POLICY_HITS
        return self._monitor("firewall/policy")

    def dns_health(self) -> Any:
        if self._settings.mock:
            return fixtures.FORTIGATE_DNS
        result = {}
        try:
            result["config"] = self._cmdb("system/dns")
        except DeviceError as exc:
            result["config_error"] = str(exc)
        try:
            result["latency"] = self._monitor("system/dns-latency")
        except DeviceError as exc:
            result["latency_error"] = str(exc)
        return result
