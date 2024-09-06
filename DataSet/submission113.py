import sqlite3

def create_connection(db_file):
    # Establish connection to the SQLite database
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    # Create a table named "customers"
    sql_create_customers_table = """CREATE TABLE IF NOT EXISTS customers (
                                        customer_id integer PRIMARY KEY,
                                        full_name text NOT NULL,
                                        customer_age integer
                                    );"""
    try:
        c = conn.cursor()
        c.execute(sql_create_customers_table)
    except sqlite3.Error as e:
        print(e)

def insert_customer(conn, customer):
    # Insert a new customer into the customers table
    sql = ''' INSERT INTO customers(full_name, customer_age)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, customer)
    conn.commit()
    return cur.lastrowid

def select_all_customers(conn):
    # Query all rows in the customers table
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers")

    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    # Main function to run the database operations
    database = "customers.db"

    conn = create_connection(database)
    with conn:
        create_table(conn)
        customer = ('Alice', 32)
        insert_customer(conn, customer)
        print("Customers in the database:")
        select_all_customers(conn)

if __name__ == '__main__':
    main()
