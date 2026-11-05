# Import Flask and request handling tools
from flask import Flask, render_template, request
# Import the functions we wrote in our analytics module
from insurance_analytics import load_and_analyze_data, generate_visualizations, estimate_premium

# Initialize the Flask application
app = Flask(__name__)

# Define what happens when the user visits the home page ('/')
@app.route('/', methods=['GET', 'POST'])
def home():
    # 1. Load data and get statistics from our analytics file
    df, avg_charge, max_charge, smoker_counts = load_and_analyze_data()
    
    # 2. Generate the graphs (saves them to static/plots/)
    generate_visualizations(df)
    
    # 3. Setup a variable to hold the estimated premium (defaults to None)
    estimated_cost = None
    
    # 4. Check if the user submitted the estimation form
    if request.method == 'POST':
        # Grab the data the user typed into the form
        user_age = request.form['age']
        user_bmi = request.form['bmi']
        user_smoker = request.form['smoker']
        
        # Call our estimation function
        estimated_cost = estimate_premium(user_age, user_bmi, user_smoker)
    
    # 5. Render the HTML page, passing all our calculated variables to it
    return render_template(
        'index.html', 
        avg_charge=avg_charge, 
        max_charge=max_charge,
        estimated_cost=estimated_cost
    )

# Run the application
if __name__ == '__main__':
    # debug=True allows the server to auto-reload when you make code changes
    app.run(debug=True)