from pypdf import PdfReader

reader = PdfReader("texto.pdf")
page = reader.pages[0]
text = page.extract_text()
print("texto:", text)
