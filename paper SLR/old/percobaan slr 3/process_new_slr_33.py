import pandas as pd
import os
import re

csv_path = r"C:\kuliah\semester_7\skripsi\slr\scopus_export_Sep-18-2026.csv"
output_csv = r"C:\kuliah\semester_7\skripsi\slr\Matriks_Ekstraksi_SLR_33.csv"
output_xlsx = r"C:\kuliah\semester_7\skripsi\slr\Matriks_Ekstraksi_SLR_33.xlsx"
inc_path = r"C:\kuliah\semester_7\skripsi\slr\scopus_included_33.csv"
exc_path = r"C:\kuliah\semester_7\skripsi\slr\scopus_excluded_33.csv"

if not os.path.exists(csv_path):
    print(f"Error: File not found at {csv_path}")
    exit(1)

df = pd.read_csv(csv_path)
total_initial = len(df)
print(f"=== PROCESSING NEW SCOPUS DATASET (33 PAPERS) ===")
print(f"Total Initial Records: {total_initial}")

# Deduplication
df_dedup = df.drop_duplicates(subset=['Title'], keep='first').copy()
if 'DOI' in df.columns:
    df_dedup = df_dedup.drop_duplicates(subset=['DOI'], keep='first')
dedup_removed = total_initial - len(df_dedup)

def categorize_domain(text):
    text_l = text.lower()
    has_logic = bool(re.search(r'\blogical thinking\b|\blogical reasoning\b|\bdeductive\b|\binductive\b|\bformal logic\b', text_l))
    has_ct = bool(re.search(r'\bcomputational thinking\b|\bprogramming\b|\bcoding\b|\balgorithmic\b', text_l))
    has_ps = bool(re.search(r'\bproblem solving\b|\bproblem-solving\b|\bcognitive\b', text_l))
    
    if has_logic and has_ct:
        return "Domain 3: Integrated (Logical Reasoning & Computational Thinking)"
    elif has_logic:
        return "Domain 1: Logical Reasoning (Logika Matematika / Penalaran Terstruktur)"
    elif has_ct:
        return "Domain 2: Computational Thinking (Logika Pemrograman / Algoritma)"
    elif has_ps:
        return "Domain 3: General Problem Solving & Cognitive Architecture"
    else:
        return "Domain 3: General Adaptive Learning / ITS"

def extract_ai_tech(text):
    text_l = text.lower()
    techs = []
    if 'deep knowledge tracing' in text_l or 'dkt' in text_l:
        techs.append('Deep Knowledge Tracing (DKT)')
    elif 'knowledge tracing' in text_l or 'kt' in text_l:
        techs.append('Knowledge Tracing (KT)')
    if 'transformer' in text_l or 'attention' in text_l or 'sakt' in text_l or 'saint' in text_l:
        techs.append('Transformer / Self-Attention')
    if 'lstm' in text_l or 'gru' in text_l or 'rnn' in text_l:
        techs.append('Recurrent Neural Network (LSTM/GRU)')
    if 'graph' in text_l or 'gnn' in text_l or 'gkt' in text_l:
        techs.append('Graph Neural Network (GNN/GKT)')
    if 'large language model' in text_l or 'llm' in text_l or 'gpt' in text_l or 'generative' in text_l:
        techs.append('LLM / Generative AI Enhanced')
    if 'intelligent tutoring' in text_l or 'its' in text_l:
        techs.append('Intelligent Tutoring System (ITS)')
    if 'adaptive learning' in text_l or 'personalized' in text_l:
        techs.append('Adaptive Learning Engine')
    if not techs:
        techs.append('Knowledge Tracing / Deep Learning')
    return ", ".join(techs)

def extract_metrics(text):
    text_l = text.lower()
    metrics = []
    if 'auc' in text_l or 'area under' in text_l:
        metrics.append('AUC (Area Under ROC)')
    if 'accuracy' in text_l or 'acc' in text_l:
        metrics.append('Accuracy (ACC)')
    if 'rmse' in text_l or 'mse' in text_l or 'mae' in text_l:
        metrics.append('RMSE / Prediction Error')
    if 'gain' in text_l or 'pre-test' in text_l or 'post-test' in text_l:
        metrics.append('Pre/Post-Test Learning Gain (N-Gain)')
    if 'f1' in text_l or 'precision' in text_l or 'recall' in text_l:
        metrics.append('F1-Score / Precision / Recall')
    if not metrics:
        metrics.append('Model Empirical Evaluation / Performance Benchmarking')
    return ", ".join(metrics)

