def get_health_recommendation(bmi, smoker):
    """
    Returns a customized health tip based on BMI and smoking status.
    """
    # Convert inputs
    bmi_value = float(bmi)
    smoker_status = str(smoker).strip().lower()
    
    tips = []
    
    # Check BMI categories
    if bmi_value < 18.5:
        tips.append("Your BMI indicates you are underweight. Consider a nutrient-rich diet.")
    elif bmi_value > 25.0:
        tips.append("Your BMI is above the standard range. Incorporating daily cardio could lower your premiums over time.")
    else:
        tips.append("Your BMI is in a healthy range. Great job maintaining your weight!")
        
    # Check smoking status
    if smoker_status == 'yes':
        tips.append("Smoking adds a $15,000 penalty to your premium. Quitting will drastically reduce your costs.")
        
    # Join tips into a single string
    return " | ".join(tips)