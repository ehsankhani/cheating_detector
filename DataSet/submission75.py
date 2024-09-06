products = {}
customers = {}
sales = []

def add_product(product_id, name, price, quantity):
    products[product_id] = {"Name": name, "Price": price, "Quantity": quantity}

def add_customer(customer_id, name):
    customers[customer_id] = {"Name": name}

def process_sale(sale_id, customer_id, product_id, quantity):
    if product_id in products and customer_id in customers:
        if products[product_id]["Quantity"] >= quantity:
            products[product_id]["Quantity"] -= quantity
            sales.append({"SaleID": sale_id, "CustomerID": customer_id, "ProductID": product_id, "Quantity": quantity})
        else:
            print(f"Not enough stock for product {product_id}")
    else:
        print("Invalid product or customer ID")

def list_products():
    for product_id, info in products.items():
        print(f"ID: {product_id}, Name: {info['Name']}, Price: ${info['Price']}, Quantity: {info['Quantity']}")

def list_customers():
    for customer_id, info in customers.items():
        print(f"ID: {customer_id}, Name: {info['Name']}")

def list_sales():
    for sale in sales:
        print(f"Sale ID: {sale['SaleID']}, Customer ID: {sale['CustomerID']}, Product ID: {sale['ProductID']}, Quantity: {sale['Quantity']}")

def main():
    add_product(1, "Eggs", 3.99, 100)
    add_product(2, "Butter", 4.99, 50)

    add_customer(201, "Charlie")
    add_customer(202, "Daisy")

    process_sale(1, 201, 1, 12)  # Charlie buys 12 eggs
    process_sale(2, 202, 2, 5)   # Daisy buys 5 butters

    print("Product List:")
    list_products()

    print("\nCustomer List:")
    list_customers()

    print("\nSales List:")
    list_sales()

if __name__ == "__main__":
    main()
