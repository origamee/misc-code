import docxpy
import os

doc = docxpy.DOCReader('Demo_WORD.docx')
doc.process()
linkextracts = doc.data['links']

#doc.data.keys() --> Since doc.data is of type dict
#['header', 'document', 'links', 'footer']
for i in doc.links.values():
    print(i)
'''
Alternate-method
#iterating a 2D list. In this case, it's a list of tuples
links = []
for i,j in linkextracts:
    links.append(j)

print(len(links))

#printing out the list called links
for k in links:
    print(k)
'''
