import sqlite3

def create_connection(db_file):
    # Create a connection to a different SQLite database
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    # Create a table named "employees"
    sql_create_employees_table = """CREATE TABLE IF NOT EXISTS employees (
                                        employee_id integer PRIMARY KEY,
                                        employee_name text NOT NULL,
                                        employee_age integer
                                    );"""
    try:
        c = conn.cursor()
        c.execute(sql_create_employees_table)
    except sqlite3.Error as e:
        print(e)

def insert_employee(conn, employee):
    # Insert a new employee into the employees table
    sql = ''' INSERT INTO employees(employee_name, employee_age)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, employee)
    conn.commit()
    return cur.lastrowid

def select_all_employees(conn):
    # Query all rows in the employees table
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")

    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    # Main function to execute database operations
    database = "company.db"

    conn = create_connection(database)
    with conn:
        create_table(conn)
        employee = ('Bob', 45)
        insert_employee(conn, employee)
        print("Employees in the database:")
        select_all_employees(conn)

if __name__ == '__main__':
    main()
