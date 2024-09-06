class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, quantity):
        self.quantity += quantity

    def update_price(self, price):
        self.price = price

class Supermarket:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product):
        self.inventory[product.product_id] = product

    def update_stock(self, product_id, quantity):
        if product_id in self.inventory:
            self.inventory[product_id].update_quantity(quantity)

    def list_inventory(self):
        for product in self.inventory.values():
            print(f"ID: {product.product_id}, Name: {product.name}, Price: ${product.price}, Quantity: {product.quantity}")

def main():
    supermarket = Supermarket()

    product1 = Product(1, "Milk", 1.99, 50)
    product2 = Product(2, "Bread", 2.49, 30)

    supermarket.add_product(product1)
    supermarket.add_product(product2)

    supermarket.update_stock(1, 20)  # Add 20 units to Milk
    supermarket.update_stock(2, -5)  # Remove 5 units from Bread

    print("Inventory List:")
    supermarket.list_inventory()

if __name__ == "__main__":
    main()
