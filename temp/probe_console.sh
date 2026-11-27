#!/bin/bash
set -euo pipefail
echo "=== [1/3] Console Directory ==="
ls -ld /opt/technitium/technitium-console
ls -la /opt/technitium/technitium-console/assets 2>/dev/null || true
echo "=== [2/3] Drop-in & Port ==="
cat /etc/systemd/system/dns.service.d/console.conf 2>/dev/null || true
echo "=== [3/3] Local HTTP Check ==="
curl -sS -o /dev/null -w "HTTP %{http_code}\n" http://127.0.0.1:5380/ || true
