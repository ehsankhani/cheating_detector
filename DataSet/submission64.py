import xml.etree.ElementTree as ET

class Book:
    def __init__(self, title, author, year, price):
        self.title = title
        self.author = author
        self.year = year
        self.price = price

class BookProcessor:
    def __init__(self, input_file):
        self.input_file = input_file
        self.books = []

    def load_books(self):
        tree = ET.parse(self.input_file)
        root = tree.getroot()
        for book_elem in root.findall('book'):
            title = book_elem.find('title').text
            author = book_elem.find('author').text
            year = int(book_elem.find('year').text)
            price = float(book_elem.find('price').text)
            self.books.append(Book(title, author, year, price))

    def filter_books(self, year):
        return [book for book in self.books if book.year > year]

    def calculate_average_price(self, books):
        total_price = sum(book.price for book in books)
        return total_price / len(books) if books else 0

    def save_to_xml(self, books, average_price, output_file):
        root = ET.Element('bookSummary')
        avg_price_elem = ET.SubElement(root, 'averagePrice')
        avg_price_elem.text = str(average_price)
        for book in books:
            book_elem = ET.SubElement(root, 'book')
            ET.SubElement(book_elem, 'title').text = book.title
            ET.SubElement(book_elem, 'author').text = book.author
            ET.SubElement(book_elem, 'year').text = str(book.year)
            ET.SubElement(book_elem, 'price').text = str(book.price)

        tree = ET.ElementTree(root)
        tree.write(output_file)

def main():
    input_file = 'books.xml'
    output_file = 'summary_books.xml'
    year_threshold = 2000

    processor = BookProcessor(input_file)
    processor.load_books()
    filtered_books = processor.filter_books(year_threshold)
    average_price = processor.calculate_average_price(filtered_books)
    processor.save_to_xml(filtered_books, average_price, output_file)
    print(f"Book summary saved to {output_file}")

if __name__ == "__main__":
    main()
