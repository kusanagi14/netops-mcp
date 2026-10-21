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
    {
        "policyid": 1,
        "name": "LAN-to-WAN",
        "srcintf": "port2",
        "dstintf": "port1",
        "srcaddr": "LAN_SUBNET",
        "dstaddr": "all",
        "action": "accept",
        "status": "enable",
        "nat": "enable",
    },
    {
        "policyid": 2,
        "name": "Block-Threats",
        "srcintf": "port1",
        "dstintf": "port2",
        "srcaddr": "BLOCKLIST",
        "dstaddr": "all",
        "action": "deny",
        "status": "enable",
        "nat": "disable",
    },
]

FORTIGATE_INTERFACES = [
    {"name": "port1", "ip": "198.51.100.2/30", "status": "up", "role": "wan"},
    {"name": "port2", "ip": "10.10.0.1/24", "status": "up", "role": "lan"},
    {"name": "port3", "ip": "0.0.0.0/0", "status": "down", "role": "unassigned"},
]

CATALYST9500_INTERFACES = [
    {"name": "TenGigabitEthernet1/0/1", "admin": "up", "oper": "up", "description": "uplink-core"},
    {"name": "TenGigabitEthernet1/0/2", "admin": "up", "oper": "down", "description": "to-access-sw-3"},
    {"name": "TenGigabitEthernet1/0/3", "admin": "down", "oper": "down", "description": "spare"},
]

CATALYST9500_VERSION = {
    "hostname": "CAT9500-DIST-01",
    "sw_version": "17.12.3",
    "model": "C9500-24Y4C",
    "serial": "FCWEXAMPLE9500",
    "uptime": "41 days, 6 hours",
}

CATALYST_CENTER_DEVICES = [
    {
        "hostname": "CAT9500-DIST-01",
        "managementIpAddress": "10.0.0.11",
        "platformId": "C9500-24Y4C",
        "softwareVersion": "17.12.3",
        "reachabilityStatus": "Reachable",
        "role": "DISTRIBUTION",
    },
    {
        "hostname": "CAT9300-ACC-07",
        "managementIpAddress": "10.0.0.37",
        "platformId": "C9300-48U",
        "softwareVersion": "17.12.3",
        "reachabilityStatus": "Reachable",
        "role": "ACCESS",
    },
    {
        "hostname": "CAT9300-ACC-09",
        "managementIpAddress": "10.0.0.39",
        "platformId": "C9300-48U",
        "softwareVersion": "17.09.4",
        "reachabilityStatus": "Unreachable",
        "role": "ACCESS",
    },
]

CATALYST_CENTER_HEALTH = {
    "networkHealth": 92,
    "totalDevices": 3,
    "healthyDevices": 2,
    "unhealthyDevices": 1,
}
