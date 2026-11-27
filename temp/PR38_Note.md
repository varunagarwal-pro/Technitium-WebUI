Thanks for the thorough testing, @byGarcia. I've pushed fixes for all three items from the last review, along with a few year-zero/era edge cases caught while stress-testing against a browser set to each zone:

1. **Restored the `'local'` live-hour logic in `heatRows` (`src/screens/dashboard/heatmap.ts`):**
`heatRows` for `'local'` now reads the live hour from `weekSpan(now, 'local').to` again instead of `new Date(now)`, so half-hour zones like `Asia/Kolkata` match `develop` (e.g. `04:50Z` marks hour 9 of Mon 11/23 and `18:50Z` marks hour 23 of Sun 11/22). Added a test for this in `heatmap.test.ts`.

2. **Two-offset probing in `toIso` instead of fixed ±1h steps (`src/screens/logs/dates.ts`):**
Instead of stepping `±1 hour` around `targetWall`—which missed 30-minute fall-backs like `Australia/Lord_Howe`—`toIso` now probes the zone's offset 24 hours before and 24 hours after the approximate instant (`cBefore` and `cAfter`). `cBefore` is checked first, so repeated times always pick the earlier occurrence (`2026-04-05T01:30:00` -> `14:30Z` in Lord Howe), and skipped times fall through to `Math.max(cBefore, cAfter)` to advance past the gap. Added Lord Howe fall-back and spring-forward cases to `dates.test.ts`.

3. **Plain `era: 'short'` (`src/lib/dates.ts`, `src/screens/logs/dates.ts`):**
Replaced the `'er' + 'a'` string-concatenation workaround and `Record` casts with `era: 'short'` and `part.type === 'era'`.

4. **Year `0..99` and BC/AD consistency across helpers (`src/screens/logs/dates.ts`, `src/api/chart-labels.ts`, `src/screens/dashboard/heatmap.ts`):**
While testing extreme dates against `TZ=<zone>`, I noticed `Date.UTC(y, ...)` and `new Date(y, ...)` were mapping years `0..99` to `1900..1999`, and `toLocalInput` / `formatLabel` weren't accounting for `era` or 4-digit year padding. Switched those constructors to `setUTCFullYear` / `setFullYear`, added signed 4–6 digit year support and `era: 'short'` formatting across `toLocalInput` and `formatLabel`, and cached the `Intl.DateTimeFormat` instances per zone.

**Verification:**
* Compared the zoned path against `'local'` under `TZ=<zone>` across 20 timezones (`UTC`, `America/New_York`, `Europe/Madrid`, `Asia/Kathmandu`, `Australia/Lord_Howe`, `America/Santiago`, `Asia/Beirut`, `America/Havana`, `Pacific/Chatham`, `America/St_Johns`, `Asia/Kolkata`, `Africa/Casablanca`, `Pacific/Easter`, `Antarctica/Troll`, `Asia/Gaza`, `America/Asuncion`, `Pacific/Kiritimati`, `Pacific/Niue`, `Pacific/Apia` including `2011-12-30`, and `Europe/Dublin`) over all of 2026 in 15-minute steps, 6-hour `heatRows` grids, and boundary years from `9999 BC` (`-009998`) through `0000`, `0001`, `0050`, `1883`, and `9999 AD`—zero mismatches.
* Ran all checks from `CONTRIBUTING.md` (including `TZ=Europe/Madrid npm test` and `npm run lint:language`).
