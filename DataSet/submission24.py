class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        """Displays the current balance."""
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        """Deposits a specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited to your account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws a specified amount from the account."""
        if amount > self.balance:
            print("Insufficient balance for this withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn from your account.")

    def show_menu(self):
        """Displays the ATM menu."""
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("====================\n")

def main():
    atm = ATM(100)  # Initial balance of $100
    while True:
        atm.show_menu()
        choice = input("Please select an option (1-4): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: $"))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: $"))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()
