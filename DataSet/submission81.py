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

class Staff:
    def __init__(self, staff_id, name, position):
        self.staff_id = staff_id
        self.name = name
        self.position = position

class Bank:
    def __init__(self):
        self.customers = {}
        self.staff = {}

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def add_staff(self, staff):
        self.staff[staff.staff_id] = staff

    def list_customers(self):
        for customer in self.customers.values():
            print(f"ID: {customer.customer_id}, Name: {customer.name}, Balance: ${customer.balance}, Loans: ${customer.loans}")

    def list_staff(self):
        for staff in self.staff.values():
            print(f"ID: {staff.staff_id}, Name: {staff.name}, Position: {staff.position}")

def main():
    bank = Bank()

    customer1 = Customer(1, "Michael", 5000)
    customer2 = Customer(2, "Sarah", 6000)

    bank.add_customer(customer1)
    bank.add_customer(customer2)

    staff1 = Staff(201, "David", "Manager")
    staff2 = Staff(202, "Emma", "Clerk")

    bank.add_staff(staff1)
    bank.add_staff(staff2)

    customer1.apply_loan(1000)

    print("Customer List:")
    bank.list_customers()

    print("\nStaff List:")
    bank.list_staff()

if __name__ == "__main__":
    main()
