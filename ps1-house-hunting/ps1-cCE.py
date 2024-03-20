current_savings = 0
annual_salary = int(input("Enter your starting annual salary: "))
monthly_salary = annual_salary / 12
semi_annual_raise = 0.07
down_payment = 250000
epsilon = 100
low = 0
high = 10000
savings_rate = int((low + high)/2)
iterations = 0

for months in range(0 , 36):
    if months >= 6 and months%6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
    
    current_savings += (current_savings * 0.04/12) + (savings_rate/10000 * monthly_salary)
    iterations += 1
    
# Initialising the bisection search with a savings rate of .5
if current_savings >= down_payment/2: 
    while abs(current_savings - down_payment) > epsilon:       
        if (current_savings - down_payment) > epsilon:
            high = savings_rate
        else:
            low = savings_rate
        savings_rate = int((low + high)/2)
        monthly_salary = annual_salary / 12
        current_savings = 0
        for months in range(0 , 36):
            if months >= 6 and months%6 == 0:
                monthly_salary += monthly_salary * semi_annual_raise
    
            current_savings += (current_savings * 0.04/12) + (savings_rate/10000 * monthly_salary)
        iterations += 1
    print("\nTotal iterations =",iterations)    
    print("You will need to save", savings_rate/10000, "of your salary per month.")
else:
    print("It is not possible to pay the down payment in three years.")