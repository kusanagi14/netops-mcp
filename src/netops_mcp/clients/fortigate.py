"""Client FortiGate (FortiOS REST API)."""
from __future__ import annotations

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
            headers={"Authorization": f"Bearer {self._cfg.api_token}"},
        )

    def system_status(self) -> dict:
        if self._settings.mock:
            return fixtures.FORTIGATE_SYSTEM_STATUS
        with self._client() as c:
            data = c.get("/api/v2/monitor/system/status")
            return data.get("results", data)

    def firewall_policies(self) -> list[dict]:
        if self._settings.mock:
            return fixtures.FORTIGATE_FIREWALL_POLICIES
        with self._client() as c:
            data = c.get("/api/v2/cmdb/firewall/policy")
            return data.get("results", [])

    def interfaces(self) -> list[dict]:
        if self._settings.mock:
            return fixtures.FORTIGATE_INTERFACES
        with self._client() as c:
            data = c.get("/api/v2/monitor/system/interface")
            results = data.get("results", {})
            if isinstance(results, dict):
                return [{"name": k, **v} for k, v in results.items()]
            return results
