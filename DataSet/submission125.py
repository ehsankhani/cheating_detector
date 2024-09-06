class MobileDevice:
    def __init__(self, brand, model, os_version):
        # Initialize mobile device with brand, model, and OS version
        self.brand = brand
        self.model = model
        self.os_version = os_version

    def display_info(self):
        # Display device information
        print(f"Brand: {self.brand}, Model: {self.model}, OS Version: {self.os_version}")

    def update_os(self, new_version):
        # Update the OS version of the device
        self.os_version = new_version

def add_device(devices, brand, model, os_version):
    # Add a new device to the list
    device = MobileDevice(brand, model, os_version)
    devices.append(device)

def update_device_os(devices, model, new_version):
    # Update the OS of a device with a given model
    for device in devices:
        if device.model == model:
            device.update_os(new_version)

def list_devices(devices):
    # List all devices
    for device in devices:
        device.display_info()

def main():
    # Main function to handle mobile devices
    devices = []
    add_device(devices, "Apple", "iPhone 13", "iOS 15")
    add_device(devices, "Samsung", "Galaxy S21", "Android 11")
    
    print("List of mobile devices before OS update:")
    list_devices(devices)
    
    update_device_os(devices, "Galaxy S21", "Android 12")
    
    print("List of mobile devices after OS update:")
    list_devices(devices)

if __name__ == "__main__":
    main()
