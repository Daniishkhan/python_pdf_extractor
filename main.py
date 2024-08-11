import PyPDF2
import os

#find current directory and turn it into a string
current_directory = os.getcwd()
pdf_directory = f"{current_directory}"

#function to extract pdf data for every pdf in directory
def extract_pdf_data():
    data = {}
    # loop over all files in directory
    for files in os.listdir(pdf_directory):
        if files.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, files)
            extracted_data = ""
            #open pdf
            with open(pdf_path, 'rb') as pdf_file:
                reader = PyPDF2.PdfReader(pdf_file)
                #extract the data
                for page in reader.pages:
                    extracted_data += page.extract_text()
                data[files] = extracted_data
    return {"data": data}


if __name__ == "__main__":
    data= extract_pdf_data()
    print(data)
