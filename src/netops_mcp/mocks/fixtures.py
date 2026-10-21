"""Fixture data contoh untuk MOCK MODE."""
from __future__ import annotations

FORTIGATE_SYSTEM_STATUS = {
    "hostname": "FGT-EDGE-01",
    "version": "v7.4.4",
    "serial": "FGVM00EXAMPLE001",
    "model": "FortiGate-VM64",
    "uptime_seconds": 1820344,
}

FORTIGATE_FIREWALL_POLICIES = [
    {"policyid": 1, "name": "LAN-to-WAN", "srcintf": "port2", "dstintf": "port1",
     "srcaddr": "LAN_SUBNET", "dstaddr": "all", "action": "accept", "status": "enable", "nat": "enable"},
    {"policyid": 2, "name": "Block-Threats", "srcintf": "port1", "dstintf": "port2",
     "srcaddr": "BLOCKLIST", "dstaddr": "all", "action": "deny", "status": "enable", "nat": "disable"},
]

FORTIGATE_INTERFACES = [
    {"name": "port1", "ip": "198.51.100.2/30", "status": "up", "role": "wan"},
    {"name": "port2", "ip": "10.10.0.1/24", "status": "up", "role": "lan"},
    {"name": "port3", "ip": "0.0.0.0/0", "status": "down", "role": "unassigned"},
]

FORTIGATE_RESOURCE = {"cpu": 12, "memory": 38, "session_count": 1842, "uptime_seconds": 1820344, "disk_usage_percent": 21}

FORTIGATE_HA_STATUS = [
    {"serial": "FGVM00EXAMPLE001", "role": "primary", "hostname": "FGT-EDGE-01", "sync_status": "synchronized"},
    {"serial": "FGVM00EXAMPLE002", "role": "secondary", "hostname": "FGT-EDGE-02", "sync_status": "synchronized"},
]

FORTIGATE_ROUTES = [
    {"type": "static", "ip_mask": "0.0.0.0/0", "gateway": "198.51.100.1", "interface": "port1", "distance": 10},
    {"type": "connected", "ip_mask": "10.10.0.0/24", "gateway": "0.0.0.0", "interface": "port2", "distance": 0},
]

FORTIGATE_BGP_NEIGHBORS = [
    {"neighbor_ip": "198.51.100.1", "remote_as": 65001, "state": "Established", "uptime": "4d2h", "prefixes_received": 1420},
]

FORTIGATE_SESSIONS = [
    {"proto": "tcp", "src": "10.10.0.50:51324", "dst": "142.250.4.100:443", "state": "established", "policyid": 1},
    {"proto": "udp", "src": "10.10.0.51:5353", "dst": "8.8.8.8:53", "state": "active", "policyid": 1},
    {"proto": "tcp", "src": "10.10.0.52:44120", "dst": "52.95.110.1:443", "state": "established", "policyid": 1},
]

FORTIGATE_IPSEC = [
    {"name": "to-branch-01", "p2name": "branch01-p2", "status": "up", "rx_bytes": 1048576, "tx_bytes": 2097152, "remote_gw": "203.0.113.10"},
    {"name": "to-branch-02", "p2name": "branch02-p2", "status": "down", "rx_bytes": 0, "tx_bytes": 0, "remote_gw": "203.0.113.20"},
]

FORTIGATE_SSLVPN = [
    {"user": "alice", "remote_host": "203.0.113.55", "duration_seconds": 3600, "tunnel_ip": "10.212.134.200"},
]

FORTIGATE_DHCP = [
    {"ip": "10.10.0.50", "mac": "00:11:22:33:44:55", "hostname": "laptop-01", "expire_seconds": 43200, "interface": "port2"},
]

FORTIGATE_ARP = [
    {"ip": "10.10.0.1", "mac": "00:aa:bb:cc:dd:01", "interface": "port2"},
    {"ip": "10.10.0.50", "mac": "00:11:22:33:44:55", "interface": "port2"},
]

FORTIGATE_POLICY_HITS = [
    {"policyid": 1, "name": "LAN-to-WAN", "hit_count": 1842934, "bytes": 982374650, "last_used": "2026-10-14T09:12:00Z"},
    {"policyid": 2, "name": "Block-Threats", "hit_count": 231, "bytes": 18420, "last_used": "2026-10-10T02:40:00Z"},
]

FORTIGATE_DNS = {"primary": "8.8.8.8", "secondary": "8.8.4.4", "primary_status": "reachable", "secondary_status": "reachable"}

CATALYST9500_INTERFACES = [
    {"name": "TenGigabitEthernet1/0/1", "admin": "up", "oper": "up", "description": "uplink-core"},
    {"name": "TenGigabitEthernet1/0/2", "admin": "up", "oper": "down", "description": "to-access-sw-3"},
    {"name": "TenGigabitEthernet1/0/3", "admin": "down", "oper": "down", "description": "spare"},
]

CATALYST9500_VERSION = {
    "hostname": "CAT9500-DIST-01", "sw_version": "17.12.3", "model": "C9500-24Y4C",
    "serial": "FCWEXAMPLE9500", "uptime": "41 days, 6 hours",
}

CATALYST_CENTER_DEVICES = [
    {"hostname": "CAT9500-DIST-01", "managementIpAddress": "10.0.0.11", "platformId": "C9500-24Y4C",
     "softwareVersion": "17.12.3", "reachabilityStatus": "Reachable", "role": "DISTRIBUTION"},
    {"hostname": "CAT9300-ACC-07", "managementIpAddress": "10.0.0.37", "platformId": "C9300-48U",
     "softwareVersion": "17.12.3", "reachabilityStatus": "Reachable", "role": "ACCESS"},
    {"hostname": "CAT9300-ACC-09", "managementIpAddress": "10.0.0.39", "platformId": "C9300-48U",
     "softwareVersion": "17.09.4", "reachabilityStatus": "Unreachable", "role": "ACCESS"},
]

CATALYST_CENTER_HEALTH = {"networkHealth": 92, "totalDevices": 3, "healthyDevices": 2, "unhealthyDevices": 1}
