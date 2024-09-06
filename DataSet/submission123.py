class MobileDevice:
    def __init__(self, brand, model, os_version):
        # Initialize a mobile device with brand, model, and OS version
        self.brand = brand
        self.model = model
        self.os_version = os_version

    def display_info(self):
        # Display the mobile device information
        print(f"Brand: {self.brand}, Model: {self.model}, OS Version: {self.os_version}")

def add_device(devices, brand, model, os_version):
    # Add a new device to the list
    device = MobileDevice(brand, model, os_version)
    devices.append(device)

def remove_device(devices, model):
    # Remove a device by its model
    devices[:] = [device for device in devices if device.model != model]

def list_devices(devices):
    # List all devices
    for device in devices:
        device.display_info()

def main():
    # Main function to handle mobile devices
    devices = []
    add_device(devices, "Apple", "iPhone 13", "iOS 15")
    add_device(devices, "Google", "Pixel 6", "Android 12")
    
    print("List of mobile devices before removal:")
    list_devices(devices)
    
    remove_device(devices, "iPhone 13")
    
    print("List of mobile devices after removal:")
    list_devices(devices)

if __name__ == "__main__":
    main()
