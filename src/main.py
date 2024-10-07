import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        # Extract text from all pages
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def find_holidays(text):
    holidays = []
    sundays = []
    
    # Keywords for holidays (you can extend this list)
    holiday_keywords = ['Onam', 'Independence Day', 'Mahanavami', 'Vijayadasami', 'Christmas', 'New Year']
    
    # Find specific holiday names in the text
    for keyword in holiday_keywords:
        holiday_matches = re.findall(fr'\b{keyword}\b', text)
        holidays.extend(holiday_matches)

    # Find all Sundays (they are always holidays)
    # Example pattern: "Sun 7" or "Sunday 7" for date format in the PDF
    sunday_pattern = r'\bSun\b \d{1,2}'
    sundays_found = re.findall(sunday_pattern, text)
    
    # Add Sundays to a separate list
    sundays.extend(sundays_found)
    
    # Remove duplicates (if any)
    sundays = list(set(sundays))
    
    return holidays, sundays

if __name__ == "__main__":
    # Provide the path to your PDF file
    pdf_path = 'data/B.TechAcademicCalender_S3_S5_S7July24-Dec24andandS4_S6_S8.pdf'
    
    # Extract text from the PDF
    text = extract_text_from_pdf(pdf_path)
    
    # Find holidays in the extracted text
    holidays, sundays = find_holidays(text)
    
    # Print the holidays
    print("Specific Holidays found in the PDF:", holidays)
    print("Sundays (holidays) found in the PDF:", sundays)
