from Bank import Bank

def main():
    bank = Bank()

    while True:
        print("\n=== Basic Bank System ===")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(name, initial_balance)

        elif choice == '2':
            name = input("Enter account holder's name: ")
            account = bank.get_account(name)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)

        elif choice == '3':
            name = input("Enter account holder's name: ")
            account = bank.get_account(name)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)

        elif choice == '4':
            name = input("Enter account holder's name: ")
            account = bank.get_account(name)
            if account:
                print(f"Current balance: {account.check_balance()}")

        elif choice == '5':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")


# Run the program
if __name__ == "__main__":
    main()
