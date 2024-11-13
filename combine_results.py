import pandas as pd

def main():
    # Read the original input file
    input_df = pd.read_excel('E:\IP\Black Coffer assignment/Input.xlsx')
    
    # Read the analysis results
    analysis_df = pd.read_csv('E:\IP\Black Coffer assignment/text_analysis_results.csv')
    
    # Merge the dataframes
    merged_df = pd.merge(input_df, analysis_df, on='URL_ID', how='left')
    
    # Save the final output
    merged_df.to_excel('E:\IP\Black Coffer assignment/final_output.xlsx', index=False)
    print("Final output saved to E:\IP\Black Coffer assignment/final_output.xlsx")

if __name__ == "__main__":
    main()