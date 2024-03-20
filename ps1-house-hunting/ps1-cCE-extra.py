#Extra personal excercise.
#How much does one have to earn at least, saving 100% of thier salary, to be able to afford the downpayment in 36 months?

low = 0
high = 7000
savings_rate = 1 #100%
down_payment = 250000
months = 0
iterations = 0
current_savings = 0
semi_annual_raise = 0.07
epsilon = 1


monthly_salary = (low + high)/2
while months <= 36:
    if months >= 6 and months%6 == 0:
        monthly_salary += monthly_salary * semi_annual_raise
    current_savings += (current_savings * 0.04/12) + (savings_rate * monthly_salary)
    months += 1

while abs(current_savings - down_payment) > epsilon:
    if (current_savings - down_payment) > epsilon:
        high = monthly_salary/(1.07**6)
    else:
        low = monthly_salary/(1.07**6)
    monthly_salary = (low + high)/2
    months = 0
    current_savings = 0
    while months <= 36:
        if months >= 6 and months%6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
        
        current_savings += (current_savings * 0.04/12) + (savings_rate * monthly_salary)
        months += 1
    iterations += 1
    
print("\nTotal iterations =",iterations)
print("You need to earn at least",  (monthly_salary/(1.07**6))*12, "as a starting annual salary to have the down payment in 36 months")

