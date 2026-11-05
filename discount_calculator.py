import numpy as np

def apply_discount(base_premium, discount_type):
    """
    Applies standard insurance discounts to a base premium using NumPy.
    """
    premium = np.float64(base_premium)
    
    # Dictionary storing discount percentages
    discounts = {
        'annual_pay': 0.10,   # 10% off for paying the whole year upfront
        'family_bundle': 0.15, # 15% off for bundling with family members
        'good_health': 0.05    # 5% off for passing a physical exam
    }
    
    # Check if the requested discount exists
    if discount_type in discounts:
        discount_amount = premium * discounts[discount_type]
        final_price = premium - discount_amount
        return round(final_price, 2), round(discount_amount, 2)
    else:
        # Return original premium and $0 discount if invalid
        return round(premium, 2), 0.00