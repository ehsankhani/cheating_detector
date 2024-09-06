customers = {}
staff = {}

def add_customer(customer_id, name, balance):
    customers[customer_id] = {"Name": name, "Balance": balance}

def add_staff(staff_id, name, position):
    staff[staff_id] = {"Name": name, "Position": position}

def deposit(customer_id, amount):
    if customer_id in customers:
        customers[customer_id]["Balance"] += amount
    else:
        print("Customer not found.")

def withdraw(customer_id, amount):
    if customer_id in customers:
        if customers[customer_id]["Balance"] >= amount:
            customers[customer_id]["Balance"] -= amount
        else:
            print("Insufficient funds.")
    else:
        print("Customer not found.")

def list_customers():
    for customer_id, info in customers.items():
        print(f"ID: {customer_id}, Name: {info['Name']}, Balance: ${info['Balance']}")

def list_staff():
    for staff_id, info in staff.items():
        print(f"ID: {staff_id}, Name: {info['Name']}, Position: {info['Position']}")

def main():
    add_customer(1, "Emma", 3000)
    add_customer(2, "John", 4000)

    add_staff(101, "Lisa", "Manager")
    add_staff(102, "Tom", "Teller")

    deposit(1, 500)
    withdraw(2, 1000)

    print("Customer List:")
    list_customers()

    print("\nStaff List:")
    list_staff()

if __name__ == "__main__":
    main()
