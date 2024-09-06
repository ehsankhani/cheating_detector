import openpyxl

# Function to create and write data into an Excel file
def create_excel(filename):
    # Create a new workbook and select the active sheet
    wb = openpyxl.Workbook()
    sheet = wb.active
    
    # Write some data into the sheet
    sheet['A1'] = "Name"
    sheet['B1'] = "Age"
    
    sheet['A2'] = "Alice"
    sheet['B2'] = 30
    
    sheet['A3'] = "Bob"
    sheet['B3'] = 25
    
    # Save the workbook
    wb.save(filename)
    print(f"File '{filename}' created and data written successfully!")

# Main function to create the Excel file
def main():
    create_excel("students_basic.xlsx")

if __name__ == "__main__":
    main()
