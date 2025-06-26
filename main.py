import csv
from generate_pptx import generate_pptx
from generate_pdf import generate_pdf

def to_raw(string):
    return fr"{string}"

def read_csv(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)
        fields = to_raw(fields[0]).split('\t')
        for row in csvreader:
            row = row[0].split('\t')
            products.append({fields[0]: [i.strip() for i in row[0].split('/')], fields[1]: row[1]})
    return products

    return products


if __name__ == "__main__":
    filename = "example_csv.csv"
    template_filename_pptx = "templates/template.pptx"
    output_pptx = "generated_pptx.pptx"

    products = read_csv(filename)
    generate_pptx(template_filename_pptx, products, output_pptx)

# if __name__ == "__main__":
    filename = "example_csv.csv"
    template_filename_pdf = "templates/pdf_template.html"
    output_pdf = "generated_pdf.pdf"

    products = read_csv(filename)
    # wkhtmltopdf_path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    generate_pdf(template_filename_pdf, products, output_pdf) # add wkhtmltopdf_path as an argument if needed

