class Automobile:
    def __init__(self, manufacturer, model_name, production_year):
        # Initialize automobile details
        self.manufacturer = manufacturer
        self.model_name = model_name
        self.production_year = production_year

    def print_info(self):
        # Print the automobile information
        print(f"Manufacturer: {self.manufacturer}, Model: {self.model_name}, Year: {self.production_year}")

def add_automobile(automobiles, manufacturer, model_name, production_year):
    # Add a new automobile to the list
    automobile = Automobile(manufacturer, model_name, production_year)
    automobiles.append(automobile)

def display_automobiles(automobiles):
    # Display all automobiles in the list
    for automobile in automobiles:
        automobile.print_info()

def automobile_management():
    # Manage automobile data
    automobiles = []
    add_automobile(automobiles, "BMW", "X5", 2017)
    add_automobile(automobiles, "Audi", "A4", 2022)

    print("Automobiles in the showroom:")
    display_automobiles(automobiles)

if __name__ == "__main__":
    automobile_management()
