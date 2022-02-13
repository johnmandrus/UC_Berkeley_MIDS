income = float(input("What is your income: "))
if income <= 1000:
    tax = income*0.05
elif 1000 < income <= 2000:
    tax = 1000*0.05 + (income-1000)*0.1
elif income > 2000:
    tax = 1000*0.05 + 1000*0.1 + (income-2000)*0.15
print("The tax owed is: ", tax)