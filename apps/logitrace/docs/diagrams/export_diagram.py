import subprocess
import os

DRAWIO_EXE = r"C:\Program Files\draw.io\draw.io.exe"
BASE_DIR = r"C:\kuliah\semester_7\skripsi\apps\logitrace\docs\diagrams"
IN_DRAWIO = os.path.join(BASE_DIR, "activity_diagram_station_rotation.drawio")
OUT_PNG = os.path.join(BASE_DIR, "activity_diagram_station_rotation.png")
OUT_DRAWIO_PNG = os.path.join(BASE_DIR, "activity_diagram_station_rotation.drawio.png")
OUT_SVG = os.path.join(BASE_DIR, "activity_diagram_station_rotation.svg")
REPAIR_SCRIPT = r"C:\Users\user\.gemini\config\skills\drawio-skill\scripts\repair_png.py"

def run_export(args, desc):
    print(f"Running: {desc}...")
    proc = subprocess.run([DRAWIO_EXE] + args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=40)
    print(f"Done: {desc} (code {proc.returncode})")

# 1. Preview PNG
run_export(["-x", "-f", "png", "-s", "2", "-o", OUT_PNG, IN_DRAWIO, "--disable-gpu"], "Preview PNG")

# 2. Final Editable PNG
run_export(["-x", "-f", "png", "-e", "-s", "2", "-o", OUT_DRAWIO_PNG, IN_DRAWIO, "--disable-gpu"], "Editable PNG")

# 3. SVG
run_export(["-x", "-f", "svg", "-e", "-o", OUT_SVG, IN_DRAWIO, "--disable-gpu"], "SVG")

# 4. Repair PNG
if os.path.exists(REPAIR_SCRIPT) and os.path.exists(OUT_DRAWIO_PNG):
    print("Repairing PNG IEND chunk...")
    subprocess.run(["python", REPAIR_SCRIPT, OUT_DRAWIO_PNG])

for f in [OUT_PNG, OUT_DRAWIO_PNG, OUT_SVG]:
    if os.path.exists(f):
        print(f"SUCCESS: {os.path.basename(f)} ({os.path.getsize(f):,} bytes)")
    else:
        print(f"MISSING: {os.path.basename(f)}")
