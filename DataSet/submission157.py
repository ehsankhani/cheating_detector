class Smartphone:
    def __init__(self, manufacturer, model_name, software_version):
        # Initialize smartphone with manufacturer, model name, and software version
        self.manufacturer = manufacturer
        self.model_name = model_name
        self.software_version = software_version

    def show_info(self):
        # Show smartphone details
        print(f"Manufacturer: {self.manufacturer}, Model: {self.model_name}, OS Version: {self.software_version}")


def register_device(device_list, manufacturer, model_name, software_version):
    # Register a new smartphone in the device list
    phone = Smartphone(manufacturer, model_name, software_version)
    device_list.append(phone)


def display_devices(device_list):
    # Display all registered smartphones
    for phone in device_list:
        phone.show_info()


def run_program():
    # Core function to manage smartphone registrations
    device_list = []
    register_device(device_list, "Google", "Pixel 6", "Android 12")
    register_device(device_list, "OnePlus", "9 Pro", "Android 11")

    print("Registered Smartphones:")
    display_devices(device_list)


if __name__ == "__main__":
    run_program()
