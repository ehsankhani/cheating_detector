from lxml import etree

def read_books(file_path):
    tree = etree.parse(file_path)
    root = tree.getroot()
    books = []
    for book in root.xpath('//book'):
        books.append({
            'title': book.find('title').text,
            'author': book.find('author').text,
            'year': int(book.find('year').text),
            'price': float(book.find('price').text)
        })
    return books

def filter_books_by_year(books, year):
    return [book for book in books if book['year'] > year]

def calculate_avg_price(books):
    if not books:
        return 0
    total_price = sum(book['price'] for book in books)
    return total_price / len(books)

def write_to_xml(books, avg_price, output_file):
    root = etree.Element('bookSummary')
    avg_elem = etree.SubElement(root, 'averagePrice')
    avg_elem.text = str(avg_price)
    for book in books:
        book_elem = etree.SubElement(root, 'book')
        title_elem = etree.SubElement(book_elem, 'title')
        title_elem.text = book['title']
        author_elem = etree.SubElement(book_elem, 'author')
        author_elem.text = book['author']
        year_elem = etree.SubElement(book_elem, 'year')
        year_elem.text = str(book['year'])
        price_elem = etree.SubElement(book_elem, 'price')
        price_elem.text = str(book['price'])

    tree = etree.ElementTree(root)
    tree.write(output_file, pretty_print=True)

def main():
    input_file = 'books.xml'
    output_file = 'recent_books.xml'
    year_filter = 2000

    books = read_books(input_file)
    filtered_books = filter_books_by_year(books, year_filter)
    average_price = calculate_avg_price(filtered_books)
    write_to_xml(filtered_books, average_price, output_file)
    print(f"XML output saved to {output_file}")

if __name__ == "__main__":
    main()
