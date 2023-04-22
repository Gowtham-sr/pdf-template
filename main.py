from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # RGB colours. You can assign it from 0-254.
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # width, height(font size), align left side, ln = break line
    pdf.line(10, 21, 200, 21)
    # x1, y1, x2, y2 co-ordinates in mm, coz you assigned it in mm.

pdf.output("output.pdf")
