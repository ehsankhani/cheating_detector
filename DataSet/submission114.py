import sqlite3

def create_connection(db_file):
    # Establish a database connection
    conn = sqlite3.connect(db_file)
    return conn

def create_table(conn):
    # Create a table named "users"
    sql_create_users_table = """CREATE TABLE IF NOT EXISTS users (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    age integer
                                );"""
    try:
        c = conn.cursor()
        c.execute(sql_create_users_table)
    except sqlite3.Error as e:
        print(e)

def insert_user(conn, user):
    # Insert a new user into the users table
    sql = ''' INSERT INTO users(name, age)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()
    return cur.lastrowid

def delete_user(conn, user_id):
    # Delete a user by user id
    sql = 'DELETE FROM users WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (user_id,))
    conn.commit()

def select_all_users(conn):
    # Query all rows in the users table
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    # Main function to execute database operations
    database = "test.db"

    conn = create_connection(database)
    with conn:
        create_table(conn)
        user = ('John', 28)
        insert_user(conn, user)
        delete_user(conn, 1)  # Example of deleting a user with id 1
        print("Users in the database:")
        select_all_users(conn)

if __name__ == '__main__':
    main()
