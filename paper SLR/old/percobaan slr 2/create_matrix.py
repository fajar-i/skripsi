import pandas as pd
import os

inc_path = r"C:\kuliah\semester_7\skripsi\slr\scopus_included.csv"
output_csv = r"C:\kuliah\semester_7\skripsi\slr\Matriks_Ekstraksi_SLR.csv"
output_xlsx = r"C:\kuliah\semester_7\skripsi\slr\Matriks_Ekstraksi_SLR.xlsx"
output_xlsx_alt = r"C:\kuliah\semester_7\skripsi\slr\Matriks_Ekstraksi_SLR_Updated.xlsx"

df = pd.read_csv(inc_path)

def extract_ai_tech(text):
    text_l = text.lower()
    techs = []
    if 'deep knowledge tracing' in text_l or 'dkt' in text_l:
        techs.append('Deep Knowledge Tracing (DKT)')
    if 'transformer' in text_l or 'attention' in text_l or 'sakt' in text_l or 'saint' in text_l:
        techs.append('Transformer / Self-Attention')
    if 'lstm' in text_l or 'gru' in text_l or 'rnn' in text_l:
        techs.append('Recurrent Neural Network (LSTM/GRU)')
    if 'large language model' in text_l or 'llm' in text_l or 'gpt' in text_l or 'generative ai' in text_l or 'genai' in text_l:
        techs.append('LLM / Generative AI')
    if 'reinforcement learning' in text_l:
        techs.append('Reinforcement Learning')
    if 'graph neural network' in text_l or 'gnn' in text_l:
        techs.append('Graph Neural Network (GNN)')
    if 'intelligent tutoring' in text_l or 'its' in text_l:
        techs.append('Intelligent Tutoring System (ITS)')
    if 'adaptive learning' in text_l or 'personalized learning' in text_l:
        techs.append('Adaptive/Personalized Learning Engine')
    if 'machine learning' in text_l or 'deep learning' in text_l or 'neural network' in text_l:
        if not techs:
            techs.append('Deep Learning / Neural Networks')
    return ", ".join(techs) if techs else "Artificial Intelligence Model"

def extract_cognitive_target(text):
    text_l = text.lower()
    targets = []
    if 'logical reasoning' in text_l or 'logical thinking' in text_l or 'deductive' in text_l or 'inductive' in text_l:
        targets.append('Logical Thinking & Reasoning')
    if 'computational thinking' in text_l or 'programming' in text_l or 'coding' in text_l or 'algorithmic' in text_l:
        targets.append('Computational Thinking / Algorithmic Logic')
    if 'critical thinking' in text_l:
        targets.append('Critical Thinking Skills')
    if 'problem solving' in text_l or 'problem-solving' in text_l:
        targets.append('Problem Solving Ability')
    if 'cognitive' in text_l or 'hots' in text_l or 'higher order' in text_l:
        targets.append('Cognitive Development / HOTS')
    return ", ".join(targets) if targets else "Logical & Cognitive Reasoning"

def extract_metrics(text):
    text_l = text.lower()
    metrics = []
    if 'auc' in text_l or 'area under' in text_l:
        metrics.append('AUC (Area Under ROC)')
    if 'accuracy' in text_l or 'acc' in text_l:
        metrics.append('Accuracy (ACC)')
    if 'rmse' in text_l or 'mse' in text_l or 'mae' in text_l:
        metrics.append('RMSE / Prediction Error')
    if 'n-gain' in text_l or 'gain' in text_l or 'pre-test' in text_l or 'post-test' in text_l:
        metrics.append('Pre-test & Post-test / Learning Gain')
    if 'f1' in text_l or 'precision' in text_l or 'recall' in text_l:
        metrics.append('F1-Score / Precision / Recall')
    if 'survey' in text_l or 'tam' in text_l or 'questionnaire' in text_l or 'usability' in text_l:
        metrics.append('User Experience / TAM / Engagement Scale')
    return ", ".join(metrics) if metrics else "Empirical Evaluation / Learning Outcome"

def summarize_abstract(abstract):
    if pd.isna(abstract) or str(abstract).strip() == '':
        return "Abstrak tidak tersedia di Scopus export."
    sentences = str(abstract).split('. ')
    if len(sentences) > 3:
        return ". ".join(sentences[:3]) + "."
    return str(abstract)

matrix_data = []

for idx, row in df.iterrows():
    no = idx + 1
    authors_raw = str(row.get('Authors', 'Unknown'))
    first_author = authors_raw.split(';')[0].strip() if ';' in authors_raw else authors_raw.split(',')[0].strip()
    year = str(row.get('Year', ''))
    author_year = f"{first_author} et al. ({year})" if ';' in authors_raw or ',' in authors_raw else f"{first_author} ({year})"
    
    title = str(row.get('Title', ''))
    source = str(row.get('Source title', ''))
    doi = str(row.get('DOI', ''))
    link = f"https://doi.org/{doi}" if doi and str(doi) != 'nan' else str(row.get('Link', ''))
    
    abstract_full = str(row.get('Abstract', ''))
    full_text = f"{title} {abstract_full}"
    
    ai_tech = extract_ai_tech(full_text)
    cognitive_target = extract_cognitive_target(full_text)
    metrics = extract_metrics(full_text)
    findings = summarize_abstract(abstract_full)
    tier = str(row.get('Relevance_Tier', ''))
    
    gap_note = "Perlu pengujian lebih lanjut pada domain DKT adaptif khusus penalaran logis." if "Tier 2" in tier else "Fokus pada integrasi model adaptif dan pengukuran penalaran kognitif siswa."
    
    matrix_data.append({
        'No': no,
        'Penulis & Tahun': author_year,
        'Judul Artikel': title,
        'Jurnal / Prosiding': source,
        'DOI / Link': link,
        'Arsitektur AI / Deep Learning': ai_tech,
        'Target Kognitif / Logical Thinking': cognitive_target,
        'Metrik Evaluasi': metrics,
        'Tingkat Relevansi SLR': tier,
        'Abstrak Lengkap': abstract_full,
        'Hasil & Temuan Utama': findings,
        'Research Gap / Catatan Kritis': gap_note
    })

df_matrix = pd.DataFrame(matrix_data)

# Export CSV
df_matrix.to_csv(output_csv, index=False, encoding='utf-8-sig')
print(f"Successfully generated CSV at: {output_csv}")

# Export XLSX (with fallback if opened in Excel)
try:
    df_matrix.to_excel(output_xlsx, index=False, engine='openpyxl')
    print(f"Successfully generated XLSX at: {output_xlsx}")
except Exception as e:
    df_matrix.to_excel(output_xlsx_alt, index=False, engine='openpyxl')
    print(f"Original XLSX was open in Excel. Generated updated XLSX at: {output_xlsx_alt}")

print(f"Total Rows Extracted: {len(df_matrix)}")
