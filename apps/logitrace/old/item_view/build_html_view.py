"""
Build script to generate an interactive, self-contained HTML dashboard
for exploring question distribution in LogiTrace (apps/logitrace/data).
Generates 'pembagian_soal.html' in the same folder.
"""

import json
import os
import sys

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_HTML = os.path.join(DATA_DIR, "pembagian_soal.html")

def build():
    # 1. Load all data files
    with open(os.path.join(DATA_DIR, "l2_item_bank", "items_adaptive_180.json"), "r", encoding="utf-8") as f:
        adaptive_items = json.load(f)

    with open(os.path.join(DATA_DIR, "l2_item_bank", "tolt_test_parallel.json"), "r", encoding="utf-8") as f:
        tolt_data = json.load(f)

    with open(os.path.join(DATA_DIR, "l2_item_bank", "nedv_control_items.json"), "r", encoding="utf-8") as f:
        nedv_data = json.load(f)

    with open(os.path.join(DATA_DIR, "l1_knowledge_base", "kcs.json"), "r", encoding="utf-8") as f:
        kcs_list = json.load(f)

    with open(os.path.join(DATA_DIR, "l1_knowledge_base", "tolt_dimensions.json"), "r", encoding="utf-8") as f:
        dims_list = json.load(f)

    with open(os.path.join(DATA_DIR, "l1_knowledge_base", "dag_prerequisites.json"), "r", encoding="utf-8") as f:
        dag_data = json.load(f)

    with open(os.path.join(DATA_DIR, "fallback_hints", "static_hints.json"), "r", encoding="utf-8") as f:
        hints_data = json.load(f)

    # Convert datasets to JSON strings for embedding
    db_json = json.dumps({
        "adaptive": adaptive_items,
        "tolt": tolt_data,
        "nedv": nedv_data,
        "kcs": kcs_list,
        "dims": dims_list,
        "dag": dag_data,
        "hints": hints_data
    }, ensure_ascii=False)

    html_content = f'''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LogiTrace — Visualisasi & Pembagian Soal Adaptif (Bank 206 Butir)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #4338ca;
      --primary-hover: #3730a3;
      --primary-light: #e0e7ff;
      --primary-50: #eef2ff;
      --primary-dark: #312e81;
      
      --secondary: #0d9488;
      --secondary-light: #ccfbf1;
      
      --accent: #f59e0b;
      --accent-light: #fef3c7;
      
      --danger: #ef4444;
      --danger-light: #fee2e2;
      
      --success: #10b981;
      --success-light: #d1fae5;
      
      --bg: #f8fafc;
      --surface: #ffffff;
      --surface-subtle: #f1f5f9;
      --border: #e2e8f0;
      --border-dark: #cbd5e1;
      
      --text: #0f172a;
      --text-muted: #475569;
      --text-subtle: #64748b;
      
      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
      
      --shadow-xs: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
      --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1);
      --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1);
      --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
      --radius-sm: 6px;
      --radius: 10px;
      --radius-lg: 16px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: var(--font-sans);
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      display: flex;
      flex-direction: column;
      min-height: 100vh;
    }}

    /* HEADER */
    header {{
      background: linear-gradient(135deg, #1e1b4b 0%, #312e81 60%, #4338ca 100%);
      color: #ffffff;
      padding: 24px 32px 18px;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
      position: sticky;
      top: 0;
      z-index: 100;
    }}

    .header-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      margin-bottom: 18px;
    }}

    .brand-area {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}

    .brand-icon {{
      width: 44px;
      height: 44px;
      background: rgba(255, 255, 255, 0.15);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255, 255, 255, 0.25);
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 22px;
    }}

    .brand-title h1 {{
      font-size: 20px;
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.2;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .brand-title h1 span.badge-tag {{
      background: rgba(255, 255, 255, 0.2);
      font-size: 11px;
      padding: 2px 8px;
      border-radius: 999px;
      font-weight: 600;
      letter-spacing: normal;
    }}

    .brand-title p {{
      font-size: 13px;
      color: #c7d2fe;
      margin-top: 2px;
    }}

    .header-actions {{
      display: flex;
      gap: 10px;
      align-items: center;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      font-size: 13px;
      font-weight: 600;
      border-radius: 8px;
      cursor: pointer;
      border: none;
      transition: all 0.15s ease;
      font-family: inherit;
      text-decoration: none;
    }}

    .btn-header {{
      background: rgba(255, 255, 255, 0.15);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.25);
    }}

    .btn-header:hover {{
      background: rgba(255, 255, 255, 0.25);
      transform: translateY(-1px);
    }}

    .btn-primary {{
      background: var(--primary);
      color: white;
    }}

    .btn-primary:hover {{
      background: var(--primary-hover);
    }}

    .btn-outline {{
      background: transparent;
      border: 1px solid var(--border-dark);
      color: var(--text-muted);
    }}

    .btn-outline:hover {{
      background: var(--surface-subtle);
      color: var(--text);
    }}

    .btn-sm {{
      padding: 5px 10px;
      font-size: 12px;
    }}

    /* STATS STRIP */
    .stats-strip {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
      gap: 10px;
      margin-top: 6px;
    }}

    .stat-pill {{
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: 8px;
      padding: 8px 12px;
      display: flex;
      flex-direction: column;
    }}

    .stat-pill .val {{
      font-size: 18px;
      font-weight: 800;
      line-height: 1.1;
      font-family: var(--font-mono);
      color: #ffffff;
    }}

    .stat-pill .lbl {{
      font-size: 11px;
      color: #c7d2fe;
      margin-top: 3px;
      font-weight: 500;
    }}

    /* NAVIGATION TABS */
    .tab-bar {{
      display: flex;
      gap: 4px;
      background: #ffffff;
      border-bottom: 1px solid var(--border);
      padding: 0 32px;
      overflow-x: auto;
      scrollbar-width: none;
    }}

    .tab-bar::-webkit-scrollbar {{
      display: none;
    }}

    .tab-btn {{
      padding: 13px 18px;
      font-size: 13.5px;
      font-weight: 600;
      color: var(--text-muted);
      background: transparent;
      border: none;
      border-bottom: 3px solid transparent;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      white-space: nowrap;
      transition: all 0.15s ease;
      font-family: inherit;
    }}

    .tab-btn:hover {{
      color: var(--primary);
      background: var(--primary-50);
    }}

    .tab-btn.active {{
      color: var(--primary);
      border-bottom-color: var(--primary);
      font-weight: 700;
    }}

    .tab-btn .badge-count {{
      background: var(--surface-subtle);
      color: var(--text-muted);
      font-size: 11px;
      padding: 2px 6px;
      border-radius: 999px;
      font-weight: 700;
    }}

    .tab-btn.active .badge-count {{
      background: var(--primary-light);
      color: var(--primary);
    }}

    /* MAIN CONTAINER */
    main {{
      flex: 1;
      padding: 24px 32px 60px;
      max-width: 1600px;
      margin: 0 auto;
      width: 100%;
    }}

    .tab-pane {{
      display: none;
    }}

    .tab-pane.active {{
      display: block;
      animation: fadeIn 0.2s ease-in-out;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* CARDS & CONTAINERS */
    .card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      box-shadow: var(--shadow-sm);
      padding: 20px;
      margin-bottom: 20px;
    }}

    .card-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 16px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border);
      flex-wrap: wrap;
      gap: 10px;
    }}

    .card-title {{
      font-size: 16px;
      font-weight: 700;
      color: var(--text);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .card-subtitle {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 2px;
    }}

    /* GRID & LAYOUTS */
    .grid-2 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
      gap: 20px;
    }}

    .grid-3 {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 16px;
    }}

    /* CHARTS & DISTRIBUTION BARS */
    .dist-row {{
      display: flex;
      align-items: center;
      margin-bottom: 10px;
      font-size: 13px;
    }}

    .dist-label {{
      width: 220px;
      font-weight: 600;
      color: var(--text);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      padding-right: 12px;
    }}

    .dist-bar-wrap {{
      flex: 1;
      height: 24px;
      background: var(--surface-subtle);
      border-radius: 6px;
      overflow: hidden;
      display: flex;
      position: relative;
    }}

    .dist-segment {{
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 11px;
      font-weight: 700;
      font-family: var(--font-mono);
      transition: width 0.3s ease;
    }}

    .bg-easy {{ background-color: #10b981; }}
    .bg-med {{ background-color: #f59e0b; }}
    .bg-hard {{ background-color: #ef4444; }}

    .dist-val {{
      width: 70px;
      text-align: right;
      font-weight: 700;
      font-family: var(--font-mono);
      color: var(--text-muted);
      padding-left: 12px;
      font-size: 13px;
    }}

    /* PILLS & BADGES */
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 700;
      line-height: 1.2;
      border: 1px solid transparent;
    }}

    .badge-diff-1 {{
      background: #ecfdf5;
      color: #065f46;
      border-color: #a7f3d0;
    }}

    .badge-diff-2 {{
      background: #fffbeb;
      color: #92400e;
      border-color: #fde68a;
    }}

    .badge-diff-3 {{
      background: #fef2f2;
      color: #991b1b;
      border-color: #fecaca;
    }}

    .badge-kc {{
      background: var(--primary-50);
      color: var(--primary);
      border-color: var(--primary-light);
      font-family: var(--font-mono);
    }}

    .badge-tolt {{
      background: #f0fdf4;
      color: #166534;
      border-color: #bbf7d0;
      font-size: 11px;
    }}

    .badge-calib {{
      background: #f3e8ff;
      color: #6b21a8;
      border-color: #d8b4fe;
    }}

    .badge-bank {{
      background: #f1f5f9;
      color: #334155;
      border-color: #cbd5e1;
    }}

    .badge-ans {{
      background: #1e293b;
      color: #ffffff;
      font-family: var(--font-mono);
      font-size: 11px;
      padding: 2px 7px;
    }}

    /* MATRIX TABLE */
    .table-container {{
      overflow-x: auto;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      background: var(--surface);
    }}

    table.matrix-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13px;
      text-align: left;
    }}

    table.matrix-table th {{
      background: var(--surface-subtle);
      color: var(--text-muted);
      font-weight: 700;
      padding: 12px 14px;
      border-bottom: 2px solid var(--border);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }}

    table.matrix-table td {{
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
      vertical-align: middle;
    }}

    table.matrix-table tr:hover td {{
      background-color: #f8fafc;
    }}

    .matrix-cell {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 6px 12px;
      border-radius: 6px;
      font-weight: 700;
      font-family: var(--font-mono);
      cursor: pointer;
      transition: all 0.15s ease;
      min-width: 44px;
      text-align: center;
    }}

    .matrix-cell:hover {{
      transform: scale(1.08);
      box-shadow: var(--shadow-sm);
    }}

    .matrix-cell.cell-easy {{
      background: #d1fae5;
      color: #047857;
      border: 1px solid #6ee7b7;
    }}

    .matrix-cell.cell-med {{
      background: #fef3c7;
      color: #b45309;
      border: 1px solid #fcd34d;
    }}

    .matrix-cell.cell-hard {{
      background: #fee2e2;
      color: #b91c1c;
      border: 1px solid #fca5a5;
    }}

    /* CATALOG & FILTERS */
    .filter-bar {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 16px;
      margin-bottom: 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}

    .filter-row {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }}

    .search-input-wrap {{
      flex: 1;
      min-width: 260px;
      position: relative;
    }}

    .search-input {{
      width: 100%;
      padding: 9px 14px 9px 36px;
      border: 1px solid var(--border-dark);
      border-radius: 8px;
      font-size: 13.5px;
      font-family: inherit;
      outline: none;
      transition: all 0.15s ease;
      background: var(--bg);
    }}

    .search-input:focus {{
      border-color: var(--primary);
      background: white;
      box-shadow: 0 0 0 3px rgba(67, 56, 202, 0.15);
    }}

    .search-icon {{
      position: absolute;
      left: 12px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-subtle);
      font-size: 15px;
    }}

    .select-filter {{
      padding: 9px 12px;
      border: 1px solid var(--border-dark);
      border-radius: 8px;
      font-size: 13px;
      font-family: inherit;
      background: white;
      color: var(--text);
      outline: none;
      cursor: pointer;
    }}

    .select-filter:focus {{
      border-color: var(--primary);
    }}

    .filter-stats-text {{
      font-size: 13px;
      font-weight: 600;
      color: var(--text-muted);
    }}

    /* ITEM CARD */
    .item-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 18px 20px;
      margin-bottom: 16px;
      box-shadow: var(--shadow-xs);
      transition: all 0.15s ease;
      border-left: 4px solid var(--border);
    }}

    .item-card:hover {{
      box-shadow: var(--shadow-md);
      border-color: var(--border-dark);
    }}

    .item-card.diff-border-1 {{ border-left-color: #10b981; }}
    .item-card.diff-border-2 {{ border-left-color: #f59e0b; }}
    .item-card.diff-border-3 {{ border-left-color: #ef4444; }}

    .item-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }}

    .item-badges {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
    }}

    .item-id {{
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 700;
      color: var(--primary-dark);
    }}

    .item-prompt {{
      font-size: 14.5px;
      font-weight: 600;
      color: var(--text);
      line-height: 1.55;
      margin-bottom: 16px;
    }}

    /* OPTIONS LIST */
    .options-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 8px;
      margin-bottom: 14px;
    }}

    .option-item {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 10px 14px;
      border: 1px solid var(--border);
      border-radius: 8px;
      background: #fafafa;
      font-size: 13.5px;
      line-height: 1.45;
      transition: all 0.15s ease;
    }}

    .option-key {{
      width: 24px;
      height: 24px;
      border-radius: 6px;
      background: var(--surface-subtle);
      border: 1px solid var(--border-dark);
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 12px;
      font-family: var(--font-mono);
      flex-shrink: 0;
      color: var(--text);
    }}

    .option-text {{
      flex: 1;
      padding-top: 1px;
    }}

    .option-item.correct-highlight {{
      background: #ecfdf5;
      border-color: #10b981;
      box-shadow: 0 0 0 1px #10b981;
    }}

    .option-item.correct-highlight .option-key {{
      background: #10b981;
      color: white;
      border-color: #059669;
    }}

    /* TOLT TWO-TIER BOX */
    .tier-box {{
      background: var(--surface-subtle);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 12px 14px;
      margin-bottom: 12px;
    }}

    .tier-title {{
      font-size: 12px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    /* EXPLANATION & HINTS ACCORDION */
    .expand-box {{
      margin-top: 10px;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--border);
    }}

    .expand-header {{
      padding: 9px 12px;
      background: var(--surface-subtle);
      font-size: 12.5px;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      user-select: none;
    }}

    .expand-header:hover {{
      background: #e2e8f0;
      color: var(--text);
    }}

    .expand-body {{
      padding: 12px 14px;
      background: white;
      font-size: 13px;
      line-height: 1.5;
      display: none;
    }}

    .expand-body.open {{
      display: block;
    }}

    .hint-step {{
      margin-bottom: 8px;
      padding-left: 10px;
      border-left: 3px solid var(--primary-light);
    }}

    .hint-step.hint-1 {{ border-left-color: #3b82f6; }}
    .hint-step.hint-2 {{ border-left-color: #f59e0b; }}
    .hint-step.hint-3 {{ border-left-color: #10b981; }}

    .hint-lvl-badge {{
      font-size: 11px;
      font-weight: 800;
      text-transform: uppercase;
      display: inline-block;
      margin-bottom: 2px;
    }}

    /* PAGINATION */
    .pagination-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 20px;
      padding: 12px 16px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
    }}

    .page-buttons {{
      display: flex;
      gap: 4px;
      align-items: center;
    }}

    .page-btn {{
      min-width: 34px;
      height: 34px;
      padding: 0 8px;
      border: 1px solid var(--border);
      background: white;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }}

    .page-btn:hover {{
      background: var(--surface-subtle);
    }}

    .page-btn.active {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}

    /* DAG GRAPH CONTAINER */
    .dag-container {{
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 24px;
      min-height: 540px;
      position: relative;
    }}

    .dag-node-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 20px;
    }}

    .dag-col {{
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}

    .dag-col-title {{
      font-size: 12px;
      font-weight: 800;
      text-transform: uppercase;
      color: var(--text-subtle);
      border-bottom: 2px solid var(--border);
      padding-bottom: 6px;
      letter-spacing: 0.05em;
    }}

    .dag-card {{
      background: white;
      border: 2px solid var(--border);
      border-radius: 10px;
      padding: 14px;
      box-shadow: var(--shadow-sm);
      cursor: pointer;
      transition: all 0.2s ease;
      position: relative;
    }}

    .dag-card:hover {{
      border-color: var(--primary);
      box-shadow: var(--shadow-md);
      transform: translateY(-2px);
    }}

    .dag-card.is-root {{
      border-top: 4px solid #10b981;
    }}

    .dag-card.is-mid {{
      border-top: 4px solid #3b82f6;
    }}

    .dag-card.is-terminal {{
      border-top: 4px solid #ef4444;
    }}

    .dag-card-id {{
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      color: var(--text-subtle);
    }}

    .dag-card-name {{
      font-size: 13.5px;
      font-weight: 700;
      color: var(--text);
      margin: 4px 0 6px;
      line-height: 1.35;
    }}

    .dag-card-meta {{
      font-size: 11px;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    /* QUIZ SIMULATION */
    .quiz-container {{
      max-width: 800px;
      margin: 0 auto;
    }}

    .quiz-option {{
      padding: 12px 16px;
      border: 2px solid var(--border);
      border-radius: 10px;
      margin-bottom: 10px;
      cursor: pointer;
      font-size: 14px;
      display: flex;
      align-items: center;
      gap: 12px;
      background: white;
      transition: all 0.15s ease;
    }}

    .quiz-option:hover {{
      border-color: var(--primary-light);
      background: var(--primary-50);
    }}

    .quiz-option.selected {{
      border-color: var(--primary);
      background: var(--primary-light);
      font-weight: 700;
    }}

    .quiz-feedback {{
      margin-top: 20px;
      padding: 16px 20px;
      border-radius: 10px;
      font-size: 14px;
      line-height: 1.5;
      display: none;
    }}

    .quiz-feedback.correct {{
      background: #ecfdf5;
      border: 1px solid #10b981;
      color: #065f46;
      display: block;
    }}

    .quiz-feedback.incorrect {{
      background: #fef2f2;
      border: 1px solid #ef4444;
      color: #991b1b;
      display: block;
    }}

    /* PRINT STYLES */
    @media print {{
      header, .tab-bar, .filter-bar, .header-actions, .pagination-bar, .btn {{
        display: none !important;
      }}
      body, main {{
        background: white !important;
        color: black !important;
        padding: 0 !important;
        max-width: 100% !important;
      }}
      .card {{
        border: 1px solid #ccc !important;
        box-shadow: none !important;
        page-break-inside: avoid;
      }}
      .tab-pane {{
        display: block !important;
      }}
      .tab-pane:not(#tab-blueprint) {{
        display: none !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- HEADER -->
  <header>
    <div class="header-top">
      <div class="brand-area">
        <div class="brand-icon">🌐</div>
        <div class="brand-title">
          <h1>
            LogiTrace • Data & Bank Soal Explorer
            <span class="badge-tag">L2 Item Bank</span>
          </h1>
          <p>Visualisasi Distribusi & Psikometri 206 Butir Soal Adaptif, TOLT Paralel, dan Kontrol NEDV</p>
        </div>
      </div>
      <div class="header-actions">
        <button class="btn btn-header" onclick="exportDataJson()">
          📥 Ekspor Seluruh Data JSON
        </button>
        <button class="btn btn-header" onclick="window.print()">
          🖨️ Cetak Blueprint Skripsi
        </button>
      </div>
    </div>

    <!-- STATS STRIP -->
    <div class="stats-strip">
      <div class="stat-pill">
        <span class="val" id="stat-total-items">206</span>
        <span class="lbl">Total Butir Soal</span>
      </div>
      <div class="stat-pill">
        <span class="val">180</span>
        <span class="lbl">Bank Adaptif (12 KC)</span>
      </div>
      <div class="stat-pill">
        <span class="val">20</span>
        <span class="lbl">TOLT Paralel (A & B)</span>
      </div>
      <div class="stat-pill">
        <span class="val">6</span>
        <span class="lbl">Kontrol NEDV (C2)</span>
      </div>
      <div class="stat-pill">
        <span class="val">60 / 60 / 60</span>
        <span class="lbl">Mudah / Sedang / Sulit</span>
      </div>
      <div class="stat-pill">
        <span class="val">25% (A/B/C/D)</span>
        <span class="lbl">Zero Position Bias</span>
      </div>
      <div class="stat-pill">
        <span class="val">6</span>
        <span class="lbl">Butir Kalibrasi US-01</span>
      </div>
      <div class="stat-pill">
        <span class="val">36</span>
        <span class="lbl">Scaffolding Hints</span>
      </div>
    </div>
  </header>

  <!-- NAVIGATION TABS -->
  <div class="tab-bar">
    <button class="tab-btn active" onclick="switchTab('dashboard')">
      📊 Ringkasan & Psikometri
    </button>
    <button class="tab-btn" onclick="switchTab('matrix')">
      🗂️ Matriks Pembagian Soal
    </button>
    <button class="tab-btn" onclick="switchTab('dag')">
      🕸️ Graf Prasyarat DAG (12 KC)
    </button>
    <button class="tab-btn" onclick="switchTab('catalog')">
      🔍 Katalog & Explorer Soal <span class="badge-count" id="catalog-count-badge">206</span>
    </button>
    <button class="tab-btn" onclick="switchTab('quiz')">
      🎮 Simulasi Kuis & Hint
    </button>
    <button class="tab-btn" onclick="switchTab('blueprint')">
      📑 Blueprint & Kisi-Kisi Skripsi
    </button>
  </div>

  <!-- MAIN VIEW CONTAINER -->
  <main>

    <!-- TAB 1: DASHBOARD & DISTRIBUSI -->
    <div id="tab-dashboard" class="tab-pane active">
      <div class="grid-2">
        
        <!-- CARD 1: Distribusi KC x Tingkat Kesulitan -->
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">📚 Distribusi Soal per Knowledge Component (KC)</div>
              <div class="card-subtitle">180 Butir Bank Adaptif (12 KC × 15 Butir: 5 Mudah, 5 Sedang, 5 Sulit)</div>
            </div>
            <div style="display: flex; gap: 8px; font-size: 11px;">
              <span class="badge badge-diff-1">● 5 Mudah</span>
              <span class="badge badge-diff-2">● 5 Sedang</span>
              <span class="badge badge-diff-3">● 5 Sulit</span>
            </div>
          </div>
          <div id="kc-distribution-list">
            <!-- Rendered by JS -->
          </div>
        </div>

        <!-- CARD 2: Dimensi Penalaran Logis TOLT -->
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">🧠 Distribusi Dimensi Penalaran Logis (TOLT)</div>
              <div class="card-subtitle">Pemetaan Dimensi Berpikir Formal pada Butir Adaptif & Tes Paralel</div>
            </div>
          </div>
          <div id="tolt-distribution-list">
            <!-- Rendered by JS -->
          </div>

          <div style="margin-top: 24px; padding-top: 16px; border-top: 1px solid var(--border);">
            <div class="card-title" style="font-size: 14.5px; margin-bottom: 8px;">⚖️ Keseimbangan Kunci Jawaban (Zero Position Bias)</div>
            <div class="card-subtitle" style="margin-bottom: 12px;">Pemeriksaan sebaran kunci jawaban A, B, C, D pada 180 butir adaptif:</div>
            <div id="key-balance-bars" style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
              <!-- Rendered by JS -->
            </div>
          </div>
        </div>

      </div>

      <!-- INSTRUMEN PENDUKUNG: TOLT PARALEL & NEDV -->
      <div class="grid-2">
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">📝 Tes Paralel TOLT (Bentuk A & Bentuk B)</div>
              <div class="card-subtitle">Model Two-Tier: Tier 1 Solusi Teknis (A-D) & Tier 2 Alasan Penalaran (1-3)</div>
            </div>
            <span class="badge badge-bank">20 Butir Paralel</span>
          </div>
          <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 14px;">
            Instrumen dirancang untuk pengukuran Pre-test dan Post-test Berpikir Logis. Menggunakan sistem skoring <strong>Polikotomis (0, 1, 2)</strong>:
          </p>
          <div style="background: var(--surface-subtle); padding: 12px 14px; border-radius: 8px; font-size: 12.5px; line-height: 1.6; margin-bottom: 14px;">
            <div>✅ <strong>Skor 2:</strong> Pilihan jawaban benar DAN alasan penalaran logis benar.</div>
            <div>⚠️ <strong>Skor 1:</strong> Pilihan jawaban benar TETAPI alasan penalaran salah.</div>
            <div>❌ <strong>Skor 0:</strong> Pilihan jawaban salah (alasan tidak dihitung).</div>
          </div>
          <div style="display: flex; gap: 10px;">
            <button class="btn btn-outline btn-sm" onclick="filterByBank('tolt_a')">Lihat Form A (10 Butir) →</button>
            <button class="btn btn-outline btn-sm" onclick="filterByBank('tolt_b')">Lihat Form B (10 Butir) →</button>
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">🛡️ Butir Kontrol Non-Equivalent (NEDV)</div>
              <div class="card-subtitle">Pengujian Ancaman Validitas Internal (Threat to Internal Validity C2)</div>
            </div>
            <span class="badge badge-diff-2">6 Butir Kontrol</span>
          </div>
          <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 14px;">
            Butir kontrol NEDV menguji topik kurikulum TKJ yang <strong>tidak diajarkan</strong> pada intervensi adaptif LogiTrace (VoIP & Fiber Optik).
          </p>
          <div style="background: var(--surface-subtle); padding: 12px 14px; border-radius: 8px; font-size: 12.5px; line-height: 1.6; margin-bottom: 14px;">
            <div>• <strong>TP 2.3 Layanan VoIP:</strong> 2 Butir (Protokol SIP & Codec Audio)</div>
            <div>• <strong>TP 2.4 / 2.5 Jaringan Fiber Optik:</strong> 4 Butir (Single Mode, Splicer, OTDR, Power Meter)</div>
            <div style="margin-top: 6px; color: var(--secondary); font-weight: 600;">
              Hipotesis: Nilai N-Gain NEDV terbukti p > 0.05 (tidak naik signifikan), mengonfirmasi isolasi dampak intervensi.
            </div>
          </div>
          <button class="btn btn-outline btn-sm" onclick="filterByBank('nedv')">Lihat 6 Butir NEDV →</button>
        </div>
      </div>
    </div>

    <!-- TAB 2: MATRIKS PEMBAGIAN SOAL -->
    <div id="tab-matrix" class="tab-pane">
      <div class="card">
        <div class="card-header">
          <div>
            <div class="card-title">🗂️ Matriks Pembagian Butir Soal Adaptif (12 KC × 3 Tingkat Kesulitan)</div>
            <div class="card-subtitle">Klik sel mana saja untuk langsung menyaring dan melihat butir soal terkait di Katalog!</div>
          </div>
          <div style="display: flex; gap: 8px;">
            <button class="btn btn-outline btn-sm" onclick="resetAndGoToCatalog()">Lihat Semua 180 Butir</button>
          </div>
        </div>

        <div class="table-container">
          <table class="matrix-table" id="matrix-table-kc">
            <thead>
              <tr>
                <th style="width: 50px;">No</th>
                <th style="width: 200px;">Knowledge Component (KC)</th>
                <th>Nama Kompetensi</th>
                <th style="text-align: center; width: 120px;">Level 1 (Mudah)</th>
                <th style="text-align: center; width: 120px;">Level 2 (Sedang)</th>
                <th style="text-align: center; width: 120px;">Level 3 (Sulit)</th>
                <th style="text-align: center; width: 100px;">Total</th>
                <th style="text-align: center; width: 120px;">Aksi</th>
              </tr>
            </thead>
            <tbody id="matrix-tbody">
              <!-- Rendered by JS -->
            </tbody>
            <tfoot>
              <tr style="background: var(--surface-subtle); font-weight: 800;">
                <td colspan="3" style="text-align: right; padding-right: 16px;">TOTAL DISTRIBUSI</td>
                <td style="text-align: center; font-family: var(--font-mono); color: #047857;">60 Butir (33.3%)</td>
                <td style="text-align: center; font-family: var(--font-mono); color: #b45309;">60 Butir (33.3%)</td>
                <td style="text-align: center; font-family: var(--font-mono); color: #b91c1c;">60 Butir (33.3%)</td>
                <td style="text-align: center; font-family: var(--font-mono); font-size: 14px;">180 Butir</td>
                <td style="text-align: center;">-</td>
              </tr>
            </tfoot>
          </table>
        </div>
      </div>

      <!-- MATRIKS KEDUA: KC x TOLT DIMS -->
      <div class="card" style="margin-top: 24px;">
        <div class="card-header">
          <div>
            <div class="card-title">🧩 Matriks Silang KC × 5 Dimensi TOLT</div>
            <div class="card-subtitle">Sebaran dimensi penalaran logis pada masing-masing topik pembelajaran</div>
          </div>
        </div>
        <div class="table-container">
          <table class="matrix-table" id="matrix-tolt-kc">
            <thead>
              <tr>
                <th style="width: 220px;">Knowledge Component</th>
                <th style="text-align: center;">Controlling Variables</th>
                <th style="text-align: center;">Proportional</th>
                <th style="text-align: center;">Combinatorial</th>
                <th style="text-align: center;">Probabilistic</th>
                <th style="text-align: center;">Correlational</th>
                <th style="text-align: center; width: 80px;">Total</th>
              </tr>
            </thead>
            <tbody id="matrix-tolt-tbody">
              <!-- Rendered by JS -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- TAB 3: DAG GRAPH -->
    <div id="tab-dag" class="tab-pane">
      <div class="card">
        <div class="card-header">
          <div>
            <div class="card-title">🕸️ Alur Prasyarat Graf Pengetahuan (Directed Acyclic Graph)</div>
            <div class="card-subtitle">Struktur Prasyarat 12 KC: 3 Root KCs → Jalur Propagasi → Terminal Troubleshooting</div>
          </div>
          <div style="font-size: 12px; color: var(--text-muted);">
            💡 Klik kartu KC di bawah untuk melihat rincian prasyarat dan memfilter soalnya!
          </div>
        </div>

        <div class="dag-container">
          <div class="dag-node-grid">
            <!-- Kolom 1: Root KCs -->
            <div class="dag-col">
              <div class="dag-col-title">🌱 Layer 0: Root Concepts (In-degree 0)</div>
              <div id="dag-col-0"></div>
            </div>

            <!-- Kolom 2: Layer 1 -->
            <div class="dag-col">
              <div class="dag-col-title">🌿 Layer 1: Core Physical & Channel</div>
              <div id="dag-col-1"></div>
            </div>

            <!-- Kolom 3: Layer 2 -->
            <div class="dag-col">
              <div class="dag-col-title">🌲 Layer 2: Protocol & Security</div>
              <div id="dag-col-2"></div>
            </div>

            <!-- Kolom 4: Layer 3 -->
            <div class="dag-col">
              <div class="dag-col-title">🎯 Layer 3: Troubleshooting Diagnostik</div>
              <div id="dag-col-3"></div>
            </div>
          </div>
        </div>

        <!-- DETAIL KC TERPILIH DI DAG -->
        <div id="dag-selected-detail" style="margin-top: 20px; display: none;" class="card">
          <div class="card-header">
            <div>
              <span class="badge badge-kc" id="dag-det-id">KC_ID</span>
              <h3 id="dag-det-name" style="margin-top: 4px; font-size: 16px;">Nama KC</h3>
            </div>
            <button class="btn btn-primary btn-sm" id="dag-btn-view-items">Lihat 15 Soal KC Ini →</button>
          </div>
          <p id="dag-det-desc" style="font-size: 13.5px; color: var(--text-muted); margin-bottom: 14px;"></p>
          
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
            <div style="background: var(--surface-subtle); padding: 12px; border-radius: 8px;">
              <div style="font-size: 11px; font-weight: 800; color: var(--text-subtle); text-transform: uppercase;">Prasyarat Langsung (Prerequisites)</div>
              <div id="dag-det-prereq" style="margin-top: 6px; font-size: 13px;">-</div>
            </div>
            <div style="background: var(--surface-subtle); padding: 12px; border-radius: 8px;">
              <div style="font-size: 11px; font-weight: 800; color: var(--text-subtle); text-transform: uppercase;">Materi Lanjutan (Dependents)</div>
              <div id="dag-det-dependents" style="margin-top: 6px; font-size: 13px;">-</div>
            </div>
          </div>

          <!-- STATIC HINTS PREVIEW -->
          <div style="margin-top: 14px;">
            <div style="font-size: 12px; font-weight: 700; color: var(--text-muted); margin-bottom: 8px;">Fallback Scaffolding Hints untuk KC Ini:</div>
            <div id="dag-det-hints" style="display: flex; flex-direction: column; gap: 6px;"></div>
          </div>
        </div>

      </div>
    </div>

    <!-- TAB 4: KATALOG & EXPLORER SOAL -->
    <div id="tab-catalog" class="tab-pane">
      
      <!-- FILTER BAR -->
      <div class="filter-bar">
        <div class="filter-row">
          <div class="search-input-wrap">
            <span class="search-icon">🔍</span>
            <input type="text" id="search-box" class="search-input" placeholder="Cari teks soal, ID, kata kunci, opsi jawaban..." oninput="handleSearch()">
          </div>

          <!-- FILTER BANK INSTRUMEN -->
          <select id="filter-bank" class="select-filter" onchange="applyFilters()">
            <option value="all">Semua Instrumen (206 Butir)</option>
            <option value="adaptive">Bank Adaptif (180 Butir)</option>
            <option value="tolt_a">TOLT Bentuk A (10 Butir)</option>
            <option value="tolt_b">TOLT Bentuk B (10 Butir)</option>
            <option value="nedv">Kontrol NEDV (6 Butir)</option>
          </select>

          <!-- FILTER KC -->
          <select id="filter-kc" class="select-filter" onchange="applyFilters()">
            <option value="all">Semua Knowledge Component</option>
          </select>

          <!-- FILTER KESULITAN -->
          <select id="filter-diff" class="select-filter" onchange="applyFilters()">
            <option value="all">Semua Tingkat Kesulitan</option>
            <option value="1">Level 1 (Mudah)</option>
            <option value="2">Level 2 (Sedang)</option>
            <option value="3">Level 3 (Sulit)</option>
          </select>

          <!-- FILTER DIMENSI TOLT -->
          <select id="filter-tolt" class="select-filter" onchange="applyFilters()">
            <option value="all">Semua Dimensi TOLT</option>
            <option value="CONTROLLING_VARIABLES">Controlling Variables</option>
            <option value="PROPORTIONAL_REASONING">Proportional Reasoning</option>
            <option value="COMBINATORIAL_REASONING">Combinatorial Reasoning</option>
            <option value="PROBABILISTIC_REASONING">Probabilistic Reasoning</option>
            <option value="CORRELATIONAL_REASONING">Correlational Reasoning</option>
          </select>

          <button class="btn btn-outline btn-sm" onclick="resetFilters()">Reset Filter</button>
        </div>

        <div class="filter-row" style="justify-content: space-between; border-top: 1px solid var(--border); padding-top: 10px;">
          <div style="display: flex; align-items: center; gap: 14px;">
            <label style="display: flex; align-items: center; gap: 6px; font-size: 13px; cursor: pointer; user-select: none;">
              <input type="checkbox" id="filter-calib-only" onchange="applyFilters()">
              Hanya Butir Kalibrasi Standar (US-01)
            </label>
            <label style="display: flex; align-items: center; gap: 6px; font-size: 13px; cursor: pointer; user-select: none;">
              <input type="checkbox" id="toggle-reveal-keys" onchange="toggleAllKeys(this.checked)" checked>
              Tampilkan Kunci & Penjelasan
            </label>
          </div>

          <div style="display: flex; align-items: center; gap: 10px;">
            <span class="filter-stats-text" id="filter-results-info">Menampilkan 206 butir</span>
            <select id="items-per-page" class="select-filter" style="padding: 5px 8px; font-size: 12px;" onchange="changePageSize(this.value)">
              <option value="15">15 per hal</option>
              <option value="30" selected>30 per hal</option>
              <option value="60">60 per hal</option>
              <option value="all">Tampilkan Semua</option>
            </select>
          </div>
        </div>
      </div>

      <!-- ITEM LIST CONTAINER -->
      <div id="item-list-container">
        <!-- Rendered by JS -->
      </div>

      <!-- PAGINATION BAR -->
      <div class="pagination-bar" id="pagination-bar">
        <div style="font-size: 13px; color: var(--text-muted);" id="page-info-text">
          Halaman 1 dari 7
        </div>
        <div class="page-buttons" id="page-buttons-container">
          <!-- Buttons rendered by JS -->
        </div>
      </div>

    </div>

    <!-- TAB 5: SIMULASI KUIS & HINT -->
    <div id="tab-quiz" class="tab-pane">
      <div class="quiz-container">
        <div class="card">
          <div class="card-header">
            <div>
              <div class="card-title">🎮 Simulasi Pengerjaan & Scaffolding Adaptif LogiTrace</div>
              <div class="card-subtitle">Uji coba interaktif butir soal dengan sistem petunjuk bertingkat (Hint 1 → 2 → 3)</div>
            </div>
            <button class="btn btn-outline btn-sm" onclick="loadRandomQuizItem()">🎲 Ambil Soal Acak Lain</button>
          </div>

          <div style="margin-bottom: 14px; display: flex; gap: 8px; flex-wrap: wrap;" id="quiz-badges">
            <!-- Badges -->
          </div>

          <div id="quiz-prompt" style="font-size: 16px; font-weight: 700; line-height: 1.5; margin-bottom: 20px;">
            <!-- Prompt -->
          </div>

          <div id="quiz-options-container">
            <!-- Options -->
          </div>

          <!-- TOLT TIER 2 IF TOLT ITEM -->
          <div id="quiz-tier2-container" style="display: none; margin-top: 16px; border-top: 1px solid var(--border); padding-top: 16px;">
            <div style="font-size: 14px; font-weight: 700; margin-bottom: 10px;">Pilihan Alasan Penalaran (Tier 2):</div>
            <div id="quiz-tier2-options"></div>
          </div>

          <div style="display: flex; gap: 10px; margin-top: 20px;">
            <button class="btn btn-primary" id="btn-submit-quiz" onclick="checkQuizAnswer()">Periksa Jawaban</button>
            <button class="btn btn-outline" id="btn-open-hint" onclick="revealNextHint()" style="display: none;">
              💡 Buka Hint Scaffolding (<span id="hint-lvl-text">Level 1</span>)
            </button>
          </div>

          <!-- FEEDBACK BOX -->
          <div id="quiz-feedback-box" class="quiz-feedback">
            <div id="quiz-feedback-title" style="font-weight: 800; font-size: 15px; margin-bottom: 4px;"></div>
            <div id="quiz-feedback-explanation"></div>
          </div>

          <!-- HINTS DISPLAY ACCORDION -->
          <div id="quiz-hints-revealed" style="margin-top: 16px; display: flex; flex-direction: column; gap: 8px;">
            <!-- Hints -->
          </div>

        </div>
      </div>
    </div>

    <!-- TAB 6: BLUEPRINT & KISI-KISI SKRIPSI -->
    <div id="tab-blueprint" class="tab-pane">
      <div class="card">
        <div class="card-header">
          <div>
            <div class="card-title">📑 Kisi-Kisi & Blueprint Instrumen Penelitian Skripsi</div>
            <div class="card-subtitle">Format tabel formal untuk Bab III Metodologi Penelitian & Lampiran Skripsi</div>
          </div>
          <div style="display: flex; gap: 10px;">
            <button class="btn btn-outline btn-sm" onclick="exportTableCsv()">📥 Unduh Kisi-Kisi (.CSV)</button>
            <button class="btn btn-primary btn-sm" onclick="window.print()">🖨️ Cetak Lampiran</button>
          </div>
        </div>

        <div class="table-container">
          <table class="matrix-table" id="blueprint-table">
            <thead>
              <tr>
                <th style="width: 40px;">No</th>
                <th style="width: 140px;">ID Butir</th>
                <th style="width: 110px;">Tipe Bank</th>
                <th style="width: 180px;">Knowledge Component / Topik</th>
                <th>Dimensi Penalaran Logis (TOLT)</th>
                <th style="text-align: center; width: 90px;">Kesulitan</th>
                <th style="text-align: center; width: 70px;">Kunci</th>
                <th style="text-align: center; width: 80px;">Kalibrasi</th>
              </tr>
            </thead>
            <tbody id="blueprint-tbody">
              <!-- Rendered by JS -->
            </tbody>
          </table>
        </div>
      </div>
    </div>

  </main>

  <!-- EMBEDDED DATASET SCRIPT -->
  <script>
    // Embedded JSON Database from apps/logitrace/data
    const DB = {db_json};

    // State
    let allItems = [];
    let filteredItems = [];
    let currentPage = 1;
    let pageSize = 30;
    let revealAllKeys = true;
    let currentQuizItem = null;
    let quizSelectedOption = null;
    let quizSelectedReasoning = null;
    let currentHintLevel = 0;

    // Initialization
    window.addEventListener("DOMContentLoaded", () => {{
      initDataset();
      renderDashboard();
      renderMatrix();
      renderDag();
      initCatalogFilters();
      applyFilters();
      renderBlueprintTable();
      loadRandomQuizItem();
    }});

    // 1. UNIFY DATASET
    function initDataset() {{
      allItems = [];

      // A. Adaptive 180 Items
      DB.adaptive.forEach(item => {{
        allItems.push({{
          bank: "adaptive",
          bankLabel: "Bank Adaptif",
          id: item.id,
          sequence_id: item.sequence_id,
          kc: item.primary_kc,
          difficulty: item.difficulty,
          tolt_dim: item.tolt_dimension,
          is_calib: !!item.is_calibration,
          prompt: item.prompt_text,
          options: item.options,
          correct_answer: item.correct_answer,
          explanation: item.explanation
        }});
      }});

      // B. TOLT Form A
      DB.tolt.form_a.forEach((item, idx) => {{
        allItems.push({{
          bank: "tolt_a",
          bankLabel: "TOLT Form A",
          id: item.id,
          sequence_id: 200 + idx,
          kc: "TOLT_FORMAL_REASONING",
          difficulty: 2,
          tolt_dim: item.dimension,
          is_calib: false,
          prompt: item.prompt,
          options: item.options,
          correct_answer: item.correct_option,
          reasoning_options: item.reasoning_options,
          correct_reasoning: item.correct_reasoning,
          explanation: "Instrumen TOLT Form A (Two-Tier Logika Formal). Kunci Opsi: " + item.correct_option + ", Kunci Alasan: " + item.correct_reasoning
        }});
      }});

      // C. TOLT Form B
      DB.tolt.form_b.forEach((item, idx) => {{
        allItems.push({{
          bank: "tolt_b",
          bankLabel: "TOLT Form B",
          id: item.id,
          sequence_id: 220 + idx,
          kc: "TOLT_FORMAL_REASONING",
          difficulty: 2,
          tolt_dim: item.dimension,
          is_calib: false,
          prompt: item.prompt,
          options: item.options,
          correct_answer: item.correct_option,
          reasoning_options: item.reasoning_options,
          correct_reasoning: item.correct_reasoning,
          explanation: "Instrumen TOLT Form B (Two-Tier Logika Formal). Kunci Opsi: " + item.correct_option + ", Kunci Alasan: " + item.correct_reasoning
        }});
      }});

      // D. NEDV Control 6 Items
      DB.nedv.items.forEach((item, idx) => {{
        allItems.push({{
          bank: "nedv",
          bankLabel: "Kontrol NEDV",
          id: item.id,
          sequence_id: 300 + idx,
          kc: item.curriculum_element.split(" - ")[0].replace(" ", "_"),
          topic: item.topic,
          difficulty: 2,
          tolt_dim: "CONTROLLING_VARIABLES",
          is_calib: false,
          prompt: item.prompt,
          options: item.options,
          correct_answer: item.correct_answer,
          explanation: item.explanation
        }});
      }});

      filteredItems = [...allItems];
      document.getElementById("stat-total-items").innerText = allItems.length;
    }}

    // TAB NAVIGATION
    function switchTab(tabId) {{
      document.querySelectorAll(".tab-pane").forEach(p => p.classList.remove("active"));
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      
      const targetPane = document.getElementById("tab-" + tabId);
      if (targetPane) targetPane.classList.add("active");

      // Active state on button
      const buttons = document.querySelectorAll(".tab-btn");
      buttons.forEach(btn => {{
        if (btn.getAttribute("onclick").includes("'" + tabId + "'")) {{
          btn.classList.add("active");
        }}
      }});
      window.scrollTo({{ top: 0, behavior: "smooth" }});
    }}

    // RENDER DASHBOARD
    function renderDashboard() {{
      // 1. KC Distribution
      const kcListEl = document.getElementById("kc-distribution-list");
      kcListEl.innerHTML = "";

      DB.kcs.forEach(kc => {{
        const itemsThisKc = DB.adaptive.filter(i => i.primary_kc === kc.id);
        const easy = itemsThisKc.filter(i => i.difficulty === 1).length;
        const med = itemsThisKc.filter(i => i.difficulty === 2).length;
        const hard = itemsThisKc.filter(i => i.difficulty === 3).length;
        const total = itemsThisKc.length;

        const row = document.createElement("div");
        row.className = "dist-row";
        row.innerHTML = `
          <div class="dist-label" title="${{kc.name}} (${{kc.id}})">${{kc.name}}</div>
          <div class="dist-bar-wrap" title="Mudah: ${{easy}}, Sedang: ${{med}}, Sulit: ${{hard}}">
            <div class="dist-segment bg-easy" style="width: 33.33%;">5</div>
            <div class="dist-segment bg-med" style="width: 33.33%;">5</div>
            <div class="dist-segment bg-hard" style="width: 33.34%;">5</div>
          </div>
          <div class="dist-val">${{total}} Butir</div>
        `;
        kcListEl.appendChild(row);
      }});

      // 2. TOLT Distribution
      const toltListEl = document.getElementById("tolt-distribution-list");
      toltListEl.innerHTML = "";

      const toltCounts = {{}};
      DB.dims.forEach(d => toltCounts[d.id] = 0);
      DB.adaptive.forEach(i => {{
        if (toltCounts[i.tolt_dimension] !== undefined) toltCounts[i.tolt_dimension]++;
      }});

      const maxTolt = Math.max(...Object.values(toltCounts), 45);

      DB.dims.forEach(d => {{
        const cnt = toltCounts[d.id] || 0;
        const pct = ((cnt / DB.adaptive.length) * 100).toFixed(1);
        const barWidth = ((cnt / maxTolt) * 100).toFixed(0);

        const row = document.createElement("div");
        row.className = "dist-row";
        row.innerHTML = `
          <div class="dist-label" title="${{d.name}}">${{d.name.split(" (")[0]}}</div>
          <div class="dist-bar-wrap">
            <div class="dist-segment" style="width: ${{barWidth}}%; background: #4338ca;">${{cnt}}</div>
          </div>
          <div class="dist-val">${{pct}}%</div>
        `;
        toltListEl.appendChild(row);
      }});

      // 3. Key Balance Bars
      const keyBalanceEl = document.getElementById("key-balance-bars");
      keyBalanceEl.innerHTML = "";
      const keys = ["A", "B", "C", "D"];
      const keyCounts = {{ "A": 0, "B": 0, "C": 0, "D": 0 }};
      DB.adaptive.forEach(i => {{
        if (keyCounts[i.correct_answer] !== undefined) keyCounts[i.correct_answer]++;
      }});

      keys.forEach(k => {{
        const cnt = keyCounts[k] || 0;
        const pct = ((cnt / DB.adaptive.length) * 100).toFixed(1);
        const box = document.createElement("div");
        box.style.cssText = "background: var(--surface-subtle); padding: 12px; border-radius: 8px; text-align: center; border: 1px solid var(--border);";
        box.innerHTML = `
          <div style="font-family: var(--font-mono); font-size: 18px; font-weight: 800; color: var(--primary);">${{k}}</div>
          <div style="font-size: 14px; font-weight: 700; color: var(--text); margin: 2px 0;">${{cnt}} Butir</div>
          <div style="font-size: 11px; color: var(--text-muted);">${{pct}}% (Ideal 25%)</div>
        `;
        keyBalanceEl.appendChild(box);
      }});
    }}

    // RENDER MATRIX TABLE
    function renderMatrix() {{
      const tbody = document.getElementById("matrix-tbody");
      tbody.innerHTML = "";

      DB.kcs.forEach((kc, idx) => {{
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td style="color: var(--text-muted); font-family: var(--font-mono);">${{idx + 1}}</td>
          <td><span class="badge badge-kc">${{kc.id}}</span></td>
          <td style="font-weight: 600;">${{kc.name}}</td>
          <td style="text-align: center;">
            <span class="matrix-cell cell-easy" onclick="filterByKcAndDiff('${{kc.id}}', 1)" title="Klik untuk filter 5 Soal Mudah">5</span>
          </td>
          <td style="text-align: center;">
            <span class="matrix-cell cell-med" onclick="filterByKcAndDiff('${{kc.id}}', 2)" title="Klik untuk filter 5 Soal Sedang">5</span>
          </td>
          <td style="text-align: center;">
            <span class="matrix-cell cell-hard" onclick="filterByKcAndDiff('${{kc.id}}', 3)" title="Klik untuk filter 5 Soal Sulit">5</span>
          </td>
          <td style="text-align: center; font-weight: 700; font-family: var(--font-mono);">15</td>
          <td style="text-align: center;">
            <button class="btn btn-outline btn-sm" onclick="filterByKcOnly('${{kc.id}}')">Lihat Soal →</button>
          </td>
        `;
        tbody.appendChild(tr);
      }});

      // Secondary Matrix: KC x TOLT
      const toltTbody = document.getElementById("matrix-tolt-tbody");
      toltTbody.innerHTML = "";

      const dimKeys = [
        "CONTROLLING_VARIABLES",
        "PROPORTIONAL_REASONING",
        "COMBINATORIAL_REASONING",
        "PROBABILISTIC_REASONING",
        "CORRELATIONAL_REASONING"
      ];

      DB.kcs.forEach(kc => {{
        const items = DB.adaptive.filter(i => i.primary_kc === kc.id);
        const counts = {{}};
        dimKeys.forEach(k => counts[k] = 0);
        items.forEach(i => {{
          if (counts[i.tolt_dimension] !== undefined) counts[i.tolt_dimension]++;
        }});

        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td style="font-weight: 600;">${{kc.name}}</td>
          ${{dimKeys.map(k => `
            <td style="text-align: center;">
              <span class="badge badge-tolt" style="cursor: pointer;" onclick="filterByKcAndTolt('${{kc.id}}', '${{k}}')">
                ${{counts[k]}}
              </span>
            </td>
          `).join("")}}
          <td style="text-align: center; font-weight: 700; font-family: var(--font-mono);">15</td>
        `;
        toltTbody.appendChild(tr);
      }});
    }}

    // RENDER DAG
    function renderDag() {{
      const layers = [
        ["WLAN_STANDARDS", "WLAN_TOPOLOGY_BSS", "IP_PEER_CONFIG"],
        ["WLAN_FREQ_CHANNEL", "WLAN_SIGNAL_PROP"],
        ["WLAN_CHANNEL_COLLISION", "WLAN_SECURITY_AUTH", "WLAN_ROAMING_PROB"],
        ["WLAN_HOST_HARDENING", "ICMP_CONNECTIVITY", "ICMP_TROUBLE_DHU", "ICMP_TROUBLE_RTO"]
      ];

      layers.forEach((layerKcs, colIdx) => {{
        const colEl = document.getElementById("dag-col-" + colIdx);
        if (!colEl) return;
        colEl.innerHTML = "";

        layerKcs.forEach(kcId => {{
          const kcObj = DB.kcs.find(k => k.id === kcId);
          if (!kcObj) return;

          const card = document.createElement("div");
          const cardTypeClass = colIdx === 0 ? "is-root" : (colIdx === 3 ? "is-terminal" : "is-mid");
          card.className = "dag-card " + cardTypeClass;
          card.onclick = () => showDagDetail(kcId);

          card.innerHTML = `
            <div class="dag-card-id">${{kcId}}</div>
            <div class="dag-card-name">${{kcObj.name}}</div>
            <div class="dag-card-meta">
              <span>📚 15 Butir</span>
              <span>🔗 Prasyarat: ${{kcObj.prerequisites.length ? kcObj.prerequisites.length : 'Root'}}</span>
            </div>
          `;
          colEl.appendChild(card);
        }});
      }});
    }}

    function showDagDetail(kcId) {{
      const kcObj = DB.kcs.find(k => k.id === kcId);
      if (!kcObj) return;

      const detailEl = document.getElementById("dag-selected-detail");
      detailEl.style.display = "block";

      document.getElementById("dag-det-id").innerText = kcObj.id;
      document.getElementById("dag-det-name").innerText = kcObj.name;
      document.getElementById("dag-det-desc").innerText = kcObj.description;

      // Prerequisites
      const prereqEl = document.getElementById("dag-det-prereq");
      if (kcObj.prerequisites.length === 0) {{
        prereqEl.innerHTML = `<span style="color: #059669; font-weight: 700;">🌱 Root Concept (Tanpa Prasyarat)</span>`;
      }} else {{
        prereqEl.innerHTML = kcObj.prerequisites.map(p => `<span class="badge badge-kc">${{p}}</span>`).join(" ");
      }}

      // Dependents (Edges where from == kcId)
      const depKcs = DB.dag.edges.filter(e => e.from === kcId).map(e => e.to);
      const depEl = document.getElementById("dag-det-dependents");
      if (depKcs.length === 0) {{
        depEl.innerHTML = `<span style="color: #b91c1c; font-weight: 700;">🎯 Terminal Troubleshooting Concept</span>`;
      }} else {{
        depEl.innerHTML = depKcs.map(d => `<span class="badge badge-kc">${{d}}</span>`).join(" ");
      }}

      // Hints
      const hintsEl = document.getElementById("dag-det-hints");
      hintsEl.innerHTML = "";
      const kcHints = DB.hints[kcId] || {{}};
      [1, 2, 3].forEach(lvl => {{
        if (kcHints[lvl]) {{
          const hDiv = document.createElement("div");
          hDiv.className = `hint-step hint-${{lvl}}`;
          hDiv.innerHTML = `
            <span class="hint-lvl-badge" style="color: ${{lvl===1?'#2563eb':lvl===2?'#d97706':'#059669'}}">Petunjuk Level ${{lvl}}:</span>
            <div style="font-size: 12.5px;">${{kcHints[lvl]}}</div>
          `;
          hintsEl.appendChild(hDiv);
        }}
      }});

      const btnView = document.getElementById("dag-btn-view-items");
      btnView.onclick = () => filterByKcOnly(kcId);
      detailEl.scrollIntoView({{ behavior: "smooth", block: "nearest" }});
    }}

    // CATALOG & FILTERS
    function initCatalogFilters() {{
      const kcSelect = document.getElementById("filter-kc");
      kcSelect.innerHTML = `<option value="all">Semua Knowledge Component</option>`;
      DB.kcs.forEach(kc => {{
        const opt = document.createElement("option");
        opt.value = kc.id;
        opt.innerText = `${{kc.name}} (${{kc.id}})`;
        kcSelect.appendChild(opt);
      }});
    }}

    function applyFilters() {{
      const bankVal = document.getElementById("filter-bank").value;
      const kcVal = document.getElementById("filter-kc").value;
      const diffVal = document.getElementById("filter-diff").value;
      const toltVal = document.getElementById("filter-tolt").value;
      const calibOnly = document.getElementById("filter-calib-only").checked;
      const searchVal = document.getElementById("search-box").value.trim().toLowerCase();

      filteredItems = allItems.filter(item => {{
        // Bank
        if (bankVal !== "all" && item.bank !== bankVal) return false;
        // KC
        if (kcVal !== "all" && item.kc !== kcVal) return false;
        // Diff
        if (diffVal !== "all" && item.difficulty.toString() !== diffVal) return false;
        // TOLT
        if (toltVal !== "all" && item.tolt_dim !== toltVal) return false;
        // Calib
        if (calibOnly && !item.is_calib) return false;
        // Search
        if (searchVal) {{
          const str = (
            item.id + " " +
            item.prompt + " " +
            Object.values(item.options || {{}}).join(" ") + " " +
            (item.explanation || "") + " " +
            (item.kc || "")
          ).toLowerCase();
          if (!str.includes(searchVal)) return false;
        }}
        return true;
      }});

      currentPage = 1;
      renderCatalog();
    }}

    function handleSearch() {{
      applyFilters();
    }}

    function resetFilters() {{
      document.getElementById("filter-bank").value = "all";
      document.getElementById("filter-kc").value = "all";
      document.getElementById("filter-diff").value = "all";
      document.getElementById("filter-tolt").value = "all";
      document.getElementById("filter-calib-only").checked = false;
      document.getElementById("search-box").value = "";
      applyFilters();
    }}

    function filterByKcOnly(kcId) {{
      switchTab("catalog");
      resetFilters();
      document.getElementById("filter-kc").value = kcId;
      applyFilters();
    }}

    function filterByKcAndDiff(kcId, diff) {{
      switchTab("catalog");
      resetFilters();
      document.getElementById("filter-kc").value = kcId;
      document.getElementById("filter-diff").value = diff.toString();
      applyFilters();
    }}

    function filterByKcAndTolt(kcId, toltDim) {{
      switchTab("catalog");
      resetFilters();
      document.getElementById("filter-kc").value = kcId;
      document.getElementById("filter-tolt").value = toltDim;
      applyFilters();
    }}

    function filterByBank(bankId) {{
      switchTab("catalog");
      resetFilters();
      document.getElementById("filter-bank").value = bankId;
      applyFilters();
    }}

    function resetAndGoToCatalog() {{
      switchTab("catalog");
      resetFilters();
    }}

    function changePageSize(val) {{
      pageSize = val === "all" ? 9999 : parseInt(val, 10);
      currentPage = 1;
      renderCatalog();
    }}

    function toggleAllKeys(show) {{
      revealAllKeys = show;
      renderCatalog();
    }}

    // RENDER CATALOG ITEMS
    function renderCatalog() {{
      const container = document.getElementById("item-list-container");
      container.innerHTML = "";

      const total = filteredItems.length;
      document.getElementById("filter-results-info").innerText = `Menampilkan ${{total}} butir`;
      document.getElementById("catalog-count-badge").innerText = total;

      if (total === 0) {{
        container.innerHTML = `
          <div style="text-align: center; padding: 48px; background: white; border-radius: 12px; border: 1px dashed var(--border-dark);">
            <div style="font-size: 32px; margin-bottom: 8px;">🔍</div>
            <div style="font-size: 16px; font-weight: 700;">Tidak ada butir soal yang cocok dengan filter</div>
            <p style="font-size: 13px; color: var(--text-muted); margin-top: 4px;">Coba ubah kriteria pencarian atau klik Reset Filter.</p>
            <button class="btn btn-outline btn-sm" style="margin-top: 14px;" onclick="resetFilters()">Reset Filter</button>
          </div>
        `;
        document.getElementById("pagination-bar").style.display = "none";
        return;
      }}

      document.getElementById("pagination-bar").style.display = "flex";

      // Pagination slice
      const startIdx = (currentPage - 1) * pageSize;
      const endIdx = startIdx + pageSize;
      const pagedItems = filteredItems.slice(startIdx, endIdx);

      pagedItems.forEach(item => {{
        const card = document.createElement("div");
        card.className = `item-card diff-border-${{item.difficulty}}`;

        const diffLabel = item.difficulty === 1 ? "Mudah (L1)" : (item.difficulty === 2 ? "Sedang (L2)" : "Sulit (L3)");
        const kcObj = DB.kcs.find(k => k.id === item.kc);
        const kcName = kcObj ? kcObj.name : item.kc;

        // Header
        card.innerHTML = `
          <div class="item-header">
            <div class="item-badges">
              <span class="item-id">${{item.id}}</span>
              <span class="badge badge-diff-${{item.difficulty}}">${{diffLabel}}</span>
              <span class="badge badge-kc" title="${{kcName}}">${{item.kc}}</span>
              <span class="badge badge-tolt">${{item.tolt_dim}}</span>
              ${{item.is_calib ? '<span class="badge badge-calib">⭐ Kalibrasi US-01</span>' : ''}}
              <span class="badge badge-bank">${{item.bankLabel}}</span>
            </div>
            <div style="display: flex; gap: 6px;">
              <button class="btn btn-outline btn-sm" onclick="copyItemText('${{item.id}}')">📋 Salin Teks</button>
              <button class="btn btn-outline btn-sm" onclick="tryInQuiz('${{item.id}}')">🎮 Coba Soal</button>
            </div>
          </div>

          <div class="item-prompt">${{item.prompt}}</div>

          <!-- PILIHAN JAWABAN TIER 1 -->
          <div class="options-grid">
            ${{Object.entries(item.options || {{}}).map(([k, text]) => {{
              const isCorrect = (k === item.correct_answer);
              const highlightClass = (revealAllKeys && isCorrect) ? "correct-highlight" : "";
              return `
                <div class="option-item ${{highlightClass}}">
                  <div class="option-key">${{k}}</div>
                  <div class="option-text">${{text}}</div>
                  ${{(revealAllKeys && isCorrect) ? '<span style="color: #059669; font-weight: 800; font-size: 13px;">✓ Kunci</span>' : ''}}
                </div>
              `;
            }}).join("")}}
          </div>

          <!-- JIKA TOLT: TAMPILKAN TIER 2 REASONING -->
          ${{item.reasoning_options ? `
            <div class="tier-box">
              <div class="tier-title">Tier 2: Alasan Penalaran Logis (Two-Tier TOLT)</div>
              <div class="options-grid" style="margin-bottom: 0;">
                ${{Object.entries(item.reasoning_options).map(([rk, rtext]) => {{
                  const isRCorrect = (rk === item.correct_reasoning);
                  const rHighlight = (revealAllKeys && isRCorrect) ? "correct-highlight" : "";
                  return `
                    <div class="option-item ${{rHighlight}}">
                      <div class="option-key">${{rk}}</div>
                      <div class="option-text">${{rtext}}</div>
                      ${{(revealAllKeys && isRCorrect) ? '<span style="color: #059669; font-weight: 800; font-size: 13px;">✓ Alasan Benar</span>' : ''}}
                    </div>
                  `;
                }}).join("")}}
              </div>
            </div>
          ` : ''}}

          <!-- EXPLANATION & HINTS ACCORDION -->
          <div class="expand-box">
            <div class="expand-header" onclick="toggleAccordion(this)">
              <span>💡 Penjelasan Rasional & Scaffolding Hints</span>
              <span>▼</span>
            </div>
            <div class="expand-body ${{revealAllKeys ? 'open' : ''}}">
              <div style="margin-bottom: 10px;">
                <strong style="color: var(--primary);">Penjelasan Pedagogis:</strong>
                <div style="margin-top: 4px; color: var(--text-muted);">${{item.explanation || "Tidak ada pembahasan khusus."}}</div>
              </div>

              ${{getHintsHtmlForItem(item.kc)}}
            </div>
          </div>
        `;

        container.appendChild(card);
      }});

      renderPagination(total);
    }}

    function getHintsHtmlForItem(kcId) {{
      const hints = DB.hints[kcId];
      if (!hints) return "";
      return `
        <div style="border-top: 1px dashed var(--border); padding-top: 8px; margin-top: 8px;">
          <div style="font-size: 11.5px; font-weight: 700; color: var(--text-subtle); margin-bottom: 6px;">
            SCAFFOLDING PETUNJUK BERTINGKAT (${{kcId}}):
          </div>
          <div class="hint-step hint-1">
            <span class="hint-lvl-badge" style="color: #2563eb;">Petunjuk 1 (Konseptual):</span>
            <div style="font-size: 12.5px; color: var(--text-muted);">${{hints["1"]}}</div>
          </div>
          <div class="hint-step hint-2">
            <span class="hint-lvl-badge" style="color: #d97706;">Petunjuk 2 (Analitis):</span>
            <div style="font-size: 12.5px; color: var(--text-muted);">${{hints["2"]}}</div>
          </div>
          <div class="hint-step hint-3">
            <span class="hint-lvl-badge" style="color: #059669;">Petunjuk 3 (Solusi Terarah):</span>
            <div style="font-size: 12.5px; color: var(--text-muted);">${{hints["3"]}}</div>
          </div>
        </div>
      `;
    }}

    function toggleAccordion(headerEl) {{
      const body = headerEl.nextElementSibling;
      body.classList.toggle("open");
    }}

    // PAGINATION RENDER
    function renderPagination(total) {{
      const totalPages = Math.ceil(total / pageSize);
      const pageInfo = document.getElementById("page-info-text");
      pageInfo.innerText = `Halaman ${{currentPage}} dari ${{totalPages}} (${{total}} butir)`;

      const btnContainer = document.getElementById("page-buttons-container");
      btnContainer.innerHTML = "";

      if (totalPages <= 1) return;

      const prevBtn = document.createElement("button");
      prevBtn.className = "page-btn";
      prevBtn.innerText = "‹";
      prevBtn.disabled = currentPage === 1;
      prevBtn.onclick = () => {{ if (currentPage > 1) {{ currentPage--; renderCatalog(); window.scrollTo({{ top: 350, behavior: 'smooth' }}); }} }};
      btnContainer.appendChild(prevBtn);

      // Max 7 page numbers shown
      let startP = Math.max(1, currentPage - 3);
      let endP = Math.min(totalPages, startP + 6);
      if (endP - startP < 6) startP = Math.max(1, endP - 6);

      for (let p = startP; p <= endP; p++) {{
        const btn = document.createElement("button");
        btn.className = `page-btn ${{p === currentPage ? 'active' : ''}}`;
        btn.innerText = p;
        btn.onclick = () => {{ currentPage = p; renderCatalog(); window.scrollTo({{ top: 350, behavior: 'smooth' }}); }};
        btnContainer.appendChild(btn);
      }}

      const nextBtn = document.createElement("button");
      nextBtn.className = "page-btn";
      nextBtn.innerText = "›";
      nextBtn.disabled = currentPage === totalPages;
      nextBtn.onclick = () => {{ if (currentPage < totalPages) {{ currentPage++; renderCatalog(); window.scrollTo({{ top: 350, behavior: 'smooth' }}); }} }};
      btnContainer.appendChild(nextBtn);
    }}

    // COPY ITEM TEXT
    function copyItemText(itemId) {{
      const item = allItems.find(i => i.id === itemId);
      if (!item) return;

      let str = `[${{item.id}}] (${{item.difficulty === 1 ? 'Mudah' : item.difficulty === 2 ? 'Sedang' : 'Sulit'}})\n`;
      str += `Soal: ${{item.prompt}}\n\n`;
      str += `Pilihan Jawaban:\n`;
      Object.entries(item.options || {{}}).forEach(([k, v]) => {{
        str += `  ${{k}}. ${{v}}${{k === item.correct_answer ? ' (KUNCI)' : ''}}\n`;
      }});
      if (item.reasoning_options) {{
        str += `\nAlasan Penalaran (TOLT):\n`;
        Object.entries(item.reasoning_options).forEach(([rk, rv]) => {{
          str += `  ${{rk}}. ${{rv}}${{rk === item.correct_reasoning ? ' (KUNCI ALASAN)' : ''}}\n`;
        }});
      }}
      str += `\nPenjelasan: ${{item.explanation}}\n`;

      navigator.clipboard.writeText(str).then(() => {{
        alert("Teks butir soal " + itemId + " berhasil disalin ke clipboard!");
      }});
    }}

    // QUIZ SIMULATION
    function loadRandomQuizItem() {{
      const idx = Math.floor(Math.random() * allItems.length);
      setupQuizItem(allItems[idx]);
    }}

    function tryInQuiz(itemId) {{
      const item = allItems.find(i => i.id === itemId);
      if (!item) return;
      switchTab("quiz");
      setupQuizItem(item);
    }}

    function setupQuizItem(item) {{
      currentQuizItem = item;
      quizSelectedOption = null;
      quizSelectedReasoning = null;
      currentHintLevel = 0;

      // Badges
      const badgeContainer = document.getElementById("quiz-badges");
      badgeContainer.innerHTML = `
        <span class="item-id">${{item.id}}</span>
        <span class="badge badge-diff-${{item.difficulty}}">${{item.difficulty === 1 ? 'Mudah' : item.difficulty === 2 ? 'Sedang' : 'Sulit'}}</span>
        <span class="badge badge-kc">${{item.kc}}</span>
        <span class="badge badge-tolt">${{item.tolt_dim}}</span>
        <span class="badge badge-bank">${{item.bankLabel}}</span>
      `;

      // Prompt
      document.getElementById("quiz-prompt").innerText = item.prompt;

      // Options
      const optContainer = document.getElementById("quiz-options-container");
      optContainer.innerHTML = "";

      Object.entries(item.options || {{}}).forEach(([k, text]) => {{
        const div = document.createElement("div");
        div.className = "quiz-option";
        div.id = "quiz-opt-" + k;
        div.onclick = () => selectQuizOption(k);
        div.innerHTML = `
          <div class="option-key">${{k}}</div>
          <div style="flex: 1;">${{text}}</div>
        `;
        optContainer.appendChild(div);
      }});

      // Tier 2 if TOLT
      const tier2Box = document.getElementById("quiz-tier2-container");
      if (item.reasoning_options) {{
        tier2Box.style.display = "block";
        const t2Opt = document.getElementById("quiz-tier2-options");
        t2Opt.innerHTML = "";
        Object.entries(item.reasoning_options).forEach(([rk, rtext]) => {{
          const rdiv = document.createElement("div");
          rdiv.className = "quiz-option";
          rdiv.id = "quiz-ropt-" + rk;
          rdiv.onclick = () => selectQuizReasoning(rk);
          rdiv.innerHTML = `
            <div class="option-key">${{rk}}</div>
            <div style="flex: 1;">${{rtext}}</div>
          `;
          t2Opt.appendChild(rdiv);
        }});
      }} else {{
        tier2Box.style.display = "none";
      }}

      // Reset feedback and hints
      document.getElementById("quiz-feedback-box").className = "quiz-feedback";
      document.getElementById("quiz-feedback-box").style.display = "none";
      document.getElementById("quiz-hints-revealed").innerHTML = "";
      document.getElementById("btn-open-hint").style.display = "none";
      document.getElementById("btn-submit-quiz").disabled = false;
      document.getElementById("hint-lvl-text").innerText = "Level 1";
    }}

    function selectQuizOption(k) {{
      quizSelectedOption = k;
      document.querySelectorAll("#quiz-options-container .quiz-option").forEach(el => el.classList.remove("selected"));
      const selectedEl = document.getElementById("quiz-opt-" + k);
      if (selectedEl) selectedEl.classList.add("selected");
    }}

    function selectQuizReasoning(rk) {{
      quizSelectedReasoning = rk;
      document.querySelectorAll("#quiz-tier2-options .quiz-option").forEach(el => el.classList.remove("selected"));
      const selectedEl = document.getElementById("quiz-ropt-" + rk);
      if (selectedEl) selectedEl.classList.add("selected");
    }}

    function checkQuizAnswer() {{
      if (!quizSelectedOption) {{
        alert("Silakan pilih salah satu opsi jawaban terlebih dahulu!");
        return;
      }}
      if (currentQuizItem.reasoning_options && !quizSelectedReasoning) {{
        alert("Silakan pilih alasan penalaran (Tier 2) juga!");
        return;
      }}

      const isOptCorrect = (quizSelectedOption === currentQuizItem.correct_answer);
      let isReasonCorrect = true;
      if (currentQuizItem.reasoning_options) {{
        isReasonCorrect = (quizSelectedReasoning === currentQuizItem.correct_reasoning);
      }}

      const fbBox = document.getElementById("quiz-feedback-box");
      const fbTitle = document.getElementById("quiz-feedback-title");
      const fbExp = document.getElementById("quiz-feedback-explanation");

      fbBox.style.display = "block";

      if (isOptCorrect && isReasonCorrect) {{
        fbBox.className = "quiz-feedback correct";
        fbTitle.innerText = "🎉 Jawaban Anda Benar!";
        fbExp.innerHTML = `
          <div>Kunci Jawaban: <strong>${{currentQuizItem.correct_answer}}</strong></div>
          <div style="margin-top: 6px;">${{currentQuizItem.explanation}}</div>
        `;
        document.getElementById("btn-open-hint").style.display = "none";
      }} else {{
        fbBox.className = "quiz-feedback incorrect";
        fbTitle.innerText = "❌ Jawaban Belum Tepat";
        fbExp.innerHTML = `
          <div>Pilihan Anda: <strong>${{quizSelectedOption}}</strong>. Coba periksa kembali analisis teknis Anda.</div>
          <div style="margin-top: 6px;">Gunakan tombol Scaffolding Hint di bawah untuk mendapatkan panduan bertahap!</div>
        `;
        document.getElementById("btn-open-hint").style.display = "inline-flex";
      }}
    }}

    function revealNextHint() {{
      if (!currentQuizItem) return;
      const hints = DB.hints[currentQuizItem.kc];
      if (!hints) {{
        alert("Tidak ada petunjuk statis khusus untuk kategori ini.");
        return;
      }}

      currentHintLevel++;
      if (currentHintLevel <= 3 && hints[currentHintLevel.toString()]) {{
        const container = document.getElementById("quiz-hints-revealed");
        const hDiv = document.createElement("div");
        hDiv.className = `hint-step hint-${{currentHintLevel}}`;
        hDiv.style.background = "white";
        hDiv.style.padding = "10px";
        hDiv.style.borderRadius = "6px";
        hDiv.style.border = "1px solid var(--border)";
        hDiv.innerHTML = `
          <span class="hint-lvl-badge" style="color: ${{currentHintLevel===1?'#2563eb':currentHintLevel===2?'#d97706':'#059669'}}">
            💡 Scaffolding Hint Level ${{currentHintLevel}}:
          </span>
          <div style="font-size: 13px; color: var(--text);">${{hints[currentHintLevel.toString()]}}</div>
        `;
        container.appendChild(hDiv);

        if (currentHintLevel < 3) {{
          document.getElementById("hint-lvl-text").innerText = `Level ${{currentHintLevel + 1}}`;
        }} else {{
          document.getElementById("btn-open-hint").style.display = "none";
        }}
      }}
    }}

    // BLUEPRINT TABLE
    function renderBlueprintTable() {{
      const tbody = document.getElementById("blueprint-tbody");
      tbody.innerHTML = "";

      allItems.forEach((item, idx) => {{
        const tr = document.createElement("tr");
        tr.innerHTML = `
          <td style="color: var(--text-muted); font-family: var(--font-mono);">${{idx + 1}}</td>
          <td style="font-family: var(--font-mono); font-weight: 700; font-size: 12px;">${{item.id}}</td>
          <td><span class="badge badge-bank">${{item.bankLabel}}</span></td>
          <td style="font-size: 12.5px;">${{item.kc}}</td>
          <td style="font-size: 12px; color: var(--text-muted);">${{item.tolt_dim}}</td>
          <td style="text-align: center;">
            <span class="badge badge-diff-${{item.difficulty}}">${{item.difficulty === 1 ? 'Mudah' : item.difficulty === 2 ? 'Sedang' : 'Sulit'}}</span>
          </td>
          <td style="text-align: center; font-family: var(--font-mono); font-weight: 800;">
            <span class="badge badge-ans">${{item.correct_answer}}</span>
          </td>
          <td style="text-align: center;">${{item.is_calib ? '⭐ Ya' : '-'}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    // EXPORT FUNCTIONS
    function exportDataJson() {{
      const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(DB, null, 2));
      const downloadAnchor = document.createElement("a");
      downloadAnchor.setAttribute("href", dataStr);
      downloadAnchor.setAttribute("download", "logitrace_item_bank_206.json");
      document.body.appendChild(downloadAnchor);
      downloadAnchor.click();
      downloadAnchor.remove();
    }}

    function exportTableCsv() {{
      let csv = `No,ID_Butir,Tipe_Bank,Knowledge_Component,Dimensi_TOLT,Tingkat_Kesulitan,Kunci_Jawaban,Kalibrasi\n`;
      allItems.forEach((item, idx) => {{
        const diffText = item.difficulty === 1 ? "Mudah" : (item.difficulty === 2 ? "Sedang" : "Sulit");
        csv += `"${{idx+1}}","${{item.id}}","${{item.bankLabel}}","${{item.kc}}","${{item.tolt_dim}}","${{diffText}}","${{item.correct_answer}}","${{item.is_calib ? 'Ya' : 'Tidak'}}"\n`;
      }});

      const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.setAttribute("download", "kisi_kisi_skripsi_logitrace.csv");
      document.body.appendChild(link);
      link.click();
      link.remove();
    }}
  </script>

</body>
</html>
'''

    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Successfully generated: {OUTPUT_HTML} ({len(html_content):,} bytes)")

if __name__ == "__main__":
    build()
