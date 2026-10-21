# NetOps MCP Server

MCP server untuk otomasi & AI assistant pada FortiGate, Cisco Catalyst 9500, dan Catalyst Center.
Status awal: READ-ONLY. Lihat docs/ROADMAP.md.

## Instalasi
    python3 -m venv .venv && source .venv/bin/activate
    pip install -e .
    cp .env.example .env && chmod 600 .env

## Uji (mock mode)
    NETOPS_MOCK=true python -m netops_mcp.selftest
