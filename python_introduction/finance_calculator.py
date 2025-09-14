# finance_calculator.py

# Prompt the user for income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Annual projection with 5% simple interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Display results
print("Your monthly savings are $" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: $" + str(projected_savings) + ".")
