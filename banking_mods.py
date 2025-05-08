def show_balance(balance):
    print(f"Your balance is ${balance:.2f}\n")

def deposit():
    amt = float(input("\nEnter an amount to deposit: "))
    if amt < 0:
        print("Deposit must be over $0")
        return 0
    else:
        return amt

def withdraw(balance):
    amt = float(input("\nEnter an amount to withdraw: "))
    
    if amt > balance:
        print("Can't overdraft!")
        return 0
    else:
        return amt