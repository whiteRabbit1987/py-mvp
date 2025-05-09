# Python Banking Program

def main():
    balance, is_running = 0, True

    while is_running:
        print("**** BANKING ****"
            "\n1. Show Balance"
            "\n2. Deposit"
            "\n3. Withdraw"
            "\n4. Exit")
        choice = input("> ")

        if choice == '4':
            print("Goodbye.")
            is_running = False
        elif choice == '1':
            from banking_mods import show_balance
            show_balance(balance)
        elif choice == '2':
            from banking_mods import deposit
            balance += deposit()
        elif choice == '3':
            from banking_mods import withdraw
            balance -= withdraw(balance)
        else:
            print("Invalid input...exiting....")
            break
    print("Done..." if is_running else  "Have a nice day!")

if __name__ == '__main__':
    main()

