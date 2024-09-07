class Publication:
    def __init__(self, name, writer, cost):
        # Initialize publication with name, writer, and cost
        self.name = name
        self.writer = writer
        self.cost = cost

    def show_info(self):
        # Display publication details
        print(f"Name: {self.name}, Writer: {self.writer}, Cost: ${self.cost}")

    def modify_cost(self, updated_cost):
        # Modify the cost of the publication
        self.cost = updated_cost


def insert_publication(inventory, name, writer, cost):
    # Insert a new publication into the inventory
    publication = Publication(name, writer, cost)
    inventory.append(publication)


def change_publication_cost(inventory, name, updated_cost):
    # Change the cost of a publication by name
    for publication in inventory:
        if publication.name == name:
            publication.modify_cost(updated_cost)


def display_inventory(inventory):
    # List all publications
    for publication in inventory:
        publication.show_info()


def run_store():
    # Main function to handle the store inventory
    inventory = []
    insert_publication(inventory, "Pride and Prejudice", "Jane Austen", 10.49)
    insert_publication(inventory, "1984", "George Orwell", 8.99)

    print("Publications available before cost modification:")
    display_inventory(inventory)

    change_publication_cost(inventory, "1984", 6.99)

    print("\nPublications available after cost modification:")
    display_inventory(inventory)


if __name__ == "__main__":
    run_store()
