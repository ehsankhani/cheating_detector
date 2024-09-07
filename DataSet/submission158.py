import sqlite3

def connect_database(db_name):
    # Establish a connection to a different SQLite database
    connection = sqlite3.connect(db_name)
    return connection

def initialize_table(connection):
    # Create a table called "staff"
    create_table_query = """CREATE TABLE IF NOT EXISTS staff (
                                staff_id integer PRIMARY KEY,
                                staff_name text NOT NULL,
                                staff_age integer
                            );"""
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
    except sqlite3.Error as error:
        print(error)

def add_employee(connection, staff):
    # Add a new entry into the staff table
    insert_query = ''' INSERT INTO staff(staff_name, staff_age)
                       VALUES(?,?) '''
    cur = connection.cursor()
    cur.execute(insert_query, staff)
    connection.commit()
    return cur.lastrowid

def fetch_all_employees(connection):
    # Retrieve all entries from the staff table
    cur = connection.cursor()
    cur.execute("SELECT * FROM staff")

    records = cur.fetchall()
    for record in records:
        print(record)

def run_operations():
    # Main function to handle database operations
    db_name = "organization.db"

    connection = connect_database(db_name)
    with connection:
        initialize_table(connection)
        staff = ('Alice', 38)
        add_employee(connection, staff)
        print("Current staff in the database:")
        fetch_all_employees(connection)

if __name__ == '__main__':
    run_operations()
