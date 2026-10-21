"""Client Cisco Catalyst 9500 (IOS-XE RESTCONF)."""
from __future__ import annotations

from ..config import DeviceConfig, Settings
from ..mocks import fixtures
from .base import BaseClient, DeviceError

_RESTCONF_HEADERS = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json",
}

class Catalyst9500Client:
    def __init__(self, cfg: DeviceConfig, settings: Settings) -> None:
        self._cfg = cfg
        self._settings = settings

    def _client(self) -> BaseClient:
        if not self._cfg.configured:
            raise DeviceError(
                "Catalyst 9500 belum dikonfigurasi. Set CATALYST9500_HOST, "
                "CATALYST9500_USERNAME, CATALYST9500_PASSWORD, atau NETOPS_MOCK=true."
            )
        c = BaseClient(
            self._cfg.host or "",
            tls_verify=self._settings.tls_verify,
            timeout=self._settings.http_timeout,
            headers=_RESTCONF_HEADERS,
        )
        c._client.auth = (self._cfg.username or "", self._cfg.password or "")
        return c

    def interfaces(self) -> list[dict]:
        if self._settings.mock:
            return fixtures.CATALYST9500_INTERFACES
        with self._client() as c:
            data = c.get("/restconf/data/ietf-interfaces:interfaces-state")
            ifaces = data.get("ietf-interfaces:interfaces-state", {}).get("interface", [])
            return [
                {
                    "name": i.get("name"),
                    "admin": i.get("admin-status"),
                    "oper": i.get("oper-status"),
                }
                for i in ifaces
            ]

    def version(self) -> dict:
        if self._settings.mock:
            return fixtures.CATALYST9500_VERSION
        with self._client() as c:
            data = c.get("/restconf/data/Cisco-IOS-XE-native:native/version")
            return data
