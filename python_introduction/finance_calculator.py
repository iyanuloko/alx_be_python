income = input("Enter your monthly income: ")
expenses = input("Enter your monthly expenses: ")
savings = int(income) - int(expenses)
pro_savings = (savings * 12) + (savings * 12 * 0.05)
print("Your monthly savings are $" + str(savings))
print("Projected savings after one year, with interest, is: $" + str(pro_savings))

