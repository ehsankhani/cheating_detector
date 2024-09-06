import psutil

# Function to check network and CPU usage
def check_network_and_cpu():
    # Get CPU usage percentage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    
    # Get network I/O statistics
    net_io = psutil.net_io_counters()
    print(f"Bytes Sent: {net_io.bytes_sent}, Bytes Received: {net_io.bytes_recv}")

# Main function to check network and CPU
def main():
    check_network_and_cpu()

if __name__ == "__main__":
    main()
