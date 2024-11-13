import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

def extract_article_text(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status() 
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the article title
        title = soup.find('h1').text.strip() if soup.find('h1') else ""
        
        # Extract the article body
        article_body = ""
        for paragraph in soup.find_all('p'):
            article_body += paragraph.text + "\n\n"
        
        # Combine title and body
        full_text = f"{title}\n\n{article_body}"
        
        return full_text
    
    except Exception as e:
        print(f"Error extracting text from {url}: {str(e)}")
        return ""

def save_text_to_file(text, file_name):
    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(text)
    except Exception as e:
        print(f"Error saving file {file_name}: {str(e)}")

def main():
    # Read the Input.xlsx file
    input_df = pd.read_excel("Input.xlsx")

    
    # Iterate through each row in the dataframe
    for index, row in input_df.iterrows():
        url = row['URL']
        url_id = row['URL_ID']
        
        # Extract text from the URL
        article_text = extract_article_text(url)
        
        # Save the extracted text to a file
        save_text_to_file(article_text, f"{url_id}.txt")
        
        print(f"Processed article {url_id}")

if __name__ == "__main__":
    main()

import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def extract_article_text(url):
    try:
        response = requests.get(url, headers=headers)
        # ... rest of the function ...
        time.sleep(1)  # Add a 1-second delay between requests
    except Exception as e:
        print(f"Error extracting text from {url}: {str(e)}")
        return "" 