class MobileDevice:
    def __init__(self, brand, model, os_version):
        # Initialize mobile device with brand, model, and OS version
        self.brand = brand
        self.model = model
        self.os_version = os_version

    def display_info(self):
        # Display device information
        print(f"Brand: {self.brand}, Model: {self.model}, OS Version: {self.os_version}")

def add_device(devices, brand, model, os_version):
    # Add a new device to the list
    device = MobileDevice(brand, model, os_version)
    devices.append(device)

def search_device_by_model(devices, model):
    # Search for a device by model
    for device in devices:
        if device.model == model:
            device.display_info()

def list_devices(devices):
    # List all devices
    for device in devices:
        device.display_info()

def main():
    # Main function to handle mobile devices
    devices = []
    add_device(devices, "Sony", "Xperia", "Android 10")
    add_device(devices, "Nokia", "8.3", "Android 11")

    print("List of mobile devices:")
    list_devices(devices)

    print("Search for devices by model:")
    search_device_by_model(devices, "8.3")


if __name__ == "main":
    main()