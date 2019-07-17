# 4/A<</Type/Action/S/URI/URI(http://en.wikipedia.org/wiki/Multimedia)
# 4/A<</Type/Action/S/URI/URI(http://en.wikipedia.org/wiki/Operating_system)

import PyPDF2

f = open('Demo_PDF.pdf','rb')

pdf = PyPDF2.PdfFileReader(f)
pgs = pdf.getNumPages()
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
