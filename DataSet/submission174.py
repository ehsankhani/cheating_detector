class AutomobileEntry:
    def __init__(self, car_make, car_version, build_year):
        # Initialize an automobile entry with make, version, and build year
        self.car_make = car_make
        self.car_version = car_version
        self.build_year = build_year

    def view_info(self):
        # View automobile details
        print(f"Make: {self.car_make}, Version: {self.car_version}, Year: {self.build_year}")

def enroll_car(car_registry, car_make, car_version, build_year):
    # Enroll a new car in the registry
    entry = AutomobileEntry(car_make, car_version, build_year)
    car_registry.append(entry)

def view_registered_cars(car_registry):
    # View all registered cars
    for entry in car_registry:
        entry.view_info()

def manage_car_registry():
    # Handle car registry management
    car_registry = []
    enroll_car(car_registry, "Mercedes", "C-Class", 2016)
    enroll_car(car_registry, "Volvo", "XC90", 2018)

    print("Cars in the registry:")
    view_registered_cars(car_registry)

if __name__ == "__main__":
    manage_car_registry()
