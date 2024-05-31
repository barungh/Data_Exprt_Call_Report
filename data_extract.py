import PyPDF2
import re
import os
import glob
import time

# Function to extract information from the text
def extract_info(text):
    # Define regular expressions to match patterns
    customer_name_pattern = r'Customer Name\s*:\s*(.*?)\n'
    contact_person_pattern = r'Customer Contact Person\s*:\s*(.*?)\n'
    case_number_pattern = r'Case Number\s*:\s*(.*?)\n'
    serial_number_pattern = r'Product Serial Number\s*:\s*(.*?)\n'
    call_log_date_pattern = r'Call Log Date\s*:\s*(.*?)\n'
    system_fixed_date_pattern = r'System Fixed Date\s*:\s*(.*?)\n'

    # Extract information using regular expressions
    customer_name = re.search(customer_name_pattern, text).group(1).strip()
    contact_person = re.search(contact_person_pattern, text).group(1).strip()
    case_number = re.search(case_number_pattern, text).group(1).strip()
    serial_number = re.search(serial_number_pattern, text).group(1).strip()
    call_log_date = re.search(call_log_date_pattern, text).group(1).strip()
    system_fixed_date = re.search(system_fixed_date_pattern, text).group(1).strip()

    return customer_name, contact_person, case_number, serial_number, call_log_date, system_fixed_date


current_directory = os.getcwd()
pdf_files = glob.glob(os.path.join(current_directory, '*.pdf'))
for i, pdf_file in enumerate(pdf_files):
    # print(i+1)
    
    # print(os.path.basename(pdf_file))
    # Open the PDF file
    # file_path = "Call_Info-SRFR-SIL-13944.pdf"
    pdf_file = open(pdf_file, "rb")

    # Read the PDF file
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Extract text from each page
    pdf_text = []
    for page in pdf_reader.pages:
        pdf_text.append(page.extract_text())

    # Close the PDF file
    pdf_file.close()
    customer_name, contact_person, case_number, serial_number, call_log_date, system_fixed_date = extract_info(pdf_text[0])
    print("| {} | {} | {} | {} | {} | {} |".format(customer_name, contact_person, case_number, serial_number, call_log_date, system_fixed_date))
    time.sleep(2)