# 📋 Technitium WebUI - Status Tracker

![Project](https://img.shields.io/badge/project-technitium--webui-blue) ![Status](https://img.shields.io/badge/status-in--progress-orange) ![Version](https://img.shields.io/badge/version-1.4.3-lightgrey)

> [!NOTE]
> Tracking Upstream Sync (v1.4.3 @ `2a30418`), PR #37 & PR #38 remediation, and `sentinel-customizations` branch realignment.

**Legend:** ✅ done | ⬜ pending | 📝 note

---

## 🔧 1. Sovereign Customizations Branch (`sentinel-customizations`) ![Done](https://img.shields.io/badge/-done-brightgreen)

📝 Approved by user on 2026-11-22 (GO). Tasks below are locked.

- ✅ Task 1.1: Rename branch `feat/themes-custom-palettes` to `sentinel-customizations` (local and remote origin)
- ✅ Task 1.2: Ensure clean sync with `upstream/develop` (`2a30418`)
- ✅ Task 1.3: Port and integrate humanized duration spacing (`spaceDuration`) into `src/screens/lists/record.ts`
  - 📝 Receipt: `ev-20261121T191139Z-7318` (`151 passed, 0 failed`)
- ✅ Task 1.4: Run tests on `sentinel-customizations` to verify custom themes, footers, and duration spacing

---

## 🔧 2. PR #37 Remediation (`feat/telemetry-visual-enhancements`) ![Done](https://img.shields.io/badge/-done-brightgreen)

📝 Approved by user on 2026-11-22 (GO). Tasks below are locked.

- ✅ Task 2.1: Verify branch base is aligned with `upstream/develop` (`2a30418`)
- ✅ Task 2.2: Delete `.github/workflows/upstream-gate.yml`
- ✅ Task 2.3: Revert `src/screens/lists/record.ts` to upstream stock duration formatting
- ✅ Task 2.4: Remove QPS badge, Live beacon, and sampling refs from `Figures.tsx`, `Dashboard.tsx`, and `Dashboard.module.css`
- ✅ Task 2.5: Fix Donut center total calculation in `Breakdown.tsx` using `activeTotal` of visible slices
- ✅ Task 2.6: Add `@media (prefers-reduced-motion: reduce)` in `Dashboard.module.css` to disable donut animations
- ✅ Task 2.7: Run Vitest on `Breakdown.test.tsx` and dashboard figures
  - 📝 Receipt: `ev-20261121T192249Z-4190` (`4 passed, 0 failed`)

---

## 🔧 3. PR #38 Remediation & Timezone Sync (`feat/display-timezone`) ![Done](https://img.shields.io/badge/-done-brightgreen)

📝 Approved by user on 2026-11-22 (GO). Tasks below are locked.

- ✅ Task 3.1: Merge `upstream/develop` (`2a30418`) into `feat/display-timezone`
- ✅ Task 3.2: Remove timezone selector and `__open_dialog__` from `src/screens/logs/QueryLogs.tsx` and `Logs.module.css`
- ✅ Task 3.3: Delete `.github/workflows/upstream-gate.yml`
- ✅ Task 3.4: Remove year-one shortcut (`d.getFullYear() <= 1`) in `src/lib/dates.ts` (`formatDate`)
  - 📝 Reverted in PR #38 per upstream maintainer request; moving custom formatting to `sentinel-customizations`
- ✅ Task 3.5: Calculate dynamic UTC offsets via `Intl.DateTimeFormat` in `src/lib/timezone.ts` for worldwide DST compliance
- ✅ Task 3.6: Reconcile `src/screens/dashboard/heatmap.ts` with upstream's `live: number | null` hour indicator (`ffd1485`) and align `weekSpan` to zone midnight
- ✅ Task 3.7: Sanitize comments (default is `local`, not IST) and strip emojis from `ChangeTimezone.tsx`
- ✅ Task 3.8: Run unit tests on `Heatmap.test.tsx`, `dates.test.ts`, and `timezone.test.ts`
  - 📝 Receipt: `ev-20261121T193425Z-feeb` (`33 passed, 0 failed; full suite 3,502 passed`)

---

## 🔧 4. Upstream Contributing Parity Suite ![Done](https://img.shields.io/badge/-done-brightgreen)

📝 Approved by user on 2026-11-22 (GO). Tasks below are locked.

- ✅ Task 4.1: Run `npm run typecheck` (`tsc -b`)
  - 📝 Verified 0 errors
- ✅ Task 4.2: Run `npm run lint` (`oxlint`)
  - 📝 Verified 0 errors across 613 files
- ✅ Task 4.3: Run `npm test` (`vitest run`)
  - 📝 Verified 258 test files passed, 3,502 unit tests passed
- ✅ Task 4.4: Run `npm run build` (`tsc -b && vite build`)
  - 📝 Receipt: `ev-20261121T193851Z-1a38` (`built in 999ms, 41 pages`)
- ✅ Task 4.5: Run language and token linters (`check-language.mjs`, `check-colour-tokens.mjs`, `css-dead.mjs`, `check-parity-sort.mjs`, `check-sort-fields.mjs`, `check-parity-controls.mjs`)
  - 📝 Verified English clean, colour tokens clean, css-dead clean, sort-fields clean, 41 installable pages verified

---

## 🔧 5. Production Deployment Integration (`deploy/sentinel-console`) ![Done](https://img.shields.io/badge/-done-brightgreen)

📝 Approved by user on 2026-11-22 (GO). Tasks below are locked.

- ✅ Task 5.1: Merge `upstream/develop` (`2a30418`) + PR #37 + PR #38 + `sentinel-customizations` into `deploy/sentinel-console`
  - 📝 Clean merge combining all upstream features, PR remediations, and sovereign customizations
- ✅ Task 5.2: Verify full build on `deploy/sentinel-console` with zero behind commits against upstream
  - 📝 Receipt: `ev-20261121T194622Z-e830` (`built in 996ms, 41 pages; 261 test files passed, 3,521 tests passed; 0 behind upstream`)
- ✅ Task 5.3: Ensure `main` mirrors `upstream/main` (`2a30418`)
  - 📝 Fast-forwarded local `main` to `upstream/main` (`2a30418`)
---

## 🔧 6. Fleet Production Deployment (`/opt/technitium/technitium-console`) ![Done](https://img.shields.io/badge/-done-brightgreen)

📝 Approved by user on 2026-11-22 (GO). Tasks below are locked.

- ✅ Task 6.1: Package production distribution archive and sha256 checksum in `temp/`
  - 📝 Receipt: `ev-20261121T200724Z-6937` (`technitium-console.tar.gz 568.5 KB, sha256 88392a722e...`)
- ✅ Task 6.2: Execute atomic fleet deployment to `/opt/technitium/technitium-console` across Mumbai, Phoenix, and Oregon
  - 📝 Receipt: `ev-20261121T200732Z-7fb0` (`Mumbai 5.86s, Oregon 17.25s, Phoenix 16.32s; all PASS`)
- ✅ Task 6.3: Verify HTTP 200 and console responsiveness on all 3 nodes
  - 📝 Receipt: `ev-20261121T200815Z-4004` (`All nodes verified serving React #root, index-CM5jnHqn.js, index-Dixdv4kR.css`)

---

## 🔧 7. Upstream PR #37 & PR #38 Round-2 Remediation ![Done](https://img.shields.io/badge/-done-brightgreen)

📝 Approved by user on 2026-11-22 (GO). Remediations completed and deployed. Tasks locked.

### PR #37 (feat/telemetry-visual-enhancements)
- ✅ Task 7.1: Fix donut mode legend percentage in `src/screens/dashboard/Breakdown.tsx` using active visible total
- ✅ Task 7.2: Add unit test in `src/screens/dashboard/Breakdown.test.tsx` verifying legend shares match donut tooltip when slices are hidden
- ✅ Task 7.3: Remove stray blank lines after `.tiles` in `src/screens/dashboard/Dashboard.module.css`
- ✅ Task 7.4: Revert out-of-scope Windows imports and check-installable script from PR #37
- ✅ Task 7.5: Verify PR #37 locally, commit, push to `origin/feat/telemetry-visual-enhancements`, and update PR description
  - 📝 Commit `be42241` pushed to `origin/feat/telemetry-visual-enhancements`

### PR #38 (feat/display-timezone)
- ✅ Task 7.6: Fix calendar day walking and DST clock change handling in `src/screens/dashboard/heatmap.ts` (`weekSpan` and `heatRows`)
- ✅ Task 7.7: Ensure year-one 4-digit padding (`pad4`) in `src/lib/dates.ts` (`formatDate`) across all timezones
- ✅ Task 7.8: Clean up IST leftovers in `src/lib/timezone.ts`, `src/app/palette/items.ts`, and `src/screens/modals/ChangeTimezone.tsx` (neutral ordering with Local and UTC first)
- ✅ Task 7.9: Restore existing tests in `Heatmap.test.tsx`, `BlockLists.nodes.test.tsx`, and `chart-labels.test.ts` to test default (`local`), add dedicated zoned/DST test blocks, and reset timezones to `local`
- ✅ Task 7.10: Remove trailing blank lines in `src/screens/logs/Logs.module.css` and revert out-of-scope Windows imports
- ✅ Task 7.11: Verify PR #38 locally under both default and non-UTC timezones (`TZ=Europe/Madrid`), commit, push to `origin/feat/display-timezone`, and update PR description
  - 📝 Commit `2930840` pushed to `origin/feat/display-timezone`

### Integration & Upstream Communication
- ✅ Task 7.12: Synchronize fixes into `deploy/sentinel-console`, build release bundle, and deploy to all 3 servers (`Mumbai`, `Phoenix`, `Oregon`)
  - 📝 Built bundle in 1.01s across 41 pages; release tarball `6e674f5d9bc26ac7037f5d9e149f160a761caafaffd886ec8c48f7f0b25e6644`
- ✅ Task 7.13: Verify live deployment via evidence gate receipt
  - 📝 Receipt: `ev-20261122T151634Z-3008` (`Exit code 0; Mumbai, Phoenix, Oregon all HTTP 200 OK`)
- ✅ Task 7.14: Post human developer follow-up comments on upstream PR #37 and PR #38
  - 📝 Comments posted: PR #37 comment `7080973313`, PR #38 comment `7081117717`

---

## 🔧 8. Upstream PR #37 & PR #38 Round-3 Remediation ![In Progress](https://img.shields.io/badge/-in--progress-orange)

📝 Awaiting user approval (GO). Plan staged in `temp/upstream_pr_remediation_round3_plan.md`.

### PR #37 (feat/telemetry-visual-enhancements)
- ⬜ Task 8.1: Suppress percentage share for hidden entries in donut mode in `src/screens/dashboard/Breakdown.tsx` (`datum: ''`)
- ⬜ Task 8.2: Update file header comment in `Breakdown.tsx` and add unit test in `src/screens/dashboard/Breakdown.test.tsx`
- ⬜ Task 8.3: Commit, push to `origin/feat/telemetry-visual-enhancements`, update PR #37 title and description

### PR #38 (feat/display-timezone)
- ⬜ Task 8.4: Implement era-aware year zero formatting in `src/lib/dates.ts` (`formatDate`) and update `dates.test.ts`
- ⬜ Task 8.5: Implement clock change disambiguation (skipped forward, repeated earlier) in `src/screens/logs/dates.ts` (`toIso`)
- ⬜ Task 8.6: Fix `tzMidnight` in `heatmap.ts` to return exact sub-hour midnight and handle skipped midnight
- ⬜ Task 8.7: Fix `untilText` in `blocking-state.ts` to compare calendar days in the active display timezone
- ⬜ Task 8.8: Fix `rangeInstants` in `custom-range.ts` to align start time to display timezone midnight
- ⬜ Task 8.9: Add comprehensive test suites for all timezone edge cases and run Vitest under multiple `TZ` environments
- ⬜ Task 8.10: Commit, push to `origin/feat/display-timezone`, update PR #38 description with clean markdown

### Integration & Upstream Communication
- ⬜ Task 8.11: Merge PR #37 and PR #38 into `deploy/sentinel-console`, verify full build and typecheck
- ⬜ Task 8.12: Package production bundle, deploy across Mumbai, Phoenix, and Oregon, and verify HTTP 200 via evidence gate
- ⬜ Task 8.13: Post human developer review responses on upstream PR #37 and PR #38

---

## 📅 Change Log

### 2026-11-23: Upstream Round-3 Feedback & Remediation Plan Staged
- Added Section 8 detailing all bug fixes requested by upstream owner byGarcia on PR #37 and PR #38.
- Plan documented in `temp/upstream_pr_remediation_round3_plan.md`. Awaiting user GO approval.

### 2026-11-22: Upstream Round-2 PR Remediations Completed & Fleet Deployed
- Completed all round-2 review adjustments requested by byGarcia on PR #37 and PR #38.
- Pushed clean, strictly scoped commits to `origin/feat/telemetry-visual-enhancements` and `origin/feat/display-timezone`.
- Updated PR #38 description to align with final code and posted human developer review responses on both PRs.
- Synchronized release into `deploy/sentinel-console`, built production bundle, and executed atomic deployment across Mumbai, Phoenix, and Oregon. Verified HTTP 200 OK via receipt `ev-20261122T151535Z-8784`.

### 2026-11-22: Upstream Round-2 Feedback & Remediation Plan Staged
- Added Section 7 detailing all bug fixes requested by upstream owner byGarcia on PR #37 and PR #38.

### 2026-11-22: Fleet Deployment Approved
- Added Section 6 for multi-node atomic deployment to `/opt/technitium/technitium-console` preserving stock `www`.

### 2026-11-22: Task Ledger Initialized
- Initialized status tracking for upstream sync, PR remediation, and branch realignment.
