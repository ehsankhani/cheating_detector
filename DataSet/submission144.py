import psutil

# Function to check CPU, memory, and disk usage
def check_full_system_usage():
    # Get CPU usage percentage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    
    # Get memory usage
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")
    
    # Get disk usage
    disk_usage = psutil.disk_usage('/')
    print(f"Disk Usage: {disk_usage.percent}%")

# Main function to run full system checks
def main():
    check_full_system_usage()

if __name__ == "__main__":
    main()
