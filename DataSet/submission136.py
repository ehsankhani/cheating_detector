import openpyxl

# Function to create and write data into an Excel file
def create_and_update_excel(filename):
    # Create a new workbook and select the active sheet
    wb = openpyxl.Workbook()
    sheet = wb.active
    
    # Write some initial data into the sheet
    sheet['A1'] = "Employee"
    sheet['B1'] = "Salary"
    
    sheet['A2'] = "John"
    sheet['B2'] = 50000
    
    sheet['A3'] = "Jane"
    sheet['B3'] = 55000
    
    # Save the workbook
    wb.save(filename)
    
    # Reopen the workbook and update a cell
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    sheet['B2'] = 51000  # Updating John's salary
    
    # Save the updated workbook
    wb.save(filename)
    print(f"File '{filename}' updated successfully!")

# Main function to create and update the Excel file
def main():
    create_and_update_excel("employees.xlsx")

if __name__ == "__main__":
    main()
