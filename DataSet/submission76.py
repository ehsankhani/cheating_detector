products = {}
staff = {}

def add_product(product_id, name, price, quantity):
    products[product_id] = {"Name": name, "Price": price, "Quantity": quantity}

def add_staff(staff_id, name, role):
    staff[staff_id] = {"Name": name, "Role": role}

def update_stock(product_id, quantity):
    if product_id in products:
        products[product_id]["Quantity"] += quantity
    else:
        print(f"Product ID {product_id} not found in inventory.")

def list_products():
    for product_id, info in products.items():
        print(f"ID: {product_id}, Name: {info['Name']}, Price: ${info['Price']}, Quantity: {info['Quantity']}")

def list_staff():
    for staff_id, info in staff.items():
        print(f"ID: {staff_id}, Name: {info['Name']}, Role: {info['Role']}")

def main():
    add_product(1, "Juice", 2.99, 80)
    add_product(2, "Cookies", 1.99, 120)

    add_staff(301, "Emma", "Cashier")
    add_staff(302, "John", "Manager")

    update_stock(1, 20)  # Add 20 units to Juice
    update_stock(2, -15) # Remove 15 units from Cookies

    print("Product List:")
    list_products()

    print("\nStaff List:")
    list_staff()

if __name__ == "__main__":
    main()
