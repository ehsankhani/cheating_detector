import xml.etree.ElementTree as ET

def read_books_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    books = []
    for book in root.findall('book'):
        books.append({
            'title': book.find('title').text,
            'author': book.find('author').text,
            'year': int(book.find('year').text),
            'price': float(book.find('price').text)
        })
    return books

def filter_books_by_year(books, year):
    return [book for book in books if book['year'] > year]

def calculate_average_price(books):
    if not books:
        return 0
    total_price = sum(book['price'] for book in books)
    return total_price / len(books)

def write_results_to_xml(books, average_price, output_file):
    root = ET.Element('bookSummary')
    avg_price_elem = ET.SubElement(root, 'averagePrice')
    avg_price_elem.text = str(average_price)
    for book in books:
        book_elem = ET.SubElement(root, 'book')
        title_elem = ET.SubElement(book_elem, 'title')
        title_elem.text = book['title']
        author_elem = ET.SubElement(book_elem, 'author')
        author_elem.text = book['author']
        year_elem = ET.SubElement(book_elem, 'year')
        year_elem.text = str(book['year'])
        price_elem = ET.SubElement(book_elem, 'price')
        price_elem.text = str(book['price'])

    tree = ET.ElementTree(root)
    tree.write(output_file)

def main():
    input_file = 'books.xml'
    output_file = 'filtered_books.xml'
    filter_year = 2000

    books = read_books_from_xml(input_file)
    recent_books = filter_books_by_year(books, filter_year)
    avg_price = calculate_average_price(recent_books)
    write_results_to_xml(recent_books, avg_price, output_file)
    print(f"Processed books saved to {output_file}")

if __name__ == "__main__":
    main()
