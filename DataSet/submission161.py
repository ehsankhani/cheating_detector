class Novel:
    def __init__(self, name, writer, cost, category):
        # Initialize novel with name, writer, cost, and category
        self.name = name
        self.writer = writer
        self.cost = cost
        self.category = category

    def show_details(self):
        # Display novel information including category
        print(f"Name: {self.name}, Writer: {self.writer}, Cost: ${self.cost}, Category: {self.category}")


def include_novel(collection, name, writer, cost, category):
    # Add a new novel to the collection with category information
    novel = Novel(name, writer, cost, category)
    collection.append(novel)


def display_novels(collection):
    # List all novels in the collection
    for novel in collection:
        novel.show_details()


def run_bookstore():
    # Main function to manage bookstore operations
    collection = []
    include_novel(collection, "The Alchemist", "Paulo Coelho", 10.49, "Fiction")
    include_novel(collection, "Sapiens", "Yuval Noah Harari", 14.99, "Non-fiction")

    print("Novels available in the collection with category info:")
    display_novels(collection)


if __name__ == "__main__":
    run_bookstore()
