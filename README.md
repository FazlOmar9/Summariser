# Financial Document Summarizer

## Overview
The Financial Document Summarizer is a Python-based tool that extracts text from a PDF file and generates a summarized version of its content. This is useful for quickly understanding key points in lengthy financial documents.

## Features
- Extracts text from financial PDFs.
- Summarizes the extracted content for quick insights.
- Simple and easy-to-use script.

## Requirements
Ensure you have the following installed before running the script:

- Python 3.x
- Required Python packages (see [Installation](#installation))

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/financial-doc-summarizer.git
   cd financial-doc-summarizer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Open `main.py` and set the document path in the following line:
   ```python
   pages = extract_text_from_pdf("docs/reliance.pdf")
   ```
   Replace `"docs/reliance.pdf"` with the path to your financial document.
2. Run the script:
   ```bash
   python main.py
   ```
3. The summarized content will be displayed in the console or saved to an output file, depending on implementation.

## File Structure
```
financial-doc-summarizer/
│── docs/
│   ├── reliance.pdf  # Sample financial document
│── main.py           # Main script to run the summarizer
│── inference.py     # Handles text summarization
│── reader.py      # Extracts text from PDFs
│── segment.py      # Segments extracted text into chunks
│── requirements.txt  # List of dependencies
│── README.md         # Project documentation
```

## License
This project is licensed under the MIT License.

## Contact
For any issues or suggestions, feel free to open an issue on GitHub or contact [fazlomr3@gmail.com].