def summarize_abstract(abstract):
    if pd.isna(abstract) or str(abstract).strip() == '':
        return "Abstrak tidak tersedia."
    sentences = str(abstract).split('. ')
    if len(sentences) > 3:
        return ". ".join(sentences[:3]) + "."
    return str(abstract)

included_records = []
excluded_records = []
matrix_records = []

for idx, row in df_dedup.iterrows():
    title = str(row.get('Title', ''))
    abstract = str(row.get('Abstract', ''))
    doc_type = str(row.get('Document Type', ''))
    authors_raw = str(row.get('Authors', 'Unknown'))
    year = str(row.get('Year', ''))
    source = str(row.get('Source title', ''))
    doi = str(row.get('DOI', ''))
    link = f"https://doi.org/{doi}" if doi and str(doi) != 'nan' else str(row.get('Link', ''))
    
    first_author = authors_raw.split(';')[0].strip() if ';' in authors_raw else authors_raw.split(',')[0].strip()
    author_year = f"{first_author} et al. ({year})" if ';' in authors_raw or ',' in authors_raw else f"{first_author} ({year})"
    
    full_text = f"{title} {abstract}"
    
    # Check minimum quality
    has_abstract = abstract != 'nan' and len(abstract.strip()) >= 30
    
    if has_abstract:
        status = "INCLUDED"
        domain = categorize_domain(full_text)
        ai_tech = extract_ai_tech(full_text)
        metrics = extract_metrics(full_text)
        findings = summarize_abstract(abstract)
        
        # Gap Note per domain
        if "Domain 1" in domain:
            gap_note = "Model KT difokuskan pada penalaran logis terstruktur; memerlukan pengujian lebih lanjut pada adaptivitas real-time."
        elif "Domain 2" in domain:
            gap_note = "Model KT difokuskan pada penalaran algoritma/coding; memerlukan pemetaan Knowledge Components (KC) yang lebih rinci."
        else:
            gap_note = "Arsitektur adaptif umum; perlu spesifikasi khusus pada indikator penalaran kognitif."
            
        row_dict = row.to_dict()
        row_dict['Domain_Taxonomy'] = domain
        row_dict['AI_Architecture'] = ai_tech
        row_dict['Evaluation_Metrics'] = metrics
        row_dict['Screening_Status'] = status
        included_records.append(row_dict)
        
        matrix_records.append({
            'No': len(matrix_records) + 1,
            'Penulis & Tahun': author_year,
            'Judul Artikel': title,
            'Jurnal / Prosiding': source,
            'DOI / Link': link,
            'Domain Taksonomi': domain,
            'Arsitektur AI / Deep Learning': ai_tech,
            'Metrik Evaluasi': metrics,
            'Abstrak Lengkap': abstract,
            'Hasil & Temuan Utama': findings,
            'Catatan Kritis / Research Gap': gap_note
        })
    else:
        row_dict = row.to_dict()
        row_dict['Screening_Status'] = "EXCLUDED"
        row_dict['Exclusion_Reason'] = "Missing or insufficient abstract"
        excluded_records.append(row_dict)

df_inc = pd.DataFrame(included_records)
df_exc = pd.DataFrame(excluded_records)
df_matrix = pd.DataFrame(matrix_records)

# Save Outputs
df_inc.to_csv(inc_path, index=False, encoding='utf-8-sig')
df_exc.to_csv(exc_path, index=False, encoding='utf-8-sig')
df_matrix.to_csv(output_csv, index=False, encoding='utf-8-sig')

try:
    df_matrix.to_excel(output_xlsx, index=False, engine='openpyxl')
    print(f"Generated Excel file: {output_xlsx}")
except Exception as e:
    print(f"Excel generation note: {e}")

print(f"\n=== SUMMARY PRISMA 2020 (33 NEW PAPERS) ===")
print(f"Total Initial Records: {total_initial}")
print(f"Duplicates Removed: {dedup_removed}")
print(f"Screened Records: {len(df_dedup)}")
print(f"Included Papers: {len(df_inc)}")
print(f"Excluded Papers: {len(df_exc)}")

print("\n--- DOMAIN TAXONOMY BREAKDOWN ---")
print(df_matrix['Domain Taksonomi'].value_counts())

print("\n--- YEAR DISTRIBUTION ---")
print(df_inc['Year'].value_counts().sort_index(ascending=False))
