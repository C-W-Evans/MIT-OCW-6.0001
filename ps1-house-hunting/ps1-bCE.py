annual_salary = float(input("Please enter your annual salary?: "))
monthly_salary = annual_salary / 12
portion_saved = float(input("\nWhat portion are you saving?: "))
total_cost = float(input("\nPlease enter the cost of your dream home: "))
semi_annual_raise = float(input("\nPlease enter your semi­annual salary raise: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
months = 0

while current_savings < portion_down_payment:
    if months >= 6 and months%6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
     
    current_savings += (current_savings * (0.04/12)) + (portion_saved * monthly_salary)
    months +=1

print("\nYou will have the down payment in", months, "months.")

