class Vehicle:
    def __init__(self, brand, type, manufacture_year):
        # Initialize a vehicle with brand, type, and manufacture year
        self.brand = brand
        self.type = type
        self.manufacture_year = manufacture_year

    def show_details(self):
        # Show vehicle details
        print(f"Brand: {self.brand}, Type: {self.type}, Year: {self.manufacture_year}")

def register_vehicle(vehicle_list, brand, type, manufacture_year):
    # Register a new vehicle to the system
    vehicle = Vehicle(brand, type, manufacture_year)
    vehicle_list.append(vehicle)

def show_all_vehicles(vehicle_list):
    # Display all registered vehicles
    for vehicle in vehicle_list:
        vehicle.show_details()

def run_vehicle_system():
    # Manage vehicle registration
    vehicle_list = []
    register_vehicle(vehicle_list, "Honda", "Civic", 2020)
    register_vehicle(vehicle_list, "Chevrolet", "Camaro", 2019)

    print("Registered vehicles:")
    show_all_vehicles(vehicle_list)

if __name__ == "__main__":
    run_vehicle_system()
