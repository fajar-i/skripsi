"""
Script Verifikasi Otomatis Ekstraksi terhadap Naskah Asli PDF (Markdown)
Memeriksa keberadaan metrik kunci dan arsitektur di naskah sumber.
"""

import os
import json

checks = {
    "paper_01.md": {"title": "A Survey of Knowledge Tracing", "tokens": ["EduKTM", "EduData", "ASSISTments"]},
    "paper_02.md": {"title": "Adapting DAS3H Model", "tokens": ["DAS3H", "distributed practice", "memorization"]},
    "paper_03.md": {"title": "Affect is key (AHGKT)", "tokens": ["0.8289", "0.8103", "0.7986", "0.7941", "AHGKT"]},
    "paper_04.md": {"title": "CLST Cold-Start", "tokens": ["CLST", "0.635", "0.722", "Mistral"]},
    "paper_05.md": {"title": "Data Augmentation Sparse (AutoTutor)", "tokens": ["AutoTutor", "0.3715", "0.3948", "tensor"]},
    "paper_06.md": {"title": "Heuristic Learning VR", "tokens": ["VR", "Heuristic", "Character"]},
    "paper_07.md": {"title": "Difficulty aware DPKT", "tokens": ["DPKT", "76.2", "76.8", "CodeNet"]},
    "paper_08.md": {"title": "GuideAI Biosensor", "tokens": ["GuideAI", "Pupil Core", "HRV", "NASA-TLX"]},
    "paper_09.md": {"title": "Guiding Not Solving (SHARP)", "tokens": ["SHARP", "AskCodey", "98%", "94%"]},
    "paper_10.md": {"title": "Infusing Expert Knowledge (DKT+BN)", "tokens": ["DKT+BN", "0.82", "0.80", "Logic-Muse"]},
    "paper_11.md": {"title": "Granular Rank Tensor (GRATE)", "tokens": ["GRATE", "0.7035", "0.2033", "MasteryGrids"]},
    "paper_12.md": {"title": "Spatio-Temporal GNN (STGNN-MKT)", "tokens": ["STGNN-MKT", "0.901", "0.893", "0.845", "0.218"]},
    "paper_13.md": {"title": "Learning Logical Reasoning ITS", "tokens": ["DKTm+BN", "0.82", "0.80", "Logic-Muse"]},
    "paper_14.md": {"title": "Let GPT be a Math Tutor (CEMAL)", "tokens": ["CEMAL", "94.7%", "85.4%", "SVAMP"]},
    "paper_15.md": {"title": "Multiscale Programming (MIE+MLPKT)", "tokens": ["MLPKT", "0.8926", "0.8738", "0.8451"]},
    "paper_16.md": {"title": "Feature Crosses (FCIKT)", "tokens": ["FCIKT", "Feature Crosses", "3.01%"]},
    "paper_17.md": {"title": "Optimizing Mastery Learning (Fast-Forwarding)", "tokens": ["overpractice", "35.7%", "Cognitive Tutor"]},
    "paper_18.md": {"title": "Remembering is Not Applying (PSKT)", "tokens": ["PSKT", "0.8252", "0.8182", "0.8201"]},
    "paper_19.md": {"title": "SageJavon AI Tutor", "tokens": ["SageJavon", "0.7932", "Bloom", "85"]},
    "paper_20.md": {"title": "Tracing Math Proficiency (STATUSKT)", "tokens": ["STATUSKT", "0.6773", "0.6639", "QANDA"]},
    "paper_21.md": {"title": "EDSense Dyscalculia", "tokens": ["EDSense", "Dyscalculia", "Smartick", "137"]}
}

def verify_all():
    print(f"{'Paper':<14} | {'Judul Singkat':<32} | {'Token Terverifikasi':<25} | {'Status'}")
    print("-" * 85)
    
    total_tokens = 0
    total_found = 0
    
    for filename, info in checks.items():
        path = os.path.join("extracted_markdowns", filename)
        if not os.path.exists(path):
            print(f"{filename:<14} | {info['title'][:32]:<32} | FILE TIDAK DITEMUKAN | GAGAL")
            continue
        
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            
        found_tokens = []
        for token in info["tokens"]:
            total_tokens += 1
            if token.lower() in content.lower():
                found_tokens.append(token)
                total_found += 1
                
        status = "VALID" if len(found_tokens) == len(info["tokens"]) else f"PARSIAL ({len(found_tokens)}/{len(info['tokens'])})"
        print(f"{filename:<14} | {info['title'][:32]:<32} | {len(found_tokens)}/{len(info['tokens'])} token cocok {'':<8} | {status}")
        
    print("-" * 85)
    print(f"Hasil Akhir: {total_found}/{total_tokens} token kunci terverifikasi langsung pada naskah asli ({(total_found/total_tokens)*100:.1f}%).")

if __name__ == "__main__":
    verify_all()
