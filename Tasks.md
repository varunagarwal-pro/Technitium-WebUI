# 📋 Technitium WebUI — Status Tracker

![Project](https://img.shields.io/badge/project-technitium--webui-blue) ![Status](https://img.shields.io/badge/status-in%20progress-yellow) ![Version](https://img.shields.io/badge/version-1.4.3-lightgrey)

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

## 🔧 5. Production Deployment Integration (`deploy/sentinel-console`) ![Pending](https://img.shields.io/badge/-pending-red)

📝 Approved by user on 2026-11-22 (GO). Tasks below are locked.

- ⬜ Task 5.1: Merge `upstream/develop` (`2a30418`) + PR #37 + PR #38 + `sentinel-customizations` into `deploy/sentinel-console`
- ⬜ Task 5.2: Verify full build on `deploy/sentinel-console` with zero behind commits against upstream
- ⬜ Task 5.3: Ensure `main` mirrors `upstream/main` (`2a30418`)

---

## 📅 Change Log

### 2026-11-22: Task Ledger Initialized
- Initialized status tracking for upstream sync, PR remediation, and branch realignment.
