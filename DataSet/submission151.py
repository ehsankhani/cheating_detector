class Publication:
    def __init__(self, name, writer, cost, category):
        # Initialize publication with name, writer, cost, and category
        self.name = name
        self.writer = writer
        self.cost = cost
        self.category = category

    def show_details(self):
        # Show publication details, including category
        print(f"Name: {self.name}, Writer: {self.writer}, Cost: ${self.cost}, Category: {self.category}")


def add_publication(inventory, name, writer, cost, category):
    # Add a new publication to the inventory with category info
    pub = Publication(name, writer, cost, category)
    inventory.append(pub)


def display_inventory(inventory):
    # Display all publications in the inventory
    for pub in inventory:
        pub.show_details()


def start_app():
    # Main function to manage the publication store
    inventory = []
    add_publication(inventory, "The Power of Now", "Eckhart Tolle", 12.99, "Self-help")
    add_publication(inventory, "Homo Deus", "Yuval Noah Harari", 18.99, "Non-fiction")

    print("Publications in the inventory with category info:")
    display_inventory(inventory)


if __name__ == "__main__":
    start_app()
