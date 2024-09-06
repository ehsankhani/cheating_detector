import psutil

# Function to check CPU and memory usage
def check_system_usage():
    # Get CPU usage percentage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    
    # Get memory usage
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.percent}%")

# Main function to run CPU and memory checks
def main():
    check_system_usage()

if __name__ == "__main__":
    main()
