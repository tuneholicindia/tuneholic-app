# Tuneholic Entertainment — Portal Project

## Who
- Company: Tuneholic Entertainment, Pune/Mumbai
- Email: tuneholicindia@gmail.com
- Role: Artist management, live music bookings

## The App
Single-file HTML portal: `index.html` (this folder)
- Run locally: `cd "C:\Users\mynew\Downloads\TP IMPROVEMENT" && python -m http.server 8080`
- Open in Chrome: `http://localhost:8080`
- PIN to enter admin: `2606` (session key: `th_admin_auth`)

## GitHub
- Repo: https://github.com/tuneholicindia/tuneholic-app
- Token: TOKEN_IN_GIT_SAVE_BAT (expires Sep 14 2026) — actual token stored in git-push-now.bat + th-git-push.bat (not committed)
- Auto-backup: runs nightly at 11 PM via Windows Task Scheduler
- Manual save: run `git-save.bat`
- Restore any version: run `git-restore.bat`

## Supabase
- Project ID: vqaxatmtomngjffilgtc
- JWT anon key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZxYXhhdG10b21uZ2pmdmlsZ3RjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDU4MjYxNjcsImV4cCI6MjA2MTQwMjE2N30.kWbADNLEEqgFGHEuEHAisvDCBZq4TlV2h-EPqjHmP4s
- MCP tool: mcp__7583b38d-934c-4d0a-90c5-db4114f5474a__execute_sql

## Key Tables (Supabase)
- `bookings` — id, month, year, date (int day), day (text), artist, type, venue, amount, artist_pay, tax, genre, slot, insta, note, status, created_at
- `artist_unavailability` — artist, date, reason
- `artists` — name, type, genre (124 seeded)
- `venues` — name (49 seeded)
- `th_invoices` — inv_no, artist, venue, gig_date, amount, remark, save_date
- `artist_pins` — artist, pin
- `expenses` — for financial tracking

## Code Rules (NEVER break these)
1. NEVER modify existing code in index.html
2. ALL changes = append-only `<script>` blocks before `</body>` at TRUE END of file
3. Always validate with `node --check` before saving
4. The file has multiple `</body>` tags — first one is INSIDE a JS string (_doVenueBillPrint). Always append at absolute end.
5. After every change: check file size and line count to confirm no corruption

## What's Built (Current State)
- Phase 1A–2D: Core portal, bookings, calendar, payouts, financials
- Phase 3A–3E: PDF contracts/invoices/payslips, TDS ledger, session reminders, artist ledger, artist portal
- Phase 4A: Artist availability calendar, conflict detection, PIN migration
- UI: Sidebar nav (v2), dark/light theme toggle, gold accent design
- Live Ops: Compact table layout, Supabase JWT fix, WA bulk send with step panel
- Payouts: Artist invoice with logo, PDF download, WhatsApp share, Bill Out tab
- Bill Out: th_invoices table, grouped by artist/venue, date filterable
- Cancelled gigs: Auto-shows in Live Ops cancelled section
- Artist name canonicalization: ARTIST_NAME_MAP in Block 4
- WA message format: 🎵 header, artist/date/venue/slot/type/reach-by, plain thank you

## Known Issues / Pending
- WhatsApp image send: can only auto-copy card to clipboard (browser limitation — no auto-attach)
- hardcoded allBookings (448 entries) in HTML + Supabase live = two sources, need dedup
- Supabase single source of truth migration: future goal

## Communication Style
- Be direct and surgical
- Diagnose root cause FIRST, then fix
- Never modify existing code — append only
- Test with node --check before every file write
- Share file only after confirming it's clean
