import xml.etree.ElementTree as ET

def parse_books_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    return [
        {
            'title': book.find('title').text,
            'author': book.find('author').text,
            'year': int(book.find('year').text),
            'price': float(book.find('price').text)
        }
        for book in root.findall('book')
    ]

def get_books_after_year(books, year):
    return list(filter(lambda book: book['year'] > year, books))

def compute_average(books):
    total_price = sum(map(lambda book: book['price'], books))
    return total_price / len(books) if books else 0

def output_to_xml(books, average_price, output_file):
    root = ET.Element('booksReport')
    avg_price_elem = ET.SubElement(root, 'averagePrice')
    avg_price_elem.text = str(average_price)
    for book in books:
        book_elem = ET.SubElement(root, 'book')
        ET.SubElement(book_elem, 'title').text = book['title']
        ET.SubElement(book_elem, 'author').text = book['author']
        ET.SubElement(book_elem, 'year').text = str(book['year'])
        ET.SubElement(book_elem, 'price').text = str(book['price'])

    tree = ET.ElementTree(root)
    tree.write(output_file)

def main():
    input_file = 'books.xml'
    output_file = 'filtered_books.xml'
    year_filter = 2000

    books = parse_books_from_xml(input_file)
    recent_books = get_books_after_year(books, year_filter)
    avg_price = compute_average(recent_books)
    output_to_xml(recent_books, avg_price, output_file)
    print(f"Books report saved to {output_file}")

if __name__ == "__main__":
    main()
