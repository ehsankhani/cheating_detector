import xml.etree.ElementTree as ET

def extract_books_from_xml(file_path):
    xml_tree = ET.parse(file_path)
    xml_root = xml_tree.getroot()
    return [
        {
            'title': book.find('title').text,
            'author': book.find('author').text,
            'year': int(book.find('year').text),
            'price': float(book.find('price').text)
        }
        for book in xml_root.findall('book')
    ]

def select_books_after_year(books, year):
    return list(filter(lambda b: b['year'] > year, books))

def average_price(books):
    total = sum(map(lambda b: b['price'], books))
    return total / len(books) if books else 0

def save_xml_output(books, avg_price, output_file):
    root = ET.Element('booksReport')
    avg_elem = ET.SubElement(root, 'averagePrice')
    avg_elem.text = str(avg_price)
    for book in books:
        book_elem = ET.SubElement(root, 'book')
        ET.SubElement(book_elem, 'title').text = book['title']
        ET.SubElement(book_elem, 'author').text = book['author']
        ET.SubElement(book_elem, 'year').text = str(book['year'])
        ET.SubElement(book_elem, 'price').text = str(book['price'])

    xml_tree = ET.ElementTree(root)
    xml_tree.write(output_file)

def main():
    input_file = 'books.xml'
    output_file = 'filtered_books.xml'
    year_cutoff = 2000

    books = extract_books_from_xml(input_file)
    recent_books = select_books_after_year(books, year_cutoff)
    avg_price = average_price(recent_books)
    save_xml_output(recent_books, avg_price, output_file)
    print(f"Books data written to {output_file}")

if __name__ == "__main__":
    main()
