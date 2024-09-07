class Car:
    def __init__(self, make, model, year):
        # Initialize car with make, model, and year
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        # Display car details
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

def add_car(cars, make, model, year):
    # Add a new car to the list
    car = Car(make, model, year)
    cars.append(car)

def list_cars(cars):
    # List all cars
    for car in cars:
        car.display_info()

def main():
    # Main function to manage car data
    cars = []
    add_car(cars, "Toyota", "Corolla", 2018)
    add_car(cars, "Ford", "Mustang", 2021)

    print("Cars in the garage:")
    list_cars(cars)

if __name__ == "__main__":
    main()
