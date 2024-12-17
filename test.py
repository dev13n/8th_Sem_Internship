import fitz  # type: ignore # PyMuPDF

# Open the PDF
doc = fitz.open("read_from.pdf")

# Iterate through the pages and extract text
for page_num in range(doc.page_count): # loop to iterate through all the pages of the PDF.
    page = doc.load_page(page_num) # loads a specific page from the PDF document
    text = page.get_text("text")  # Extract text from the page
    print(text)
