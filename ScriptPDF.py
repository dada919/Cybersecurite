from PyPDF2 import PdfWriter

pdf_writer = PdfWriter()
pdf_writer.add_js("app.alert('Je suis en train de te hacker !!!'); app.launchURL('https://www.youtube.com/watch?v=dQw4w9WgXcQ', true);")  
pdf_writer.add_blank_page(width=210, height=297)
with open("test.pdf", "wb") as f:
    pdf_writer.write(f)
