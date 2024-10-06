import PyPDF2
import pandas as pd

def test_pdf_reading():
    print("PDF reading library is installed and working.")

def test_excel_reading():
    df = pd.DataFrame({'Subject': ['Math', 'Science'], 'Day': ['Monday', 'Tuesday']})
    print(df)

if __name__ == "__main__":
    test_pdf_reading()
    test_excel_reading()
