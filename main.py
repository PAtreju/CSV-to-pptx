import csv
import pdfkit

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

def generate_pdf(products, output_filename):
    # HTML template for the catalog
    html_template = """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f8ff;
                margin: 0;
                padding: 0;
            }
            .page {
                width: 210mm;
                height: 297mm;
                margin: 0 auto;
                padding: 20mm;
                box-sizing: border-box;
                background-color: #ffffff;
            }
            .grid {
                display: flex;
                flex-wrap: wrap;
                gap: 20px;
            }
            .grid-item {
                width: calc(50% - 10px);
                text-align: center;
                border: 1px solid #ddd;
                padding: 10px;
                box-sizing: border-box;
            }
            .grid-item img {
                max-width: 100%;
                height: auto;
            }
            .product-name {
                margin-top: 10px;
                font-size: 14px;
                color: #333;
            }
        </style>
    </head>
    <body>
    """

    # Add product data to the HTML
    html_template += '<div class="page"><div class="grid">'
    for product in products:
        html_template += f"""
        <div class="grid-item">
            <img src="{product['image']}" alt="Product Image">
            <div class="product-name">{product['name']}</div>
        </div>
        """
    html_template += '</div></div></body></html>'

    # Configure pdfkit with wkhtmltopdf path
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_string(html_template, output_filename, configuration=config)

if __name__ == "__main__":
    filename = "eksport produktów pod katalog canva B2B v2.csv"
    output_pdf = "katalog_B2B.pdf"

    products = read_csv(filename)
    generate_pdf(products, output_pdf)
    print(f"Katalog wygenerowany: {output_pdf}")