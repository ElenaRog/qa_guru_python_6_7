from pypdf import PdfReader

from tests.conftest import path_to_file_res

# TODO оформить в тест, добавить ассерты и использовать универсальный путь
pdffile = path_to_file_res('docs-pytest-org-en-latest.pdf')


def test_pdf_reading():
    reader = PdfReader(pdffile)
    number_of_pages = len(reader.pages)
    assert number_of_pages == 412

    page = reader.pages[0]
    text = page.extract_text()
    assert 'https://merlinux.eu/' in text
