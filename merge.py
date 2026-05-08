import fitz  # PyMuPDF
import os


output_file_name = input("Enter the output file name: ")
files = []

def merge_pdfs(input_list, output_path):
    # 1. Create a new empty PDF
    combined_pdf = fitz.open()

    for file_path in input_list:
        # 2. Open each source PDF
        with fitz.open(file_path) as source_pdf:
            # 3. Append the source PDF to the end of the combined document
            combined_pdf.insert_pdf(source_pdf)

    # 4. Save the merged result
    combined_pdf.save(output_path)
    combined_pdf.close()

#Read from ./Documents
for i in os.listdir("Documents"):
    if i.endswith(".pdf"):
        files.append("Documents/" + i)
#sort files by last 1 or 2 digits
def get_last_digits(filename):
    # Extract the number part after the last hyphen
    parts = filename.split('-')
    if len(parts) > 1:
        # Get the last part, remove .pdf, convert to int
        try:
            num_part = parts[-1].replace('.pdf', '')
            return int(num_part)
        except ValueError:
            return float('inf') # Put files with non-numeric endings at the end
    return float('inf')

# Sort using the helper function
#files.sort(key=get_last_digits)
files.sort()
print(files)

merge_pdfs(files, output_file_name + ".pdf")