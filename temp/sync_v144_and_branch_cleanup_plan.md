# Implementation Plan: Technitium-WebUI v1.4.4 Sync, Branch Cleanup & 3-Node Fleet Deploy

## 1. Current Verified State vs Target 5-Role Standard

| Branch | Current Local | Current `origin` | Action |
|---|---|---|---|
| `feat/telemetry-visual-enhancements` (PR #37) | Already deleted | Already deleted | None needed |
| `feat/display-timezone` (PR #38) | Already deleted | Already deleted | None needed |
| `sentinel-customizations` | `efb55a5` (exists) | Already deleted | `git branch -D sentinel-customizations` + `git fetch --prune origin` |
| `deploy/sentinel-console` | `731ca62` (exists) | `731ca62` (exists) | Delete locally (`git branch -D deploy/sentinel-console`) & on GitHub (`git push origin --delete deploy/sentinel-console`) |
| `upstream-mirror` | `2a30418` (`v1.4.3`) | `a4ce53d` (`v1.4.4` + 2 upstream doc/test commits) | Fast-forward local `upstream-mirror` to `origin/upstream-mirror` (`a4ce53d`) |
| `custom` | `efb55a5` (contains PR #37/#38 merge artifacts) | `efb55a5` | Rebase/clean onto `upstream-mirror` (`a4ce53d`) so `custom` holds **only** our sovereign customizations (themes, `byVarun` footer, duration spacing, year-one date shortcut, `fileURLToPath`, governance/docs) |
| `main` | `20d8f89` | `20d8f89` | Integrate `upstream-mirror` (`a4ce53d`) + cleaned `custom`, verify all checks, push `custom` & `main` |

---

## 2. Step-by-Step Execution Plan

### Phase 1: Branch Cleanup & `upstream-mirror` Sync
1. Prune stale remote-tracking refs: `git fetch --prune origin` and `git fetch upstream --tags`.
2. Delete retired local branches: `sentinel-customizations` and `deploy/sentinel-console`.
3. Delete retired remote branch on GitHub: `git push origin --delete deploy/sentinel-console`.
4. Fast-forward local `upstream-mirror` to `origin/upstream-mirror` (`a4ce53d`, which includes `Release 1.4.4` `9349db6`).

### Phase 2: Clean `custom` Branch (Only Sovereign Customizations)
1. Audit `upstream-mirror..custom` commits and ensure `custom` is rebased cleanly onto `upstream-mirror` (`a4ce53d`), dropping upstream-merged PR #37 (`0b98183`) and PR #38 (`be7ee54`) commits.
2. Verify `git diff --stat upstream-mirror..custom` shows **only** our custom theme, footer, duration-spacing, year-one date, cross-platform test/build, and repo governance files (zero PR #37/#38 leftovers).
3. Update `docs/BRANCHING_STRATEGY.md` (replace stale Mermaid diagram and `sentinel-customizations`/`deploy/sentinel-console` sections with the `upstream-mirror` + `custom` → `main` standard) and `Tasks.md` (add `v1.4.4` sync & branch retirement log).
4. Run `npm run lint`, `npm run typecheck`, `npm test`, and `npm run build` on `custom`.

### Phase 3: Integrate into `main` & Close Cycle
1. Merge `upstream-mirror` (`a4ce53d`) and cleaned `custom` into `main` (resolving any conflicts cleanly in favor of `v1.4.4` upstream + our custom layer).
2. Run full verification suite on `main` via `evidence_gate.py`:
   - `npm run lint` (`oxlint`)
   - `npm run typecheck` (`tsc -b --force`)
   - `npm test` (`vitest run`)
   - `npm run build` (`tsc -b && vite build`)
3. Push `custom` (with `--force-with-lease` if rebased) and `main` to `origin`.
4. Run `python D:\SentinelLabs\tools\upstream\cli.py close-cycle --repo Technitium-WebUI` and `cli.py doctor --repo Technitium-WebUI`.

### Phase 4: Compile & Deploy to All 3 Servers
1. Deploy the verified `dist/` production bundle from `main` to `/opt/technitium/technitium-console` across **Mumbai** (`80.225.252.237`), **Phoenix** (`129.146.39.180`), and **Oregon** (`35.212.133.199`) in parallel (using `Deploy-Fleet.ps1` or `remote_exec.ps1`), preserving `/opt/technitium/dns/www` untouched.
2. Verify `dns.service` health and served `v1.4.4` console assets on all 3 nodes.
