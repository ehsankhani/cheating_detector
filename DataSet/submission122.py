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
    # Add a new device to the devices list
    device = MobileDevice(brand, model, os_version)
    devices.append(device)

def list_devices(devices):
    # List all devices in the system
    for device in devices:
        device.display_info()

def main():
    # Main function to manage mobile devices
    devices = []
    add_device(devices, "Apple", "iPhone 13", "iOS 15")
    add_device(devices, "Samsung", "Galaxy S21", "Android 11")
    
    print("List of mobile devices:")
    list_devices(devices)

if __name__ == "__main__":
    main()
