# Catatan Keamanan

- Kredensial di .env (chmod 600); jangan hardcode/commit.
- Gunakan akun layanan read-only di tiap perangkat untuk tahap awal.
- NETOPS_TLS_VERIFY=true di produksi.
- VM di management/OOB network, firewall OS batasi egress ke IP perangkat.
- Rilis saat ini read-only; tool mutasi menyusul dengan konfirmasi + audit log.
