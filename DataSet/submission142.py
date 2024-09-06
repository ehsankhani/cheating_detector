import psutil

# Function to check CPU usage
def check_cpu_usage():
    # Get CPU usage percentage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

# Main function to run the CPU check
def main():
    check_cpu_usage()

if __name__ == "__main__":
    main()
