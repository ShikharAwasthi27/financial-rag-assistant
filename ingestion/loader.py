import fitz
from pathlib import Path


class FinancialDocumentLoader:

    def load_pdf(self, file_path):
        doc = fitz.open(file_path)

        pages = []

        for page_num, page in enumerate(doc):
            text = page.get_text()

            pages.append({
                "text": text,
                "page": page_num + 1
            })

        return pages

    def load_directory(self, directory):
        documents = []

        pdf_files = Path(directory).glob("*.pdf")

        for pdf in pdf_files:
            pages = self.load_pdf(str(pdf))

            documents.append({
                "file_name": pdf.name,
                "pages": pages
            })

        return documents
