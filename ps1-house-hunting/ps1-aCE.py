annual_salary = float(input("Please enter your annual salary?: "))
monthly_salary = annual_salary / 12
portion_saved = float(input("\nWhat portion are you saving? \nPlease enter a decimal between 0 and 1: "))
total_cost = float(input("\nPlease enter the cost of your dream home: "))

portion_down_payment = 0.25 * total_cost
current_savings = 0
months = 0

while current_savings < portion_down_payment:
    current_savings = (current_savings * (1 + 0.04/12)) + (portion_saved * monthly_salary)
    months +=1
print("You will have the down payment in", months, "months.")