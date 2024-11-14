import fitz
from cleantext import clean


def preprocess_text(text: str) -> str:
    cleaned_text = clean(
        text,
        to_ascii=True,     # transliterate to closest ASCII representation
        lower=False,       # keep the text in its original case
        no_line_breaks=True,  # remove line breaks
        no_urls=False,      # remove URLs
        no_emails=False,    # remove email addresses
        no_phone_numbers=False,  # remove phone numbers
        no_numbers=False,  # keep numbers
        no_digits=False,   # keep digits
        no_currency_symbols=False,  # remove currency symbols
        no_punct=False,    # keep punctuations
        lang="en"          # specify the language for better cleaning
    )

    return cleaned_text


def extract_text_from_pdf(pdf_path: str) -> list:
    document = fitz.open(pdf_path)
    text = []

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        page_text = page.get_text()
        text.append(page_text)

    text = [preprocess_text(page_text) for page_text in text]
    return text
