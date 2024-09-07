import psutil


# Function to monitor CPU, memory, and disk utilization
def monitor_system_utilization():
    # Retrieve CPU utilization percentage
    cpu_util = psutil.cpu_percent(interval=1)
    print(f"CPU Utilization: {cpu_util}%")

    # Retrieve memory utilization
    mem_info = psutil.virtual_memory()
    print(f"Memory Utilization: {mem_info.percent}%")

    # Retrieve disk space utilization
    disk_info = psutil.disk_usage('/')
    print(f"Disk Utilization: {disk_info.percent}%")


# Core function to perform system checks
def execute_system_checks():
    monitor_system_utilization()


if __name__ == "__main__":
    execute_system_checks()
