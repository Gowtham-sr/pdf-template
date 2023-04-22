from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # RGB colours. You can assign it from 0-254.
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # Cell's width, height(recommended font size), align left side, ln = break line
    pdf.line(10, 21, 200, 21)
    # x1, y1, x2, y2 co-ordinates in mm, coz you assigned it in mm.

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
    # range represents a list. Suppose range(3) represents [0, 1, 2] means i -> 0, 1, 2.
    # Why -1 means coz already 1 page is created in parent for loop.

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
