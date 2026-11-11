import os
import sys
import json
import warnings
from pathlib import Path
from markitdown import MarkItDown

# Suppress pydub ffmpeg runtime warning
warnings.filterwarnings("ignore")

pdf_dir = Path("pdf")
output_dir = Path("extracted_markdowns")
output_dir.mkdir(parents=True, exist_ok=True)

# Load existing mapping if available for consistent paper_XX IDs
mapping_file = Path("extracted_texts/mapping.json")
pdf_to_id = {}
if mapping_file.exists():
    with open(mapping_file, "r", encoding="utf-8") as f:
        existing_mapping = json.load(f)
        for txt_name, pdf_name in existing_mapping.items():
            base_id = Path(txt_name).stem  # e.g., paper_01
            pdf_to_id[pdf_name] = base_id

pdf_files = sorted(list(pdf_dir.glob("*.pdf")))
total = len(pdf_files)
print(f"Found {total} PDF files in '{pdf_dir}'. Initializing MarkItDown...")

md = MarkItDown()
results_summary = []
markdown_mapping = {}

for idx, pdf_path in enumerate(pdf_files, 1):
    pdf_name = pdf_path.name
    base_name = pdf_path.stem
    paper_id = pdf_to_id.get(pdf_name, f"paper_{idx:02d}")
    
    # Target file paths
    # We save primarily with the paper's full title for readability
    target_md_named = output_dir / f"{base_name}.md"
    # Also save with standardized paper_XX.md for automated pipeline compatibility
    target_md_id = output_dir / f"{paper_id}.md"

    print(f"[{idx}/{total}] Converting: {pdf_name} ({paper_id})...", end=" ", flush=True)
    try:
        res = md.convert(str(pdf_path))
        content = res.text_content
        
        # Save both files
        with open(target_md_named, "w", encoding="utf-8") as f:
            f.write(content)
        with open(target_md_id, "w", encoding="utf-8") as f:
            f.write(content)
            
        markdown_mapping[f"{paper_id}.md"] = {
            "title_md": f"{base_name}.md",
            "pdf_source": pdf_name,
            "char_count": len(content),
            "line_count": len(content.splitlines())
        }
        print(f"SUCCESS ({len(content):,} chars)")
        results_summary.append({"paper": pdf_name, "status": "OK", "chars": len(content)})
    except Exception as e:
        print(f"FAILED: {e}")
        results_summary.append({"paper": pdf_name, "status": f"ERROR: {e}", "chars": 0})

# Save mapping file in extracted_markdowns
with open(output_dir / "mapping.json", "w", encoding="utf-8") as f:
    json.dump(markdown_mapping, f, indent=2, ensure_ascii=False)

print("\nConversion process completed!")
print(f"All converted markdowns saved to '{output_dir}'.")
