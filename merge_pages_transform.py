from pypdf import PdfWriter, PdfReader

conta_de_luz_reader = PdfReader("conta_de_luz.pdf")
cnh_reader = PdfReader("cnh.pdf")
writer = PdfWriter()

conta_de_luz_pagina = conta_de_luz_reader.pages[0]
cnh_pagina = cnh_reader.pages[0]
conta_de_luz_pagina.merge_page(cnh_pagina)

writer.add_page(conta_de_luz_pagina)
writer.write("imprimir.pdf")
writer.close()
