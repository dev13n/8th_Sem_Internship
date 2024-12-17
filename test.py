# import PdfReader class from pypdf
from pypdf import PdfReader # type: ignore

# creating an object to read a pdf
reader = PdfReader("read_from.pdf")

# printing the length of pages
print("The number of pages are: ",len(reader.pages),"\n\n")

# creating a page object
page = reader.pages[0]
# print(page) 
# # Prints the data, the internal structure of the PDF page in the pypdf library, which represents the raw data of the PDF's internal components (e.g., fonts, resources, media box dimensions). This is not the textual content of the page, but rather the metadata of the page itself.

print (page.extract_text())