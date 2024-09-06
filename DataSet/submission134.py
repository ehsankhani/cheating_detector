import openpyxl

# Function to read and print data from an Excel file
def read_excel(filename):
    # Load the workbook and select the active sheet
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    
    # Print the data from the sheet
    for row in sheet.iter_rows(values_only=True):
        print(row)

# Main function to read and print data from the Excel file
def main():
    print("Reading data from 'students_with_city.xlsx':")
    read_excel("students_with_city.xlsx")

if __name__ == "__main__":
    main()
