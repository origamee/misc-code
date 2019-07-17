#Remove links from an uncompressed PDF file, and store
#the output as a file named output.pdf
import PyPDF2, os, re

def remove_pdf_links(input_file, output_file):
    fileObj = open('Demo_PDF.pdf', 'rb')
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

if __name__ == '__main__':
    input_file = 'Demo_PDF.pdf'
    output_file = 'output.pdf'
    #remove links and save pdf
    remove_pdf_links(input_file, output_file)
