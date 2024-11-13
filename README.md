Text Analysis Project

-Table of Contents

1. [Project Overview]
2. [Setup and Installation]
3. [Project Structure]
4. [How to Run]
5. [Output]
6. [Approach and Methodology]
7. [Troubleshooting]
8. [Dependencies]
9. [Contact Information]


-Project Overview
This project performs text analysis on articles from various URLs. It extracts text from given URLs, computes several text analysis metrics (such as sentiment scores, readability indices, and word statistics), and compiles the results into a structured output file.


-Setup and Installation
1. Ensure you have Python 3.7+ installed.
2. Clone this repository: `git clone [your-repo-url]`
3. Navigate to the project directory: `cd text-analysis-project`
4. Create a virtual environment: `python -m venv venv`
5. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
6. Install the required packages: `pip install -r requirements.txt`


-Project Structure
text-analysis-project/
│
├── data/
│   ├── raw/
│   │   └── Input.xlsx
│   └── processed/
│
├── scripts/
│   ├── scraper.py
│   ├── analyzer.py
│   └── compiler.py
│
├── output/
│   └── final_output.xlsx
│
├── README.md
└── requirements.txt


-How to Run
1. Ensure you're in the project directory with the virtual environment activated.
2. Run the web scraper: `python scripts/scraper.py`
3. Perform text analysis: `python scripts/analyzer.py`
4. Compile the results: `python scripts/compiler.py`
5. The final output will be in `output/final_output.xlsx`


-Output
The final output is an Excel file (`final_output.xlsx`) in the `output/` directory. It contains the following columns:
- URL_ID
- URL
- [List all the text analysis metrics]

Each row represents one article, with its URL and computed metrics.


-Approach and Methodology
1. Web Scraping: Used BeautifulSoup to extract article text from URLs.
2. Text Analysis: Implemented various NLP techniques using NLTK and textstat libraries.
3. Data Compilation: Used pandas to merge and structure the final output.


-Key decisions:
- Chose BeautifulSoup for its simplicity and effectiveness in HTML parsing.
- Used NLTK for sentiment analysis due to its comprehensive lexicon.
- Implemented error handling to manage potential issues with URL access or text processing.


Troubleshooting
- Issue: Script fails to access a URL
  Solution: Check your internet connection. If the problem persists, the website might be blocking web scraping.

- Issue: Text analysis produces unexpected results
  Solution: Ensure the extracted text is clean and properly formatted. Check for any encoding issues.

- Issue: Final output is missing data
  Solution: Verify that all intermediate files are present and contain data. Check the logs for any error messages during processing.


Dependencies
- Python 3.7+
- pandas
- numpy
- beautifulsoup4
- nltk
- textstat
- requests
- openpyxl

For a complete list with versions, see `requirements.txt`.

Contact Information
Name - Rakshit A Solanki
Email ID - rakshit.diu@gmail.com
