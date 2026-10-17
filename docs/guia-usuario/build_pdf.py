#!/usr/bin/env python3
"""Genera Guia-Socio-Creativo.pdf a partir de guia-usuario.md.

Uso (desde esta carpeta):
    python3 build_pdf.py

Requiere: python-markdown y wkhtmltopdf. La guía es la fuente única: se edita
guia-usuario.md, se corre este script y se obtiene el PDF actualizado.
"""
import os
import re
import subprocess
import sys

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "guia-usuario.md")
HTML = os.path.join(HERE, "_guia.html")
PDF = os.path.join(HERE, "Guia-Socio-Creativo.pdf")

SALTO_ANTES = ["Ejemplo real: un carrusel paso a paso", "Qué hay de nuevo"]

CSS = """
@page { size: A4; }
body { font-family: 'Liberation Sans', 'DejaVu Sans', Arial, sans-serif;
       font-size: 11pt; line-height: 1.5; color: #1d2433; }
h1 { font-size: 27pt; color: #2b3a67; margin: 0 0 4pt 0; line-height: 1.15; }
h1 + p { color: #6b7488; font-size: 10pt; margin-top: 0; }
h1 + p + p { font-size: 12pt; border-left: 4px solid #2b3a67; padding-left: 10pt;
             margin: 14pt 0 6pt 0; color: #2b3a67; }
h2 { font-size: 16pt; color: #2b3a67; border-bottom: 2px solid #d9deea;
     padding-bottom: 3pt; margin: 22pt 0 8pt 0; page-break-after: avoid; }
p, li { margin: 5pt 0; }
ul, ol { margin: 5pt 0 5pt 0; padding-left: 20pt; }
table { border-collapse: collapse; width: 100%; margin: 9pt 0; font-size: 9.6pt;
        page-break-inside: auto; }
tr { page-break-inside: avoid; }
th { background: #2b3a67; color: #ffffff; text-align: left; padding: 5pt 6pt;
     border: 1px solid #2b3a67; }
td { padding: 5pt 6pt; border: 1px solid #d9deea; vertical-align: top; }
tr:nth-child(even) td { background: #f3f5fa; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 9.4pt;
       background: #eef1f8; padding: 0 3pt; }
pre { background: #f3f5fa; border: 1px solid #d9deea; border-left: 4px solid #2b3a67;
      padding: 7pt 9pt; white-space: pre-wrap; word-wrap: break-word;
      page-break-inside: avoid; margin: 8pt 0; }
pre code { background: transparent; padding: 0; font-size: 9.6pt; }
img { display: block; width: 330pt; margin: 8pt auto; border: 1px solid #d9deea; }
"""


def numerar(ruta):
    """Agrega 'Guía de uso: Socio Creativo' y 'n / N' al pie de cada página."""
    import io
    from pypdf import PdfReader, PdfWriter
    from reportlab.pdfgen import canvas
    lector = PdfReader(ruta)
    total = len(lector.pages)
    escritor = PdfWriter()
    for i, pagina in enumerate(lector.pages, start=1):
        ancho = float(pagina.mediabox.width)
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=(ancho, float(pagina.mediabox.height)))
        c.setFont("Helvetica", 8)
        c.setFillGray(0.45)
        c.drawString(51, 30, "Guía de uso: Socio Creativo")
        c.drawRightString(ancho - 51, 30, f"{i} / {total}")
        c.save()
        buf.seek(0)
        pagina.merge_page(PdfReader(buf).pages[0])
        escritor.add_page(pagina)
    with open(ruta, "wb") as f:
        escritor.write(f)


def main():
    with open(SRC, encoding="utf-8") as f:
        md_text = f.read()
    body = markdown.markdown(md_text, extensions=["tables", "fenced_code", "sane_lists"])
    for titulo in SALTO_ANTES:
        body = body.replace(f"<h2>{titulo}</h2>",
                            f'<h2 style="page-break-before: always">{titulo}</h2>')
    html = (
        '<!doctype html><html lang="es"><head><meta charset="utf-8">'
        f"<title>Guía de uso: Socio Creativo</title><style>{CSS}</style></head>"
        f"<body>{body}</body></html>"
    )
    with open(HTML, "w", encoding="utf-8") as f:
        f.write(html)
    cmd = [
        "wkhtmltopdf", "--quiet", "--enable-local-file-access",
        "--page-size", "A4",
        "--margin-top", "18mm", "--margin-bottom", "18mm",
        "--margin-left", "18mm", "--margin-right", "18mm",
        HTML, PDF,
    ]
    subprocess.run(cmd, check=True)
    os.remove(HTML)
    numerar(PDF)
    print("PDF generado:", PDF)


if __name__ == "__main__":
    sys.exit(main())
