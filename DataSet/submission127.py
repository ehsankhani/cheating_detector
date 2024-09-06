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
    # Add a new book to the book store
    book = Book(title, author, price)
    books.append(book)

def list_books(books):
    # List all books in the store
    for book in books:
        book.display_info()

def main():
    # Main function to handle book store operations
    books = []
    add_book(books, "The Catcher in the Rye", "J.D. Salinger", 10.99)
    add_book(books, "To Kill a Mockingbird", "Harper Lee", 7.99)
    
    print("Books available in the store:")
    list_books(books)

if __name__ == "__main__":
    main()
