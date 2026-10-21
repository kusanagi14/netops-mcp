"""Konfigurasi terpusat: baca environment variables & setting per-perangkat."""
from __future__ import annotations

import os
from dataclasses import dataclass

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass

def _as_bool(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}

def _clean(value: str | None) -> str | None:
    if value is None:
        return None
    v = value.strip()
    return v or None

@dataclass(frozen=True)
class DeviceConfig:
    name: str
    host: str | None
    api_token: str | None = None
    username: str | None = None
    password: str | None = None

    @property
    def configured(self) -> bool:
        if not self.host:
            return False
        return bool(self.api_token) or bool(self.username and self.password)

@dataclass(frozen=True)
class Settings:
    mock: bool
    tls_verify: bool
    http_timeout: float
    fortigate: DeviceConfig
    catalyst9500: DeviceConfig
    catalyst_center: DeviceConfig

def load_settings() -> Settings:
    mock = _as_bool(os.getenv("NETOPS_MOCK"), default=True)
    tls_verify = _as_bool(os.getenv("NETOPS_TLS_VERIFY"), default=True)
    try:
        http_timeout = float(os.getenv("NETOPS_HTTP_TIMEOUT", "30"))
    except ValueError:
        http_timeout = 30.0

    fortigate = DeviceConfig(
        name="FortiGate",
        host=_clean(os.getenv("FORTIGATE_HOST")),
        api_token=_clean(os.getenv("FORTIGATE_API_TOKEN")),
    )
    catalyst9500 = DeviceConfig(
        name="Catalyst 9500",
        host=_clean(os.getenv("CATALYST9500_HOST")),
        username=_clean(os.getenv("CATALYST9500_USERNAME")),
        password=_clean(os.getenv("CATALYST9500_PASSWORD")),
    )
    catalyst_center = DeviceConfig(
        name="Catalyst Center",
        host=_clean(os.getenv("CATALYST_CENTER_HOST")),
        username=_clean(os.getenv("CATALYST_CENTER_USERNAME")),
        password=_clean(os.getenv("CATALYST_CENTER_PASSWORD")),
    )

    return Settings(
        mock=mock,
        tls_verify=tls_verify,
        http_timeout=http_timeout,
        fortigate=fortigate,
        catalyst9500=catalyst9500,
        catalyst_center=catalyst_center,
    )
