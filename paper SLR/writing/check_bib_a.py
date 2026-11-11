import csv
import re

with open('c:/kuliah/semester_7/skripsi/slr/export_a8f07c28-62e6-474a-87dc-d8a0c117a9bd_2026-10-25T094602.912270816.csv', encoding='utf-8') as f:
    scopus = list(csv.DictReader(f))

with open('c:/Users/user/Downloads/naskah_slr_lengkap(1).md', encoding='utf-8') as f:
    text_a = f.read()

ref_a = text_a[text_a.find('## Daftar Pustaka'):]
entries = [e.strip().replace('\n', ' ') for e in ref_a.split('\n\n') if len(e.strip()) > 30 and '##' not in e]

mismatches = 0
matches = 0
for e in entries:
    m = re.search(r'doi\.org/(10\.[^\s]+)', e)
    doi_a = m.group(1) if m else 'NO_DOI'
    matched = None
    for s in scopus:
        t_prefix = s['Title'][:20].lower()
        if t_prefix in e.lower():
            matched = s
            break
    if matched:
        doi_s = matched['DOI']
        year_s = matched['Year']
        source_s = matched['Source title']
        if doi_a != doi_s and doi_a != 'NO_DOI':
            mismatches += 1
            print(f"MISMATCH in: {matched['Title'][:45]}")
            print(f"  Paper A DOI: {doi_a}")
            print(f"  Scopus DOI : {doi_s}")
            print(f"  Scopus Source: {source_s} ({year_s})")
        else:
            matches += 1

print(f"Paper A results: Matches={matches}, Mismatches={mismatches}")
