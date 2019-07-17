import PyPDF2, os, re

def remove_pdf_links(input_file, output_file):
#this function removes all sorts of link from a PDF file, and stores it as output.pdf
    fileObj = open(input_file, 'rb')
    data = fileObj.read()
    fileObj.close()

    linksRegex = re.compile('\\/URI \\((.*)\\)', re.MULTILINE)

    #copy data into a variable
    output = data

    #finding URI's
    links = linksRegex.finditer(data)
    #for each regex match
    for match in links:
        #replace URI's with something of the same length
        output = output.replace(match.group(1), ' ' * len(match.group(1)))
        #store matched URL in a list

    linksRegex = re.compile('\\/URI', re.MULTILINE)

    #finding remaining clickables
    links = linksRegex.finditer(data)

    for match in links:
        #replace /URI tags with spaces
        output = output.replace(match.group(0), ' ' * len(match.group(0)))

    #save the modified pdf file as a binary file
    fileObj = open('output.pdf', 'wb')
    fileObj.write(output)
    fileObj.close()

def extract_links(input_file):
    '''
    This function extacts all the links and prints them as output
    Here's how a link shows up in a PDF file (converted into text)
    4/A<</Type/Action/S/URI/URI(http://en.wikipedia.org/wiki/Multimedia)
    4/A<</Type/Action/S/URI/URI(http://en.wikipedia.org/wiki/Operating_system)
    '''
    f = open(input_file,'rb')

    pdf = PyPDF2.PdfFileReader(f)
    pgs = pdf.getNumPages()
    #Breaking the PDF into annotations, URI's and anks. It's a 3D array so will nest the loop 3-levels
    key = '/Annots'
    uri = '/URI'
    ank = '/A'

    for pg in range(pgs):

        p = pdf.getPage(pg)
        o = p.getObject()

        if o.has_key(key):
            ann = o[key]
            for a in ann:
                u = a.getObject()
                if u[ank].has_key(uri):
                    print u[ank][uri]

if __name__ == '__main__':
    input_file = 'Demo_PDF.pdf'
    output_file = 'output.pdf'
    #extact all links from a PDF and print
    extract_links(input_file)
    #remove links and save the new file as output.pdf
    remove_pdf_links(input_file, output_file)
