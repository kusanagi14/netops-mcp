"""HTTP client dasar yang dipakai semua platform."""
from __future__ import annotations

from typing import Any

class DeviceError(RuntimeError):
    """Error terkait komunikasi ke perangkat, dengan pesan yang mudah dibaca."""

class BaseClient:
    def __init__(
        self,
        base_url: str,
        *,
        tls_verify: bool = True,
        timeout: float = 30.0,
        headers: dict[str, str] | None = None,
    ) -> None:
        import httpx

        self._base_url = base_url.rstrip("/")
        self._client = httpx.Client(
            base_url=self._base_url,
            verify=tls_verify,
            timeout=timeout,
            headers=headers or {},
        )

    def request(self, method: str, path: str, **kwargs: Any) -> Any:
        import httpx

        try:
            resp = self._client.request(method, path, **kwargs)
            resp.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise DeviceError(
                f"{self._base_url} mengembalikan HTTP {exc.response.status_code}: "
                f"{exc.response.text[:300]}"
            ) from exc
        except httpx.RequestError as exc:
            raise DeviceError(
                f"Gagal menghubungi {self._base_url}: {exc.__class__.__name__}: {exc}"
            ) from exc

        ctype = resp.headers.get("content-type", "")
        if "json" in ctype:
            return resp.json()
        return resp.text

    def get(self, path: str, **kwargs: Any) -> Any:
        return self.request("GET", path, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "BaseClient":
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()
