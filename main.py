from reader import extract_text_from_pdf
from inference import summarize

if __name__ == "__main__":
    pages = extract_text_from_pdf("docs/reliance.pdf")
    summary = summarize(pages, 2)
