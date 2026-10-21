"""Client Cisco Catalyst Center / DNA Center (Intent API)."""
from __future__ import annotations

from ..config import DeviceConfig, Settings
from ..mocks import fixtures
from .base import BaseClient, DeviceError

class CatalystCenterClient:
    def __init__(self, cfg: DeviceConfig, settings: Settings) -> None:
        self._cfg = cfg
        self._settings = settings

    def _authed_client(self) -> BaseClient:
        if not self._cfg.configured:
            raise DeviceError(
                "Catalyst Center belum dikonfigurasi. Set CATALYST_CENTER_HOST, "
                "CATALYST_CENTER_USERNAME, CATALYST_CENTER_PASSWORD, atau NETOPS_MOCK=true."
            )
        auth = BaseClient(
            self._cfg.host or "",
            tls_verify=self._settings.tls_verify,
            timeout=self._settings.http_timeout,
        )
        auth._client.auth = (self._cfg.username or "", self._cfg.password or "")
        token_resp = auth.request("POST", "/dna/system/api/v1/auth/token")
        auth.close()
        token = token_resp.get("Token") if isinstance(token_resp, dict) else None
        if not token:
            raise DeviceError("Gagal memperoleh X-Auth-Token dari Catalyst Center.")
        return BaseClient(
            self._cfg.host or "",
            tls_verify=self._settings.tls_verify,
            timeout=self._settings.http_timeout,
            headers={"X-Auth-Token": token},
        )

    def devices(self) -> list[dict]:
        if self._settings.mock:
            return fixtures.CATALYST_CENTER_DEVICES
        with self._authed_client() as c:
            data = c.get("/dna/intent/api/v1/network-device")
            return data.get("response", [])

    def network_health(self) -> dict:
        if self._settings.mock:
            return fixtures.CATALYST_CENTER_HEALTH
        with self._authed_client() as c:
            data = c.get("/dna/intent/api/v1/network-health")
            return data.get("response", data)
