from tabula import read_pdf
from tabulate import tabulate
import json
def extract_data(pdf_file,file_inst):

    df = read_pdf(pdf_file,pages="all",multiple_tables=True) 
    file_inst.extracted_table_txt = df
    file_inst.save()
    


