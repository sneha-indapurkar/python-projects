import sys
import os
import comtypes.client
wdFormatPDF = 17
filename = "filename"
in_file = "C:\\Users\\h316585\\Documents\\SOC\\ATP KBA\\" + filename + ".docx"
out_file = "C:\\Users\\h316585\\Documents\\SOC\\ATP KBA\\" + filename + ".pdf"
word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(in_file)
doc.SaveAs(out_file, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()
