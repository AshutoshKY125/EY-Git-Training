import pandas as pd
import numpy as np

def generate_text_report(filepath="data/insurance.csv", output_path="summary_report.txt"):
    """
    Reads the insurance dataset and writes a statistical summary to a text file.
    """
    df = pd.read_csv(filepath)
    
    # Calculate key metrics using NumPy and Pandas
    total_records = len(df)
    avg_age = np.mean(df['age'])
    highest_charge = np.max(df['charges'])
    
    # Format the report string
    report_content = f"""
    --- INSURANCE DATA SUMMARY ---
    Total Customers Analyzed: {total_records}
    Average Customer Age: {round(avg_age, 1)} years
    Highest Premium Charged: ${round(highest_charge, 2)}
    ------------------------------
    """
    
    # Write the summary to a text file
    with open(output_path, "w") as file:
        file.write(report_content)
        
    print(f"Report successfully saved to {output_path}")

# Allow testing the file directly
if __name__ == '__main__':
    generate_text_report()