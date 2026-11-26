# 🌿 SentinelLabs Branching Strategy & Lifecycle Architecture

[![Ecosystem](https://img.shields.io/badge/Ecosystem-Sentinel--Labs-blue?style=for-the-badge&logo=shield)](https://github.com/varunagarwal-pro)
[![Target](https://img.shields.io/badge/Console-Technitium--Webui-purple?style=for-the-badge&logo=react)](https://github.com/varunagarwal-pro/Technitium-WebUI)
[![Fleet](https://img.shields.io/badge/Fleet-Mumbai%20%7C%20Phoenix%20%7C%20Oregon-emerald?style=for-the-badge&logo=linux)](https://github.com/varunagarwal-pro)

> **📌 Target Repository:** `varunagarwal-pro/Technitium-WebUI`  
> **📅 Version:** 1.0.0 (Sovereign Production Standard)  
> **👤 Lead Maintainer:** Varun Agarwal (Sentinel Labs)

---

## 🧭 1. Architectural Overview & Philosophy

The branching strategy for `Technitium-WebUI` enforces a strict separation of concerns across four distinct operational boundaries:
1. **Vanilla Upstream Mirroring:** Clean, fast-forwardable upstream tracking without local commit pollution.
2. **Open-Source Contribution:** Clean, isolated feature branches for upstream pull requests.
3. **Sovereign Customizations:** Proprietary Sentinel enhancements that do not belong upstream.
4. **Cluster Production Deployments:** Release staging for live deployment across the Sentinel server fleet.

```mermaid
flowchart TD
    upstream["Upstream (byGarcia/technitium-console:main)"] -->|Fast-Forward Only (Tier A)| main["main (Pristine Upstream Mirror)"]
    
    upstream_dev["Upstream develop"] -.->|PR #37| pr37["feat/telemetry-visual-enhancements"]
    upstream_dev -.->|PR #38| pr38["feat/display-timezone"]
    
    main -->|Base for Sovereign Work| sovereign["sentinel-customizations"]
    
    main --> deploy["deploy/sentinel-console"]
    sovereign --> deploy
    pr37 -.->|Staged Until Upstream Merge| deploy
    pr38 -.->|Staged Until Upstream Merge| deploy
    
    deploy -->|Multi-Node Deploy| fleet["Fleet (/opt/technitium/technitium-console)<br>• Mumbai (80.225.252.237)<br>• Phoenix (129.146.39.180)<br>• Oregon (35.212.133.199)"]
```

---

## 🗂️ 2. Core Branch Definitions & Roles

### 🔵 `main` — Tier A Pure Upstream Mirror
* **Role:** 100% byte-for-byte pure vanilla replica of upstream `byGarcia/technitium-console:main`.
* **Invariants:**
  * **Strictly zero local commits.** No customizations, no feature merges, and no manual changes.
  * Enrolled as a **Tier A** pure mirror in `D:\SentinelLabs\upstream\fleet.toml`.
  * Automatically audited and fast-forwarded by SentinelOrbit's serverless `fleet-upstream-sync` engine.
  * If `main` contains any local commit, the fleet engine halts immediately with a divergence alert.

### 🟡 `feat/display-timezone` — Upstream PR #38 *(Merged & Retired)*
* **Role:** Dedicated feature branch for upstream Pull Request #38 against `byGarcia/technitium-console:develop`.
* **Scope:**
  * Configurable IANA display timezone preference persisted in `localStorage`.
  * Dynamic DST-aware UTC offset calculation via native `Intl.DateTimeFormat`.
  * Real-time reactive label re-formatting on dashboard charts, heatmap, and query logs.
* **Lifecycle:** Squash-merged into `byGarcia/technitium-console:develop` (`f2c7859`) on 2026-11-25; branch retired and deleted locally and on `origin`.

### 🟣 `feat/telemetry-visual-enhancements` — Upstream PR #37 *(Merged & Retired)*
* **Role:** Dedicated feature branch for upstream Pull Request #37 against `byGarcia/technitium-console:develop`.
* **Scope:**
  * Rank indicator badges (`#1`, `#2`, `#3`) and volume share bars for Top Lists.
  * Dynamic donut chart center count summing active visible slices.
  * Accessibility enhancements respecting `prefers-reduced-motion`.
* **Lifecycle:** Squash-merged into `byGarcia/technitium-console:develop` (`0b98183`) on 2026-11-23; branch retired and deleted locally and on `origin`.

### 🛡️ `sentinel-customizations` — Sovereign Customizations
* **Role:** The permanent home for Sentinel-specific enhancements that are not intended for upstream.
* **Scope:**
  * **Sovereign Themes:** Dark Grey, Amber (phosphor amber & gold), and Glassmorphism (frosted acrylic sky glow) with full $\ge 4.5:1$ WCAG AA contrast compliance.
  * **Profile Selection:** Full theme swatch options in `ThemeChoice.tsx`.
  * **Duration Spacing:** Human-readable spacing in TTL displays (`24d 6h`, `15m 32s`) in `src/screens/lists/record.ts`.
  * **Year-One Default Dates:** Safe handling of uninitialized .NET `DateTime` default timestamps (`d.getFullYear() <= 1`).
  * **Repository Governance:** CodeRabbit configuration (`.coderabbit.yaml`) and workflow tooling.
* **History:** Replaces and supersedes the obsolete upstream-rejected branch `feat/themes-custom-palettes` (which has been permanently deleted).

### 🚀 `deploy/sentinel-console` — Cluster Production Release Branch
* **Role:** The active release deployment branch for the Sentinel DNS fleet.
* **Formula:**
  $$\text{deploy/sentinel-console} = \text{main} + \text{sentinel-customizations} + (\text{feat/display-timezone} + \text{feat/telemetry-visual-enhancements})$$
* **Target Directory:** Deployed strictly to `/opt/technitium/technitium-console` via drop-in `/etc/systemd/system/dns.service.d/console.conf`.
* **Isolation:** The stock console in `/opt/technitium/dns/www` remains **100% untouched**.
* **Future Convergence:** Once PR #37 and PR #38 are merged into upstream `develop` and tagged in a release, upstream sync will fast-forward `main`. At that point, `deploy/sentinel-console` will simply be $\text{main} + \text{sentinel-customizations}$.

---

## 🔄 3. Upstream Sync & Lifecycle Workflow

1. **Upstream Releases:** When `byGarcia/technitium-console` cuts a new release, SentinelOrbit fast-forwards `main` (Tier A).
2. **Rebasing Sovereign Features:** `sentinel-customizations` pulls from updated `main` to verify compatibility.
3. **Deploying Releases:** `deploy/sentinel-console` merges `main` and `sentinel-customizations`, compiles the distribution bundle via `npm run build`, and deploys across Mumbai, Phoenix, and Oregon via `tools/Deploy-Fleet.ps1` or `temp/deploy_fleet.py`.
4. **Zero Main Pollution:** Because `main` is never modified locally, `python tools/upstream/cli.py fleet --mode check --repo Technitium-WebUI` always returns `[ OK ] Technitium-WebUI A UP-TO-DATE:`.
