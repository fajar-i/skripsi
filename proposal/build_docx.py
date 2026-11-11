import re
import os
import docx
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def create_proposal_docx(md_path, docx_path):
    doc = docx.Document()

    # 1. Page Setup according to UPI Standard (Pedoman Karya Ilmiah UPI)
    # A4 Paper (21.0 x 29.7 cm)
    # Margins: Top 3 cm, Left 4 cm, Bottom 3 cm, Right 3 cm
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(3.0)
    section.bottom_margin = Cm(3.0)
    section.left_margin = Cm(4.0)
    section.right_margin = Cm(3.0)

    # Set base Normal style to Times New Roman 12pt
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    normal_style.paragraph_format.line_spacing = 1.5
    normal_style.paragraph_format.space_after = Pt(4)

    # Setup Footer with Page Number
    footer = section.footer
    footer_p = footer.paragraphs[0]
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    footer_p.paragraph_format.line_spacing = 1.0
    footer_p.paragraph_format.space_after = Pt(0)
    footer_run = footer_p.add_run()
    footer_run.font.name = 'Times New Roman'
    footer_run.font.size = Pt(10)
    footer_run.font.color.rgb = RGBColor(100, 100, 100)

    # Dynamic Page Number Field in Word
    fld1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instr = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
    fld2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    fld3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    footer_run._r.append(fld1)
    footer_run._r.append(instr)
    footer_run._r.append(fld2)
    footer_run._r.append(fld3)

    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    lines = md_text.split('\n')
    total_lines = len(lines)

    # Helper function to parse inline markdown (bold, italic, code, math)
    def add_runs(paragraph, text, base_font_size=12, base_italic=False, base_bold=False, base_color=RGBColor(0, 0, 0)):
        pattern = re.compile(r'(\*\*\*.*?\*\*\*|\*\*.*?\*\*|\*.*?\*|`.*?`|\$.*?\$|\[.*?\]\(.*?\))')
        pos = 0
        for match in pattern.finditer(text):
            start, end = match.span()
            if start > pos:
                plain = text[pos:start]
                r = paragraph.add_run(plain)
                r.font.name = 'Times New Roman'
                r.font.size = Pt(base_font_size)
                r.bold = base_bold
                r.italic = base_italic
                r.font.color.rgb = base_color
            token = match.group(0)
            if token.startswith('***') and token.endswith('***'):
                r = paragraph.add_run(token[3:-3])
                r.font.name = 'Times New Roman'
                r.font.size = Pt(base_font_size)
                r.bold = True
                r.italic = True
                r.font.color.rgb = base_color
            elif token.startswith('**') and token.endswith('**'):
                r = paragraph.add_run(token[2:-2])
                r.font.name = 'Times New Roman'
                r.font.size = Pt(base_font_size)
                r.bold = True
                r.italic = base_italic
                r.font.color.rgb = base_color
            elif token.startswith('*') and token.endswith('*'):
                r = paragraph.add_run(token[1:-1])
                r.font.name = 'Times New Roman'
                r.font.size = Pt(base_font_size)
                r.bold = base_bold
                r.italic = True
                r.font.color.rgb = base_color
            elif token.startswith('`') and token.endswith('`'):
                r = paragraph.add_run(token[1:-1])
                r.font.name = 'Consolas'
                r.font.size = Pt(base_font_size - 1.5)
                r.font.color.rgb = RGBColor(40, 40, 40)
            elif token.startswith('$') and token.endswith('$'):
                math_content = token[1:-1]
                math_content = math_content.replace('\\alpha_d', 'α_d')
                math_content = math_content.replace('\\gamma_d', 'γ_d')
                math_content = math_content.replace('\\beta', 'β')
                math_content = math_content.replace('\\le', '≤')
                math_content = math_content.replace('\\ge', '≥')
                math_content = math_content.replace('\\hat{p}', 'p̂')
                math_content = math_content.replace('\\approx', '≈')
                math_content = math_content.replace('\\times', '×')
                math_content = math_content.replace('\\neq', '≠')
                math_content = math_content.replace('\\tau', 'τ')
                math_content = math_content.replace('\\Delta', 'Δ')
                math_content = math_content.replace('{', '').replace('}', '')
                r = paragraph.add_run(math_content)
                r.font.name = 'Cambria Math'
                r.font.size = Pt(base_font_size)
                r.italic = True
                r.font.color.rgb = base_color
            elif token.startswith('[') and '](' in token:
                link_text = token[1:token.index('](')]
                r = paragraph.add_run(link_text)
                r.font.name = 'Times New Roman'
                r.font.size = Pt(base_font_size)
                r.font.color.rgb = RGBColor(0, 51, 153)
                r.underline = True
            pos = end
        if pos < len(text):
            plain = text[pos:]
            r = paragraph.add_run(plain)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(base_font_size)
            r.bold = base_bold
            r.italic = base_italic
            r.font.color.rgb = base_color

    # Table formatting function
    def format_table(table, col_widths, headers, data_rows, is_matrix=False):
        tblPr = table._tbl.tblPr
        borders = parse_xml(f'''
            <w:tblBorders {nsdecls("w")}>
                <w:top w:val="single" w:sz="8" w:space="0" w:color="333333"/>
                <w:bottom w:val="single" w:sz="8" w:space="0" w:color="333333"/>
                <w:left w:val="none"/>
                <w:right w:val="none"/>
                <w:insideH w:val="single" w:sz="4" w:space="0" w:color="D0D0D0"/>
                <w:insideV w:val="none"/>
            </w:tblBorders>
        ''')
        tblPr.append(borders)

        # Header Row
        hdr_row = table.rows[0]
        trPr = hdr_row._tr.get_or_add_trPr()
        trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))
        trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

        hdr_font_size = 8.5 if is_matrix else 9.5
        cell_font_size = 8.0 if is_matrix else 9.0

        for ci, heading in enumerate(headers):
            cell = hdr_row.cells[ci]
            cell.width = col_widths[ci]
            tcPr = cell._tc.get_or_add_tcPr()
            tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="F0F4F8"/>'))
            tcPr.append(parse_xml(f'''
                <w:tcMar {nsdecls("w")}>
                    <w:top w:w="120" w:type="dxa"/>
                    <w:bottom w:w="120" w:type="dxa"/>
                    <w:left w:w="120" w:type="dxa"/>
                    <w:right w:w="120" w:type="dxa"/>
                </w:tcMar>
            '''))
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing = 1.1
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.space_before = Pt(2)
            add_runs(p, heading.strip(), base_font_size=hdr_font_size, base_bold=True)

        # Data Rows
        for ri, row_data in enumerate(data_rows):
            row = table.rows[ri + 1]
            trPr = row._tr.get_or_add_trPr()
            trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

            bg_color = "FAFBFC" if ri % 2 == 1 else "FFFFFF"

            for ci, cell_text in enumerate(row_data):
                if ci >= len(row.cells):
                    break
                cell = row.cells[ci]
                cell.width = col_widths[ci]
                tcPr = cell._tc.get_or_add_tcPr()
                if bg_color != "FFFFFF":
                    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_color}"/>'))
                tcPr.append(parse_xml(f'''
                    <w:tcMar {nsdecls("w")}>
                        <w:top w:w="100" w:type="dxa"/>
                        <w:bottom w:w="100" w:type="dxa"/>
                        <w:left w:w="120" w:type="dxa"/>
                        <w:right w:w="120" w:type="dxa"/>
                    </w:tcMar>
                '''))
                p = cell.paragraphs[0]
                cleaned = cell_text.strip()
                if len(cleaned) <= 6 and (cleaned.isdigit() or re.match(r'^[0-9.,%+-]+$', cleaned) or cleaned in ['STS', 'TS', 'N', 'S', 'SS', '1', '2', '3', '4', '5']):
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                p.paragraph_format.line_spacing = 1.1
                p.paragraph_format.space_after = Pt(2)
                p.paragraph_format.space_before = Pt(2)
                add_runs(p, cleaned, base_font_size=cell_font_size)

    # Section State Tracker
    current_section = 'COVER'
    in_code_block = False
    code_block_lines = []

    i = 0
    while i < total_lines:
        line = lines[i]
        stripped = line.strip()

        # Check section transition
        if stripped.startswith('# '):
            h_text = stripped[2:].strip().upper()
            if 'KATA PENGANTAR' in h_text:
                current_section = 'KATA_PENGANTAR'
            elif 'DAFTAR ISI' in h_text:
                current_section = 'DAFTAR_ISI'
            elif 'BAB I' in h_text:
                current_section = 'BAB_I'
            elif 'BAB II' in h_text:
                current_section = 'BAB_II'
            elif 'BAB III' in h_text:
                current_section = 'BAB_III'
            elif 'DAFTAR PUSTAKA' in h_text:
                current_section = 'DAFTAR_PUSTAKA'
            elif 'LAMPIRAN' in h_text:
                current_section = 'LAMPIRAN'

        # --- 1. COVER PAGE LOGIC ---
        if current_section == 'COVER':
            if stripped == '# PROPOSAL SKRIPSI':
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.line_spacing = 1.3
                p.paragraph_format.space_before = Pt(18)
                p.paragraph_format.space_after = Pt(18)
                add_runs(p, 'PROPOSAL SKRIPSI', base_font_size=16, base_bold=True)
                i += 1
                continue
            elif stripped.startswith('## PENGEMBANGAN WEB'):
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.line_spacing = 1.3
                p.paragraph_format.space_before = Pt(12)
                p.paragraph_format.space_after = Pt(24)
                add_runs(p, stripped[3:], base_font_size=14, base_bold=True)
                i += 1
                continue
            elif stripped.startswith('Disusun untuk memenuhi'):
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.line_spacing = 1.2
                p.paragraph_format.space_before = Pt(12)
                p.paragraph_format.space_after = Pt(36)
                add_runs(p, stripped, base_font_size=12)
                i += 1
                continue
            elif stripped.startswith('**Oleh:**') or stripped == 'Oleh:':
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_before = Pt(6)
                p.paragraph_format.space_after = Pt(2)
                add_runs(p, 'Oleh:', base_font_size=12)
                i += 1
                continue
            elif 'Fajari Arkan Fadhlurrahman' in stripped:
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(2)
                add_runs(p, 'Fajari Arkan Fadhlurrahman', base_font_size=12, base_bold=True)
                i += 1
                continue
            elif 'NIM. 2304794' in stripped:
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_before = Pt(2)
                p.paragraph_format.space_after = Pt(48)
                add_runs(p, 'NIM. 2304794', base_font_size=12, base_bold=True)
                i += 1
                continue
            elif stripped in ['---', '***']:
                prev_lines = [lines[k].strip() for k in range(max(0, i-5), i) if lines[k].strip()]
                if prev_lines and '2026' in prev_lines[-1]:
                    doc.add_page_break()
                    current_section = 'FRONTMATTER'
                i += 1
                continue
            elif any(inst in stripped for inst in ['PROGRAM STUDI', 'FAKULTAS', 'UNIVERSITAS', 'BANDUNG', '2026']):
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after = Pt(2)
                clean_inst = stripped.replace('**', '')
                add_runs(p, clean_inst, base_font_size=12, base_bold=True)
                i += 1
                continue

        # --- 2. CODE BLOCKS ---
        if stripped.startswith('```'):
            if not in_code_block:
                in_code_block = True
                code_block_lines = []
                i += 1
                continue
            else:
                in_code_block = False
                code_table = doc.add_table(rows=1, cols=1)
                code_table.alignment = WD_TABLE_ALIGNMENT.CENTER
                code_cell = code_table.rows[0].cells[0]
                code_cell.width = Cm(14.0)
                tcPr = code_cell._tc.get_or_add_tcPr()
                tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="F6F8FA"/>'))
                tcPr.append(parse_xml(f'''
                    <w:tcMar {nsdecls("w")}>
                        <w:top w:w="140" w:type="dxa"/>
                        <w:bottom w:w="140" w:type="dxa"/>
                        <w:left w:w="180" w:type="dxa"/>
                        <w:right w:w="180" w:type="dxa"/>
                    </w:tcMar>
                '''))
                cp = code_cell.paragraphs[0]
                cp.paragraph_format.line_spacing = 1.0
                cp.paragraph_format.space_after = Pt(0)
                cp.paragraph_format.space_before = Pt(0)
                full_code = '\n'.join(code_block_lines)
                c_run = cp.add_run(full_code)
                c_run.font.name = 'Consolas'
                c_run.font.size = Pt(8.5)
                c_run.font.color.rgb = RGBColor(30, 30, 30)

                sp = doc.add_paragraph()
                sp.paragraph_format.space_after = Pt(6)
                sp.paragraph_format.line_spacing = 1.0
                i += 1
                continue

        if in_code_block:
            code_block_lines.append(line)
            i += 1
            continue

        # --- 3. TABLES ---
        if stripped.startswith('|') and stripped.endswith('|'):
            table_lines = []
            while i < total_lines and lines[i].strip().startswith('|') and lines[i].strip().endswith('|'):
                table_lines.append(lines[i].strip())
                i += 1

            if len(table_lines) >= 3:
                raw_headers = [c.strip() for c in table_lines[0].split('|')[1:-1]]
                raw_data = []
                for dl in table_lines[2:]:
                    cols = [c.strip() for c in dl.split('|')[1:-1]]
                    if len(cols) < len(raw_headers):
                        cols += [''] * (len(raw_headers) - len(cols))
                    raw_data.append(cols[:len(raw_headers)])

                num_cols = len(raw_headers)
                num_rows = len(raw_data) + 1

                total_w = 14.0  # Usable portrait width (21.0 - 4.0 - 3.0)
                is_matrix = (num_cols == 6)

                if is_matrix:
                    col_widths = [Cm(2.1), Cm(2.5), Cm(2.2), Cm(2.4), Cm(2.4), Cm(2.4)]
                elif num_cols == 2:
                    col_widths = [Cm(4.0), Cm(10.0)]
                elif num_cols == 3:
                    col_widths = [Cm(2.5), Cm(5.0), Cm(6.5)]
                elif num_cols == 4:
                    col_widths = [Cm(2.5), Cm(3.5), Cm(4.0), Cm(4.0)]
                elif num_cols == 5:
                    col_widths = [Cm(1.0), Cm(3.2), Cm(3.3), Cm(3.0), Cm(3.5)]
                elif num_cols == 7:
                    col_widths = [Cm(0.9), Cm(7.6), Cm(1.1), Cm(1.1), Cm(1.1), Cm(1.1), Cm(1.1)]
                else:
                    sample_lens = [len(h) for h in raw_headers]
                    sum_lens = sum(sample_lens) or 1
                    col_widths = [Cm(max(1.2, round((l / sum_lens) * total_w, 2))) for l in sample_lens]
                    current_sum = sum(w.cm for w in col_widths)
                    col_widths = [Cm(round(w.cm * (total_w / current_sum), 2)) for w in col_widths]

                table = doc.add_table(rows=num_rows, cols=num_cols)
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                format_table(table, col_widths, raw_headers, raw_data, is_matrix=is_matrix)

                sp = doc.add_paragraph()
                sp.paragraph_format.space_after = Pt(6)
                sp.paragraph_format.line_spacing = 1.0
            continue

        # Blank line
        if not stripped:
            i += 1
            continue

        # Horizontal Rule `---`
        if stripped in ['---', '***', '___']:
            doc.add_page_break()
            i += 1
            continue

        # --- 4. MAJOR HEADINGS ---
        # Handle Chapter Headings: `# BAB ...` followed by `# TITLE`
        if line.startswith('# BAB '):
            doc.add_page_break()
            bab_num = line[2:].strip()
            # Check if next non-empty line is `# ...`
            nxt_idx = i + 1
            bab_title = ''
            if nxt_idx < total_lines and lines[nxt_idx].strip().startswith('# '):
                bab_title = lines[nxt_idx].strip()[2:].strip()
                i = nxt_idx  # advance past the second header line

            full_h = f"{bab_num}\n{bab_title}" if bab_title else bab_num
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(18)
            p.paragraph_format.keep_with_next = True
            add_runs(p, full_h, base_font_size=14, base_bold=True)
            i += 1
            continue

        # Handle Other `# ...` Headings (KATA PENGANTAR, DAFTAR ISI, DAFTAR PUSTAKA, LAMPIRAN)
        if line.startswith('# '):
            h_text = line[2:].strip()
            doc.add_page_break()

            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(18)
            p.paragraph_format.keep_with_next = True
            add_runs(p, h_text, base_font_size=14, base_bold=True)
            i += 1
            continue

        # Heading 2: `## ...`
        if line.startswith('## '):
            h_text = line[3:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(12)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            add_runs(p, h_text, base_font_size=12, base_bold=True)
            i += 1
            continue

        # Heading 3: `### ...`
        if line.startswith('### '):
            h_text = line[4:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            add_runs(p, h_text, base_font_size=12, base_bold=True)
            i += 1
            continue

        # Heading 4: `#### ...`
        if line.startswith('#### '):
            h_text = line[5:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            add_runs(p, h_text, base_font_size=12, base_bold=True, base_italic=True)
            i += 1
            continue

        # --- 5. SPECIAL SECTIONS ---
        # DAFTAR ISI items
        if current_section == 'DAFTAR_ISI' and (stripped.startswith('- ') or stripped.startswith('* ')):
            indent_spaces = len(line) - len(line.lstrip())
            content = stripped[2:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(2)

            if indent_spaces == 0:
                p.paragraph_format.left_indent = Cm(0)
                add_runs(p, content, base_font_size=11, base_bold=True)
            elif indent_spaces == 2:
                p.paragraph_format.left_indent = Cm(0.8)
                add_runs(p, content, base_font_size=10.5)
            elif indent_spaces == 4:
                p.paragraph_format.left_indent = Cm(1.6)
                add_runs(p, content, base_font_size=10)
            else:
                p.paragraph_format.left_indent = Cm(2.4)
                add_runs(p, content, base_font_size=9.5)
            i += 1
            continue

        # KATA PENGANTAR Signature Block
        if current_section == 'KATA_PENGANTAR' and (stripped.startswith('Bandung,') or stripped == 'Penulis,' or stripped.startswith('**Fajari') or stripped.startswith('NIM.')):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.left_indent = Cm(10.0)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(2)
            is_bold = stripped.startswith('**') or stripped.startswith('Fajari')
            clean_text = stripped.replace('**', '')
            add_runs(p, clean_text, base_font_size=12, base_bold=is_bold)
            i += 1
            continue

        # DAFTAR PUSTAKA Entries (APA 7th Hanging Indent)
        if current_section == 'DAFTAR_PUSTAKA':
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(6)
            p.paragraph_format.left_indent = Cm(1.0)
            p.paragraph_format.first_line_indent = Cm(-1.0)
            add_runs(p, stripped, base_font_size=11)
            i += 1
            continue

        # Blockquote: `> ...`
        if line.startswith('> '):
            b_text = line[2:].strip()
            b_text = re.sub(r'^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*', '', b_text)
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.left_indent = Cm(1.0)
            p.paragraph_format.right_indent = Cm(1.0)
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(6)
            add_runs(p, b_text, base_font_size=11, base_italic=True)
            i += 1
            continue

        # Table caption check (e.g. `**Tabel 2.6 ...**`)
        if stripped.startswith('**Tabel ') and stripped.endswith('**'):
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(8)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            add_runs(p, stripped[2:-2], base_font_size=11, base_bold=True)
            i += 1
            continue

        # Bullet List: `- ...` or `* ...`
        if stripped.startswith('- ') or stripped.startswith('* '):
            indent_level = len(line) - len(line.lstrip())
            content = stripped[2:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.space_before = Pt(0)
            base_left = 0.75 + (indent_level // 2) * 0.5
            p.paragraph_format.left_indent = Cm(base_left)
            p.paragraph_format.first_line_indent = Cm(-0.4)
            bullet_sym = '▪ ' if indent_level >= 2 else '• '
            r_b = p.add_run(bullet_sym)
            r_b.font.name = 'Times New Roman'
            r_b.font.size = Pt(11)
            add_runs(p, content, base_font_size=11.5)
            i += 1
            continue

        # Numbered List: `1. `, `2. `, `a. `, etc.
        m_num = re.match(r'^(\d+\.|\([a-z0-9]+\)|[a-z]\.)\s+(.*)', stripped)
        if m_num:
            prefix = m_num.group(1)
            content = m_num.group(2)
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_after = Pt(3)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.left_indent = Cm(0.8)
            p.paragraph_format.first_line_indent = Cm(-0.5)
            r_num = p.add_run(prefix + ' ')
            r_num.font.name = 'Times New Roman'
            r_num.font.size = Pt(12)
            r_num.bold = False
            add_runs(p, content, base_font_size=12)
            i += 1
            continue

        # Standard Body Paragraph
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.space_after = Pt(4)
        if len(stripped) > 80 and not stripped.startswith('**'):
            p.paragraph_format.first_line_indent = Cm(1.0)
        add_runs(p, stripped, base_font_size=12)

        i += 1

    doc.save(docx_path)
    print(f"Document successfully created at: {docx_path}")

if __name__ == '__main__':
    md_in = r'c:\kuliah\semester_7\skripsi\proposal\proposal_skripsi_bab_1_2_3.md'
    docx_out = r'c:\kuliah\semester_7\skripsi\proposal\proposal_skripsi_bab_1_2_3.docx'
    create_proposal_docx(md_in, docx_out)
