"""Génère index.html : python3 build.py template.html AQA.QUAL.03.pdf fond.png index.html"""
import base64
import sys

template, pdf, fond, out = sys.argv[1:5]
b64 = lambda p: base64.b64encode(open(p, "rb").read()).decode()
html = open(template, encoding="utf-8").read()
html = html.replace("__PDF_BASE64__", b64(pdf)).replace("__BG_BASE64__", b64(fond))
open(out, "w", encoding="utf-8").write(html)
