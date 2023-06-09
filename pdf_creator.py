import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("files/*.txt")

for filepath in filepaths:
    df = pd.read_csv(filepath)
    pdf = FPDF(orientation='P', unit="mm", format="A4")
    pdf.add_page()
    filename = Path(filepath).stem
    name = filename.title()
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{name}")
    pdf.output(f"PDFs/{filename}.pdf")