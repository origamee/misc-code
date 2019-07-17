#install qpdf on Phantom machine
#Relace fields with <> with actual input/output-filename values
import PyPDF2, os

command = 'qpdf --password=infected --decrypt <input_file.pdf> <output_file.pdf>’
os.system(command)

#Now if you need to extract text or something
pdfFileObj = open(‘<output_file.pdf>’, 'rb')
filename = ‘<output_file.pdf>’
fileObj = open(‘<output_file.pdf>’, 'rb')
readerObj = PyPDF2.PdfFileReader(fileObj)
pageObj = reader.getPage(0)
pageObj.extractText()
