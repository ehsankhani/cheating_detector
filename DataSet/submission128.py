class Book:
    def __init__(self, title, author, price):
        # Initialize book with title, author, and price
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        # Display book information
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price}")

def add_book(books, title, author, price):
    # Add a new book to the store
    book = Book(title, author, price)
    books.append(book)

def search_book(books, title):
    # Search for a book by title
    for book in books:
        if book.title == title:
            book.display_info()

def list_books(books):
    # List all books in the store
    for book in books:
        book.display_info()

def main():
    # Main function to manage the book store
    books = []
    add_book(books, "The Great Gatsby", "F. Scott Fitzgerald", 8.99)
    add_book(books, "1984", "George Orwell", 9.99)
    
    print("Books available in the store:")
    list_books(books)
    
    print("\nSearching for '1984':")
    search_book(books, "1984")

if __name__ == "__main__":
    main()
