import xml.etree.ElementTree as ET

def load_books_from_xml(file_path):
    xml_tree = ET.parse(file_path)
    xml_root = xml_tree.getroot()
    book_list = []
    for book in xml_root.findall('book'):
        book_list.append({
            'title': book.find('title').text,
            'author': book.find('author').text,
            'year': int(book.find('year').text),
            'price': float(book.find('price').text)
        })
    return book_list

def filter_books_after_year(book_list, year):
    return [book for book in book_list if book['year'] > year]

def avg_price_calculator(book_list):
    if not book_list:
        return 0
    total = sum(book['price'] for book in book_list)
    return total / len(book_list)

def save_results_to_xml(book_list, avg_price, output_file):
    root = ET.Element('booksSummary')
    avg_price_elem = ET.SubElement(root, 'averagePrice')
    avg_price_elem.text = str(avg_price)
    for book in book_list:
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
    year_threshold = 2000

    books = load_books_from_xml(input_file)
    recent_books = filter_books_after_year(books, year_threshold)
    avg_price = avg_price_calculator(recent_books)
    save_results_to_xml(recent_books, avg_price, output_file)
    print(f"Filtered books written to {output_file}")

if __name__ == "__main__":
    main()
