import PyPDF2
import re

def extract_working_days_from_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        
        # Extract text from all pages
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()

    # Now that we have the text, let's identify working days
    # This is just an example and can be modified based on the actual format of the PDF.
    
    # Example: Assume the PDF lists working days with weekday names like 'Monday', 'Tuesday', etc.
    working_days = re.findall(r'\b(Monday|Tuesday|Wednesday|Thursday|Friday)\b', text)
    
    return working_days

if __name__ == "__main__":
    # Test the PDF extraction
    pdf_path = 'AttendanceTracker/data/B.TechAcademicCalender_S3_S5_S7July24-Dec24andandS4_S6_S8.pdf'
    working_days = extract_working_days_from_pdf(pdf_path)
    print("Working days extracted from PDF:", working_days)
