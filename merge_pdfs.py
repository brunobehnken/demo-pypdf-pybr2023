from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["conta_de_luz.pdf", "cnh.pdf"]:
    merger.append(pdf)

merger.write("imprimir.pdf")
merger.close()
