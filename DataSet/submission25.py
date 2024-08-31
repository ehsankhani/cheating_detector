class BankMachine:
    def __init__(self, starting_balance=0):
        self.current_balance = starting_balance

    def display_balance(self):
        """Shows the current balance."""
        print(f"Balance available: ${self.current_balance:.2f}")

    def add_funds(self, deposit_amount):
        """Adds funds to the account."""
        if deposit_amount > 0:
            self.current_balance += deposit_amount
            print(f"${deposit_amount:.2f} added to your account.")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw_funds(self, withdrawal_amount):
        """Removes funds from the account."""
        if withdrawal_amount > self.current_balance:
            print("Insufficient funds for this transaction.")
        elif withdrawal_amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.current_balance -= withdrawal_amount
            print(f"${withdrawal_amount:.2f} withdrawn from your account.")

    def menu_options(self):
        """Displays available options in the ATM menu."""
        print("\n=== Welcome to Your Bank ===")
        print("1. View Balance")
        print("2. Make a Deposit")
        print("3. Make a Withdrawal")
        print("4. Exit")
        print("============================\n")

def run_bank_machine():
    atm_machine = BankMachine(100)  # Initial balance set to $100
    while True:
        atm_machine.menu_options()
        user_choice = input("Select an option (1-4): ")

        if user_choice == '1':
            atm_machine.display_balance()
        elif user_choice == '2':
            deposit = float(input("Enter deposit amount: $"))
            atm_machine.add_funds(deposit)
        elif user_choice == '3':
            withdrawal = float(input("Enter withdrawal amount: $"))
            atm_machine.withdraw_funds(withdrawal)
        elif user_choice == '4':
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a valid option.")

if __name__ == "__main__":
    run_bank_machine()
