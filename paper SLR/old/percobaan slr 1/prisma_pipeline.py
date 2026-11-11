import pandas as pd
import re
import os
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

START_YEAR = 2021
END_YEAR = 2026

KEYWORDS_GAME = r'game|gaming|simulation|serious game|gamif'
KEYWORDS_TARGET = r'computational thinking|debugging|debug|problem solving|coding|programming|algorithm'

# Exclude non-CS domain articles (e.g. Chinese Literacy, Deep Blue chess book, Linux user guide)
EXCLUDE_PATTERN = r'chinese literacy|manjaro linux user guide|behind deep blue|applied behavior analysis'

def load_and_standardize_data(scopus_path, ieee_path):
    print("="*50)
    print(" 1. TAHAP IDENTIFIKASI (DATA LOADING) ")
    print("="*50)
    
    df_scopus_raw = pd.read_csv(scopus_path)
    count_scopus_raw = len(df_scopus_raw)
    
    df_scopus = pd.DataFrame({
        'source_db': 'Scopus',
        'title': df_scopus_raw['Title'].fillna(''),
        'authors': df_scopus_raw['Authors'].fillna(''),
        'year': pd.to_numeric(df_scopus_raw['Year'], errors='coerce'),
        'source_title': df_scopus_raw['Source title'].fillna(''),
        'abstract': df_scopus_raw['Abstract'].fillna(''),
        'doi': df_scopus_raw['DOI'].fillna('').astype(str).str.lower().str.strip(),
        'doc_type': df_scopus_raw['Document Type'].fillna(''),
        'open_access': df_scopus_raw['Open Access'].fillna('All Access'),
        'link': df_scopus_raw['Link'].fillna('')
    })
    
    df_ieee_raw = pd.read_csv(ieee_path)
    count_ieee_raw = len(df_ieee_raw)
    
    df_ieee = pd.DataFrame({
        'source_db': 'IEEE Xplore',
        'title': df_ieee_raw['Document Title'].fillna(''),
        'authors': df_ieee_raw['Authors'].fillna(''),
        'year': pd.to_numeric(df_ieee_raw['Publication Year'], errors='coerce'),
        'source_title': df_ieee_raw['Publication Title'].fillna(''),
        'abstract': df_ieee_raw['Abstract'].fillna(''),
        'doi': df_ieee_raw['DOI'].fillna('').astype(str).str.lower().str.strip(),
        'doc_type': 'Conference / Journal Paper',
        'open_access': df_ieee_raw['License'].fillna('All Access'),
        'link': df_ieee_raw['PDF Link'].fillna('')
    })
    
    combined = pd.concat([df_scopus, df_ieee], ignore_index=True)
    
    print(f"Hasil Ekspor IEEE Xplore  : {count_ieee_raw} artikel")
    print(f"Hasil Ekspor Scopus       : {count_scopus_raw} artikel")
    print(f"Total Artikel Mentah      : {len(combined)} artikel")
    
    return combined, count_ieee_raw, count_scopus_raw

def run_prisma_pipeline():
    scopus_file = 'scopus_export.csv'
    ieee_file = 'ieee_export.csv'
    
    if not os.path.exists(scopus_file) or not os.path.exists(ieee_file):
        print(f"Error: Pastikan file '{scopus_file}' dan '{ieee_file}' ada di folder ini!")
        return

    df, ieee_raw, scopus_raw = load_and_standardize_data(scopus_file, ieee_file)
    
    # 1. Filter Tahun 2021-2026
    df_year = df[(df['year'] >= START_YEAR) & (df['year'] <= END_YEAR)].copy()
    count_year = len(df_year)
    
    # 2. Deduplikasi
    df_valid_doi = df_year[df_year['doi'] != ''].drop_duplicates(subset=['doi'], keep='first')
    df_empty_doi = df_year[df_year['doi'] == '']
    df_dedup_doi = pd.concat([df_valid_doi, df_empty_doi], ignore_index=True)
    
    df_dedup_doi['title_clean'] = df_dedup_doi['title'].astype(str).str.lower().apply(lambda x: re.sub(r'[^a-z0-9]', '', x))
    df_final_dedup = df_dedup_doi.drop_duplicates(subset=['title_clean'], keep='first').copy()
    
    count_dedup = len(df_final_dedup)
    removed_duplicates = count_year - count_dedup
    
    # 3. Keyword & Relevance Screening
    def check_relevance(row):
        text = f"{str(row['title'])} {str(row['abstract'])}".lower()
        if re.search(EXCLUDE_PATTERN, text):
            return False
        has_game = bool(re.search(KEYWORDS_GAME, text))
        has_target = bool(re.search(KEYWORDS_TARGET, text))
        return has_game and has_target

    df_final_dedup['is_relevant'] = df_final_dedup.apply(check_relevance, axis=1)
    df_eligible = df_final_dedup[df_final_dedup['is_relevant']].copy()
    
    df_eligible = df_eligible.drop(columns=['title_clean', 'is_relevant'])
    
    output_filename = "prisma_eligible_articles_2021_2026.csv"
    df_eligible.to_csv(output_filename, index=False, encoding='utf-8-sig')
    
    print("\n" + "="*50)
    print(" METRIKI DIAGRAM ALIR PRISMA 2020 ")
    print("="*50)
    print(f"1. Total Identifikasi (IEEE: {ieee_raw}, Scopus: {scopus_raw}) : {len(df)} artikel")
    print(f"2. Setelah Filter Rentang Tahun 2021-2026      : {count_year} artikel")
    print(f"3. Duplikat Dihapus                            : {removed_duplicates} artikel")
    print(f"4. Sisa Artikel Unik (Hasil Deduplikasi)       : {count_dedup} artikel")
    print(f"5. Lolos Penapisan Judul/Abstrak (Eligible)    : {len(df_eligible)} artikel")
    print("="*50)
    print(f"SUCCESS: File hasil akhir siap diulas disimpan ke: '{output_filename}'\n")

if __name__ == '__main__':
    run_prisma_pipeline()
