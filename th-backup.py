"""
Tuneholic Entertainment — Monthly Supabase Backup
Exports all key tables to timestamped CSV files in a backups/ subfolder.
Run manually or via Windows Task Scheduler on the last day of each month.
"""

import os, csv, json, datetime, urllib.request, urllib.error

SUPA_URL = 'https://vqaxatmtomngjffilgtc.supabase.co'
SUPA_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZxYXhhdG10b21uZ2pmdmlsZ3RjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDU4MjYxNjcsImV4cCI6MjA2MTQwMjE2N30.kWbADNLEEqgFGHEuEHAisvDCBZq4TlV2h-EPqjHmP4s'

TABLES = [
    'bookings',
    'artists',
    'venues',
    'artist_unavailability',
    'artist_availability',
    'expenses',
    'expense_templates',
    'project_rules',
    'tbc_entries',
    'tbf_entries',
    'th_invoices',
    'sync_notifications',
    'app_settings',
    'settings',
]

def fetch_table(table):
    url = f'{SUPA_URL}/rest/v1/{table}?select=*&limit=10000'
    req = urllib.request.Request(url, headers={
        'apikey': SUPA_KEY,
        'Authorization': f'Bearer {SUPA_KEY}',
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode())

def export_csv(folder, table, rows):
    if not rows:
        print(f'  {table}: 0 rows — skipped')
        return
    path = os.path.join(folder, f'{table}.csv')
    keys = list(rows[0].keys())
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)
    print(f'  {table}: {len(rows)} rows → {path}')

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    stamp = datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
    folder = os.path.join(script_dir, 'backups', stamp)
    os.makedirs(folder, exist_ok=True)
    print(f'Tuneholic Backup — {stamp}')
    print(f'Output: {folder}')
    errors = []
    for table in TABLES:
        try:
            rows = fetch_table(table)
            export_csv(folder, table, rows)
        except Exception as e:
            print(f'  {table}: ERROR — {e}')
            errors.append(table)
    print()
    if errors:
        print(f'FAILED tables: {errors}')
    else:
        print('All tables backed up successfully.')

if __name__ == '__main__':
    main()
