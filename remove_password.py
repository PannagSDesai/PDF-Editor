import pymupdf
import os
import getpass

def remove_pdf_password(input_path, output_path, password):
    doc = pymupdf.open(input_path)
    
    if doc.needs_pass:
        rc = doc.authenticate(password)
        if rc <= 0:
            print("Authentication failed. Incorrect password.")
            return False
            
    doc.save(output_path, encryption=pymupdf.PDF_ENCRYPT_NONE)
    doc.close()
    print(f"Password removed successfully. Saved to: {output_path}")
    return True


if os.path.exists("Documents"):
    password = getpass.getpass("Enter the password for the PDF files: ")
    for i in os.listdir("Documents"):
        if i.endswith(".pdf"):
            remove_pdf_password("Documents/" + i, "Documents/" + i + "_unprotected.pdf", password)
else:
    print("No files to process, Please make sure to add your Protected files under the documents")