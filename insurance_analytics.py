# Import required libraries
import pandas as pd
import numpy as np
import matplotlib
# Use 'Agg' backend so Matplotlib generates images in the background without opening UI windows
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_and_analyze_data(filepath="data/insurance.csv"):
    """
    Reads the CSV file using Pandas and calculates basic statistics using Numpy.
    """
    # Read the dataset into a Pandas DataFrame
    df = pd.read_csv(filepath)
    
    # Calculate average charges using NumPy
    avg_charge = np.mean(df['charges'])
    
    # Calculate the maximum charge
    max_charge = np.max(df['charges'])
    
    # Count how many smokers vs non-smokers exist
    smoker_counts = df['smoker'].value_counts().to_dict()
    
    return df, round(avg_charge, 2), round(max_charge, 2), smoker_counts

def generate_visualizations(df):
    """
    Generates data visualizations using Seaborn and Matplotlib, and saves them as images.
    """
    # Ensure the static/plots directory exists to save images
    os.makedirs('static/plots', exist_ok=True)
    
    # 1. Clear any existing plots in memory
    plt.clf() 
    
    # 2. Create a scatter plot: Age vs Insurance Charges
    # x-axis is age, y-axis is charges, color-coded by smoker status
    sns.scatterplot(data=df, x='age', y='charges', hue='smoker')
    plt.title('Age vs Insurance Charges')
    
    # Save the plot to the static folder so the HTML file can display it
    plt.savefig('static/plots/age_vs_charges.png')
    
    # Clear memory again for the next plot
    plt.clf()
    
    # 3. Create a bar chart: Average charges for smokers vs non-smokers
    sns.barplot(data=df, x='smoker', y='charges')
    plt.title('Average Charges: Smoker vs Non-Smoker')
    
    # Save the second plot
    plt.savefig('static/plots/smoker_vs_charges.png')

def estimate_premium(age, bmi, is_smoker):
    """
    A mathematical rule-based function to estimate insurance premium using Numpy operations.
    (Acts as a replacement for an ML model)
    """
    # Convert inputs to Numpy floats for calculation
    age = np.float64(age)
    bmi = np.float64(bmi)
    
    # Base premium cost
    base_cost = 2000.0
    
    # Penalty for age: $250 for every year of age
    age_penalty = age * 250.0
    
    # Penalty for BMI: $100 for every BMI point
    bmi_penalty = bmi * 100.0
    
    # Heavy penalty if the user is a smoker ($15,000)
    smoker_penalty = 15000.0 if is_smoker == 'yes' else 0.0
    
    # Calculate total estimated cost
    total_estimate = base_cost + age_penalty + bmi_penalty + smoker_penalty
    
    return round(total_estimate, 2)