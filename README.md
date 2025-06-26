# CSV-to-pptx

This project allows you to generate PowerPoint presentations (`.pptx`) and PDF catalogs from a CSV file containing product information. It uses Python libraries `python-pptx` and `pdfkit` to create the output files.

## Requirements

Before using this project, ensure you have the following installed:

- Python 3.x
- Required Python libraries (install via `pip`):
  - `pdfkit`
  - `python-pptx`
  - `requests`

You can install the required libraries by running:
```bash
    pip install -r requirements.txt
```
Additionally, for PDF generation, you need to download and install `wkhtmltopdf`. Follow the instructions provided here: [Installing wkhtmltopdf](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf).

## Usage

1. **Prepare the CSV file**:
   - Create a CSV file (`example_csv.csv`) containing product information. The first row should contain column headers, and subsequent rows should contain product data.
   - Example format:
     ```
     Product Name/Image URL
     Product1/Name1/Name2/Name3    https://example.com/image1.jpg
     Product2/Name1/Name2/Name3    https://example.com/image2.jpg
     ```

2. **Prepare templates**:
   - For PowerPoint generation, place your `.pptx` template in the `templates` folder (e.g., `templates/template.pptx`).
   - For PDF generation, place your HTML template in the `templates` folder (e.g., `templates/pdf_template.html`).

3. **Run the script**:
   - To generate a PowerPoint presentation:
     ```
     python main.py
     ```
   - To generate a PDF catalog:
     Uncomment the relevant lines in `main.py` and ensure the path to `wkhtmltopdf` is correctly set. Then run:
     ```
     python main.py
     ```

4. **Output**:
   - The generated `.pptx` file will be saved as `generated_pptx.pptx`.
   - The generated `.pdf` file will be saved as `generated_pdf.pdf`.

## Notes

- Ensure `wkhtmltopdf` is installed and its path is correctly set in the script for PDF generation.
- The templates should be properly formatted to match the expected structure for the project to work correctly.