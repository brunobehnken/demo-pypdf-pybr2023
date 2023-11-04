from pypdf import PdfWriter, PdfReader

conta_de_luz_reader = PdfReader("conta_de_luz.pdf")
cnh_reader = PdfReader("cnh.pdf")
writer = PdfWriter()

writer.add_page(conta_de_luz_reader.pages[0])
writer.add_page(cnh_reader.pages[0].rotate(180))

writer.write("imprimir.pdf")
writer.close()
