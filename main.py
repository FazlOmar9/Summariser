import sys
from reader import extract_text_from_pdf
from inference import summarize

if __name__ == "__main__":
    pages = extract_text_from_pdf("docs/reliance.pdf")
    summary = summarize(pages, 2)
    
    # Redirect stdout to a file
    with open("./summary.txt", "w", encoding='utf-8') as f:
        sys.stdout = f
        for i, s in enumerate(summary):
            print(f"=============== Summary for pages {i * 2 + 1}, {i * 2 + 2}: ===============\n")
            print(f"{s}\n\n")
        sys.stdout = sys.__stdout__  # Reset redirect.