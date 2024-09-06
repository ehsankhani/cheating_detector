import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ 
    Create a database connection to the SQLite database specified by db_file 
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection to {db_file} successful.")
    except Error as e:
        print(f"Error: {e}")
    return conn

def create_table(conn):
    """
    Create a table named "patients"
    """
    sql_create_patients_table = """CREATE TABLE IF NOT EXISTS patients (
                                       patient_id integer PRIMARY KEY,
                                       patient_name text NOT NULL,
                                       patient_age integer
                                   );"""
    try:
        c = conn.cursor()
        c.execute(sql_create_patients_table)
        print("Table 'patients' created successfully.")
    except Error as e:
        print(f"Error: {e}")

def insert_patient(conn, patient):
    """
    Insert a new patient into the patients table
    """
    sql = ''' INSERT INTO patients(patient_name, patient_age)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, patient)
    conn.commit()
    return cur.lastrowid

def select_all_patients(conn):
    """
    Query all rows in the patients table
    """
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM patients")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")

def main():
    """
    Main function to execute database operations with custom path
    """
    database = "hospital.db"  # Custom database path

    conn = create_connection(database)
    if conn is not None:
        create_table(conn)
        patient = ('Alice', 30)
        insert_patient(conn, patient)
        print("Patients in the database:")
        select_all_patients(conn)
    else:
        print("Error! Cannot create the database connection.")

if __name__ == '__main__':
    main()
