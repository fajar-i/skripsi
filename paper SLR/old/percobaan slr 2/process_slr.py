import pandas as pd
import os
import re

csv_path = r"C:\kuliah\semester_7\skripsi\slr\scopus_export.csv"

df = pd.read_csv(csv_path)
total_initial = len(df)

# Step 1: Deduplication
df_dedup = df.drop_duplicates(subset=['Title'], keep='first').copy()
if 'DOI' in df.columns:
    df_dedup = df_dedup.drop_duplicates(subset=['DOI'], keep='first')

duplicates_removed = total_initial - len(df_dedup)

# Define Specific Keyword Clusters
dkt_adaptive_kw = [
    r'\bdeep knowledge tracing\b', r'\bdkt\b', r'\bknowledge tracing\b', 
    r'\badaptive learning\b', r'\bintelligent tutoring\b', r'\bpersonalized learning\b',
    r'\blearning path\b', r'\bstudent model\b', r'\bstudent modeling\b'
]

general_ai_kw = [
    r'\bdeep learning\b', r'\bneural network\b', r'\bartificial intelligence\b', 
    r'\bmachine learning\b', r'\bgenerative ai\b', r'\bllm\b', r'\bsocratic\b'
]

logic_reasoning_kw = [
    r'\blogical thinking\b', r'\blogical reasoning\b', r'\breasoning skill\b', 
    r'\bformal logic\b', r'\bdeductive reasoning\b', r'\binductive reasoning\b', 
    r'\bcomputational thinking\b'
]

cognitive_problem_kw = [
    r'\bproblem solving\b', r'\bcritical thinking\b', r'\bhigher order thinking\b', 
    r'\bhots\b', r'\bcognitive skill\b', r'\bcognitive development\b'
]

pat_dkt = '|'.join(dkt_adaptive_kw)
pat_ai = '|'.join(general_ai_kw)
pat_logic = '|'.join(logic_reasoning_kw)
pat_cog = '|'.join(cognitive_problem_kw)

results = []

for idx, row in df_dedup.iterrows():
    title = str(row.get('Title', '')).lower()
    abstract = str(row.get('Abstract', '')).lower()
    keywords = str(row.get('Author Keywords', '')).lower()
    text = f"{title} {abstract} {keywords}"
    
    has_dkt = bool(re.search(pat_dkt, text))
    has_ai = bool(re.search(pat_ai, text))
    has_logic = bool(re.search(pat_logic, text))
    has_cog = bool(re.search(pat_cog, text))
    
    row_dict = row.to_dict()
    
    # Categorize into Tiers
    if (has_dkt or has_ai) and has_logic:
        tier = "Tier 1: High Relevance (AI/DKT + Logical Reasoning)"
        status = "INCLUDED"
        reason = "Direct match for DKT/AI-Adaptive & Logical Reasoning"
    elif has_dkt and has_cog:
        tier = "Tier 1: High Relevance (DKT/Adaptive + Cognitive/Problem Solving)"
        status = "INCLUDED"
        reason = "Match for DKT/Adaptive Learning & Cognitive Skills"
    elif has_ai and has_cog:
        tier = "Tier 2: Medium Relevance (General AI + Problem Solving/Critical Thinking)"
        status = "INCLUDED (Secondary)"
        reason = "General AIEd with Cognitive/Problem Solving focus"
    else:
        tier = "Tier 3: Low Relevance / Excluded"
        status = "EXCLUDED"
        reasons_list = []
        if not (has_dkt or has_ai):
            reasons_list.append("No AI/Adaptive Learning concept")
        if not (has_logic or has_cog):
            reasons_list.append("No Logical Reasoning/Cognitive concept")
        reason = "; ".join(reasons_list) if reasons_list else "Broad non-technical/non-cognitive paper"
        
    row_dict['Relevance_Tier'] = tier
    row_dict['Screening_Status'] = status
    row_dict['Screening_Note'] = reason
    results.append(row_dict)

df_results = pd.DataFrame(results)

inc_path = r"C:\kuliah\semester_7\skripsi\slr\scopus_included.csv"
exc_path = r"C:\kuliah\semester_7\skripsi\slr\scopus_excluded.csv"
all_path = r"C:\kuliah\semester_7\skripsi\slr\scopus_screened_all.csv"

df_inc = df_results[df_results['Screening_Status'].str.startswith("INCLUDED")].copy()
df_exc = df_results[df_results['Screening_Status'] == "EXCLUDED"].copy()

df_results.to_csv(all_path, index=False)
df_inc.to_csv(inc_path, index=False)
df_exc.to_csv(exc_path, index=False)

print("=== REFINED PRISMA SCREENING REPORT ===")
print(f"Total Initial Records from Scopus: {total_initial}")
print(f"Duplicates Removed: {duplicates_removed}")
print(f"Total Screened Records: {len(df_results)}")
print("\nBreakdown by Relevance Tier:")
print(df_results['Relevance_Tier'].value_counts())

print("\n--- INCLUDED PAPERS BY YEAR ---")
print(df_inc['Year'].value_counts().sort_index(ascending=False))

print(f"\nFiles exported successfully to 'C:\\kuliah\\semester_7\\skripsi\\slr\\':")
print(f" 1. scopus_screened_all.csv ({len(df_results)} rows)")
print(f" 2. scopus_included.csv ({len(df_inc)} rows)")
print(f" 3. scopus_excluded.csv ({len(df_exc)} rows)")
