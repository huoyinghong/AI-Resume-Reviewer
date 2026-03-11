import io
import pdfplumber


def extract_text_from_pdf(file_bytes: bytes) -> str:
    all_text = []

    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                all_text.append(page_text)

    return "\n".join(all_text)