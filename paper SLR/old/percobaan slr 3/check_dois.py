import pandas as pd
df = pd.read_csv(r"C:\kuliah\semester_7\skripsi\slr\scopus_export_Sep-18-2026.csv")
for idx, r in df.head(5).iterrows():
    print(f"[{idx+1}] DOI: {r.get('DOI')} | Title: {r.get('Title')}")
