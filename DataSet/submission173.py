class MotorCar:
    def __init__(self, brand_name, car_model, year_of_manufacture):
        # Initialize motor car details
        self.brand_name = brand_name
        self.car_model = car_model
        self.year_of_manufacture = year_of_manufacture

    def show_info(self):
        # Display motor car info
        print(f"Brand: {self.brand_name}, Model: {self.car_model}, Year: {self.year_of_manufacture}")

def add_motor_car(car_list, brand_name, car_model, year_of_manufacture):
    # Add a new motor car to the car list
    motor_car = MotorCar(brand_name, car_model, year_of_manufacture)
    car_list.append(motor_car)

def show_all_motor_cars(car_list):
    # Show all motor cars in the list
    for motor_car in car_list:
        motor_car.show_info()

def car_system():
    # Manage car system
    car_list = []
    add_motor_car(car_list, "Tesla", "Model S", 2020)
    add_motor_car(car_list, "Nissan", "Altima", 2019)

    print("Cars in the system:")
    show_all_motor_cars(car_list)

if __name__ == "__main__":
    car_system()
