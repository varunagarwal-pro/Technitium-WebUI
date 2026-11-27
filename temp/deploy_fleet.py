#!/usr/bin/env python3
"""
deploy_fleet.py — Parallel Multi-Node Deployment for Technitium-WebUI
Deploys technitium-console.tar.gz to Mumbai, Phoenix, and Oregon.
"""
from __future__ import annotations
import hashlib
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

KEY_PATH = r"d:\SentinelLabs\SentinelCore\Confidential\Keys\pisg_ed25519"
TAR_PATH = r"d:\SentinelLabs\Technitium-WebUI\temp\technitium-console.tar.gz"
REMOTE_PORT = "41022"
REMOTE_USER = "vexa"

NODES = {
    "mumbai": {
        "name": "Mumbai",
        "ip": "80.225.252.237",
        "domain": "hub.agrawal.pro",
    },
    "phoenix": {
        "name": "Phoenix",
        "ip": "129.146.39.180",
        "domain": "hub.vastrikafashion.in",
    },
    "oregon": {
        "name": "Oregon",
        "ip": "35.212.133.199",
        "domain": "hub.agarwal.us.kg",
    },
}

SSH_OPTS = [
    "-o", "ConnectTimeout=10",
    "-o", "ServerAliveInterval=5",
    "-o", "ServerAliveCountMax=3",
    "-o", "StrictHostKeyChecking=accept-new",
    "-o", "BatchMode=yes",
]

REMOTE_UNPACK_SCRIPT = """#!/bin/bash
set -euo pipefail
DEST="/opt/technitium/technitium-console"
ARCHIVE="/tmp/technitium-console.tar.gz"

echo "=== [1/4] Preparing destination ==="
sudo mkdir -p "$DEST"
sudo rm -rf "$DEST"/*

echo "=== [2/4] Extracting release archive ==="
sudo tar -xzf "$ARCHIVE" -C "$DEST"
sudo chown -R root:root "$DEST"
sudo chmod -R 755 "$DEST"
rm -f "$ARCHIVE"

echo "=== [3/4] Checking assets ==="
ls -la "$DEST/assets" | head -n 5

echo "=== [4/4] Verifying HTTP response ==="
HTTP_CODE=$(curl -sS -o /dev/null -w "%{http_code}" http://127.0.0.1:5380/ || true)
echo "Local HTTP Status: $HTTP_CODE"

if [ "$HTTP_CODE" = "200" ]; then
    echo "[OK] Deployment verified successfully on $(hostname)"
else
    echo "[WARN] HTTP code was $HTTP_CODE"
fi
"""


def deploy_node(node_key: str, node_info: dict) -> tuple[str, bool, str, float]:
    start_time = time.time()
    name = node_info["name"]
    ip = node_info["ip"]
    target = f"{REMOTE_USER}@{ip}"

    # Step 1: Upload tarball via SCP
    scp_cmd = [
        "scp",
        "-i", KEY_PATH,
        "-P", REMOTE_PORT,
    ] + SSH_OPTS + [TAR_PATH, f"{target}:/tmp/technitium-console.tar.gz"]

    res_scp = subprocess.run(scp_cmd, capture_output=True, text=True)
    if res_scp.returncode != 0:
        elapsed = time.time() - start_time
        err_msg = f"SCP failed:\n{res_scp.stderr}\n{res_scp.stdout}"
        return name, False, err_msg, elapsed

    # Step 2: Execute remote unpack script via SSH
    ssh_cmd = [
        "ssh",
        "-i", KEY_PATH,
        "-p", REMOTE_PORT,
    ] + SSH_OPTS + [target, REMOTE_UNPACK_SCRIPT]

    res_ssh = subprocess.run(ssh_cmd, capture_output=True, text=True)
    elapsed = time.time() - start_time
    output = res_ssh.stdout + "\n" + res_ssh.stderr
    success = (res_ssh.returncode == 0) and ("Local HTTP Status: 200" in output)

    return name, success, output, elapsed


def main() -> int:
    print("================================================================================")
    print(" 🚀 SENTINEL FLEET DEPLOYMENT: Technitium-WebUI")
    print("================================================================================")
    print(f" Source Tarball : {TAR_PATH}")
    print(f" Size           : {os.path.getsize(TAR_PATH)} bytes")
    h = hashlib.sha256(Path(TAR_PATH).read_bytes()).hexdigest()
    print(f" SHA256         : {h}")
    print(f" Targets        : {', '.join(n['name'] for n in NODES.values())}")
    print("================================================================================\n")

    overall_start = time.time()
    results = []

    with ThreadPoolExecutor(max_workers=len(NODES)) as executor:
        futures = {executor.submit(deploy_node, k, v): k for k, v in NODES.items()}
        for fut in as_completed(futures):
            results.append(fut.result())

    all_passed = True
    for name, success, out, elapsed in sorted(results, key=lambda x: x[0]):
        status_tag = "[OK]  " if success else "[FAIL]"
        print(f"--------------------------------------------------------------------------------")
        print(f" {status_tag} {name} (Elapsed: {elapsed:.2f}s)")
        print(f"--------------------------------------------------------------------------------")
        print(out.strip())
        print()
        if not success:
            all_passed = False

    total_time = time.time() - overall_start
    print("================================================================================")
    print(f" FLEET DEPLOYMENT SUMMARY: {'ALL PASSED' if all_passed else 'SOME FAILED'} ({total_time:.2f}s)")
    print("================================================================================")
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
