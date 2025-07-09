monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your monthly expenses: ")
monthly_savings = int(monthly_income) - int(monthly_expenses)
pro_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
print("Your monthly savings are $" + str(monthly_savings))
print("Projected savings after one year, with interest, is: $" + str(pro_savings))

