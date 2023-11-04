from pypdf import PdfWriter

merger = PdfWriter()
conta_de_luz = open("conta_de_luz.pdf", "rb")
cnh = open("cnh.pdf", "rb")

merger.append(fileobj=conta_de_luz, pages=(0, 1))
merger.append(fileobj=cnh)

merger.encrypt("pythonbrasil2023", algorithm="AES-256-R5")

merger.write("imprimir.pdf")
merger.close()
