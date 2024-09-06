class Book:
    def __init__(self, title, author, price):
        # Initialize a book with title, author, and price
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        # Display the book information
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}")

def add_book(books, title, author, price):
    # Add a new book to the list
    book = Book(title, author, price)
    books.append(book)

def remove_book(books, title):
    # Remove a book by its title
    books[:] = [book for book in books if book.title != title]

def list_books(books):
    # List all books
    for book in books:
        book.display_info()

def main():
    # Main function to handle book store operations
    books = []
    add_book(books, "Moby Dick", "Herman Melville", 11.99)
    add_book(books, "Pride and Prejudice", "Jane Austen", 6.99)
    
    print("Books available before removal:")
    list_books(books)
    
    remove_book(books, "Moby Dick")
    
    print("\nBooks available after removal:")
    list_books(books)

if __name__ == "__main__":
    main()
