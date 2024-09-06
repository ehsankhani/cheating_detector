customers = {}
transactions = []

def add_customer(customer_id, name, balance):
    customers[customer_id] = {"Name": name, "Balance": balance}

def deposit(customer_id, amount):
    if customer_id in customers:
        customers[customer_id]["Balance"] += amount
        transactions.append({"CustomerID": customer_id, "Type": "Deposit", "Amount": amount})
    else:
        print("Customer not found.")

def withdraw(customer_id, amount):
    if customer_id in customers:
        if customers[customer_id]["Balance"] >= amount:
            customers[customer_id]["Balance"] -= amount
            transactions.append({"CustomerID": customer_id, "Type": "Withdraw", "Amount": amount})
        else:
            print("Insufficient funds.")
    else:
        print("Customer not found.")

def list_customers():
    for customer_id, info in customers.items():
        print(f"ID: {customer_id}, Name: {info['Name']}, Balance: ${info['Balance']}")

def list_transactions():
    for transaction in transactions:
        print(f"Customer ID: {transaction['CustomerID']}, Type: {transaction['Type']}, Amount: ${transaction['Amount']}")

def main():
    add_customer(1, "Charlie", 2000)
    add_customer(2, "Daisy", 2500)

    deposit(1, 300)
    withdraw(2, 500)

    print("Customer List:")
    list_customers()

    print("\nTransaction List:")
    list_transactions()

if __name__ == "__main__":
    main()
