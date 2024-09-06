import openpyxl

# Function to create and write different data into an Excel file
def create_excel_different_data(filename):
    # Create a new workbook and select the active sheet
    wb = openpyxl.Workbook()
    sheet = wb.active
    
    # Write some different data into the sheet
    sheet['A1'] = "Product"
    sheet['B1'] = "Price"
    
    sheet['A2'] = "Laptop"
    sheet['B2'] = 999.99
    
    sheet['A3'] = "Smartphone"
    sheet['B3'] = 499.99
    
    # Save the workbook
    wb.save(filename)
    print(f"File '{filename}' created with product data successfully!")

# Main function to create the Excel file with product data
def main():
    create_excel_different_data("products.xlsx")

if __name__ == "__main__":
    main()
