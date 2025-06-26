import pdfkit
from pathlib import Path
from typing import List

def _split_template(template_path: str):
    head, tail, passed_grid = [], [], False
    with Path(template_path).open(encoding="utf-8") as fh:
        for line in fh:
            if not passed_grid:
                head.append(line)
                if line.strip() == '<div class="grid">':
                    passed_grid = True
                continue
            tail.append(line)
    return "".join(head), "".join(tail)


def _one_grid_item(name_parts: List[str], img_url: str):
    n1, n2, n3 = name_parts
    return f"""\
        <div class="grid-item">
            <img src="{img_url}" alt="Product Image">
            <div class="product-name">
                <p class="bold">{n1}</p>
                <p>{n2}</p>
                <p>{n3}</p>
            </div>
        </div>"""

def generate_pdf(template_path: str, products: List[dict], output_pdf: str, wkhtmltopdf_bin: str = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe") -> None:

    head, tail = _split_template(template_path)

    blocks = [_one_grid_item(prod["name"], prod["image"]) for prod in products]
    html = head + "\n".join(blocks) + tail

    cfg = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_bin)
    options = {
        "enable-local-file-access": True,
        "disable-smart-shrinking": True,
        "no-stop-slow-scripts": True,
    }
    pdfkit.from_string(html, output_pdf, configuration=cfg, options=options)
    print(f"Katalog PDF wygenerowany: {output_pdf}")
