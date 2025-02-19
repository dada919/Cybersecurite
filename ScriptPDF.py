from PyPDF2 import PdfWriter

pdf_writer = PdfWriter()
pdf_writer.add_js("app.alert('J suis en train de te hack !!!');")  
pdf_writer.add_blank_page(width=210, height=297)
with open("malicious.pdf", "wb") as f:
    pdf_writer.write(f)
