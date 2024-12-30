import pdfplumber
import json
import os

def read_pdf(file_path):
    # Initialize a variable to hold the text
    pdf_text = ""

    # Open the PDF file using pdfplumber
    with pdfplumber.open(file_path) as pdf:
        # Loop through each page in the PDF
        for page in pdf.pages:
            # Extract text from the page and append it to the pdf_text variable
            pdf_text += page.extract_text() + "\n"  # Adding a newline for separation between pages

    return pdf_text

# Example usage
if __name__ == "__main__":
    # Use a raw string or forward slashes to avoid issues with backslashes
    pdf_file_path = r"C:\Users\Devpn\Desktop\Dev\Linde\Dataset\yumuna_pump_new_2023-12-14-13-45-42_c19b5b723f06645aae07e9b2b5f3e709.pdf"  # Corrected path
    
    # Check if the file exists
    if not os.path.exists(pdf_file_path):
        print("File does not exist:", pdf_file_path)
    else:
        extracted_text = read_pdf(pdf_file_path)
        
        # Print the extracted text or do something with it
        print(extracted_text)

        # Save the extracted text to a text file
        with open('output.txt', 'w', encoding='utf-8') as output_file:
            output_file.write(extracted_text)

        # Save the extracted text to a JSON file
        with open('output.json', 'w', encoding='utf-8') as json_file:
            json.dump({"extracted_text": extracted_text}, json_file)