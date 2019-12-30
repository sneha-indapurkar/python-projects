# Python code to merge two or more pdf files into one

from pyPdf import PdfFileReader, PdfFileWriter

input_pdf1 = open("D:\\pdf1.pdf", "rb")
input_pdf2 = open("D:\\pdf2.pdf", "rb")
input_pdf3 = open("D:\\pdf3.pdf", "rb")

inputs = [input_pdf1, input_pdf2, input_pdf3]
for reader in map(PdfFileReader, inputs):
    for page_index in range(reader.getNumPages()):
        writer.addPage(reader.getPage(page_index))

output_pdf = open("D:\\combined.pdf", "wb")
writer.write(output_pdf)

for f in inputs:
    f.close()
