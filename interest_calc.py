# Python compound interest calculator

initial_amount = 0
interest_rate = 0
years = 0

while True:
    initial_amount = float(input("Enter the initial deposit: "))
    if initial_amount < 0:
        print("Amount cannot be negative.")
    else:
        break

while interest_rate <= 0:
    interest_rate = float(input("Enter the annual interest rate (in %): "))
    if interest_rate <= 0:
        print("Rate must be greater than zero.")

while years <= 0:
    years = int(input("Enter the number of years: "))
    if years <= 0:
        print("Years must be greater than zero.")

final_balance = initial_amount * pow((1 + interest_rate / 100), years)
print(f"Total balance after {years} year(s): ${final_balance:.2f}")