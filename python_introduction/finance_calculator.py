income = input("Enter your monthly income: ")
expenses = input("Enter your monthly expenses: ")
monthly_savings = int(income) - int(expenses)
pro_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
print("Your monthly savings are $" + str(monthly_savings))
print("Projected savings after one year, with interest, is: $" + str(pro_savings))

