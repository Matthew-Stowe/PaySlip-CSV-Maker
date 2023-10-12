import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

fd = open("Pay4.pdf", "rb")
#doc = PDFDocument(fd)      #PDFDoc Instace
viewer = SimplePDFViewer(fd)        #SPDFViewer Instance (meta data can be viewed through both instaces)



#--PDFDocument Instance--

#Shows PDF's version
#print(doc.header.version)

#Shows all PFD metadata
#print(doc.metadata)

#Shows Doc Type
#print(doc.root.type)

#Page Generator, yeild page isntances
#page_one = next(doc.pages())

#array of page instaces - prints amount of pages in document
#all_pages = [p for p in doc.pages()]
#print(len(all_pages))

#If you need to get to a specific page, you need to iterate through all prior pages



#--PDF Viewer Instance--
#SPDFViewer provides a SimpleCanvas object for every page
#SimpleCanvas objects contion content like: images, forms, and text

#viewer.navigate(1)  #finds page 1
#viewer.render()     #renders page 1's content

#you can also loop though all page with a for loop
#this loop walks through all documents pages and extract data
for canvas in viewer:
    page_images = canvas.images
    print("--Images--")
    print(page_images)
    print("\n")

    age_forms = canvas.forms
    print("--forms--")
    print(age_forms)
    print("\n")

    page_text = canvas.text_content
    print("--text--")
    print(page_text)
    print("\n")

    page_inline_images = canvas.inline_images
    print("--inline_images--")
    print(page_inline_images)
    print("\n")

    page_strings = canvas.strings
    print("--strings--")                #best option for upcoming projects
    print(page_strings)
    print("\n")



fd.close()
