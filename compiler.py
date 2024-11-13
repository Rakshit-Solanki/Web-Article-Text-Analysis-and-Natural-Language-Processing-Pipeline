import pandas as pd
import os
import logging


def reorder_columns(df):
    column_order = [
        'URL_ID', 'URL',
        'POSITIVE SCORE', 'NEGATIVE SCORE', 'POLARITY SCORE',
        'SUBJECTIVITY SCORE', 'AVG SENTENCE LENGTH',
        'PERCENTAGE OF COMPLEX WORDS', 'FOG INDEX',
        'AVG NUMBER OF WORDS PER SENTENCE', 'COMPLEX WORD COUNT',
        'WORD COUNT', 'SYLLABLE PER WORD',
        'PERSONAL PRONOUNS', 'AVG WORD LENGTH'
    ]
    
    # Reorder the columns
    return df[column_order]

def fill_missing_values(df):
    # Fill missing numerical values with 0
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_columns] = df[numeric_columns].fillna(0)
    
    # Fill missing text values with an empty string
    text_columns = df.select_dtypes(include=['object']).columns
    df[text_columns] = df[text_columns].fillna('')
    
    return df

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        # Read the original input file
        input_df = pd.read_excel('E:\IP\Black Coffer assignment/Input.xlsx')
        
        # Read the analysis results
        analysis_df = pd.read_csv('E:\IP\Black Coffer assignment/text_analysis_results.csv')
        
        # Merge the dataframes
        merged_df = pd.merge(input_df, analysis_df, on='URL_ID', how='left')
        
        # Handle missing values
        merged_df = fill_missing_values(merged_df)

        # Reorder columns to match the Output Data Structure
        final_df = reorder_columns(merged_df)
        
        # Save the final output
        final_df.to_excel('E:\IP\Black Coffer assignment/final_output.xlsx', index=False)
        print("Final output saved to E:\IP\Black Coffer assignment/final_output.xlsx")
        logging.info("Data compilation and output generation completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during compilation: {str(e)}")
        raise

if __name__ == "__main__":
    main()