class Customer:
    def __init__(self, customer_id, name, balance):
        self.customer_id = customer_id
        self.name = name
        self.balance = balance
        self.loans = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def apply_loan(self, amount):
        self.loans += amount
        self.balance += amount

class Bank:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def find_customer(self, customer_id):
        return self.customers.get(customer_id, None)

    def list_customers(self):
        for customer in self.customers.values():
            print(f"ID: {customer.customer_id}, Name: {customer.name}, Balance: ${customer.balance}, Loans: ${customer.loans}")

def main():
    bank = Bank()

    customer1 = Customer(1, "Alice", 1000)
    customer2 = Customer(2, "Bob", 1500)

    bank.add_customer(customer1)
    bank.add_customer(customer2)

    customer1.deposit(500)
    customer2.withdraw(200)
    customer1.apply_loan(300)

    print("Customer List:")
    bank.list_customers()

if __name__ == "__main__":
    main()
