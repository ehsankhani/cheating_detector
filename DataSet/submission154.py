import psutil

# Function to monitor CPU utilization
def monitor_cpu_utilization():
    # Retrieve CPU utilization percentage
    utilization = psutil.cpu_percent(interval=1)
    print(f"Current CPU Utilization: {utilization}%")

# Core function to execute the CPU monitoring
def run_monitor():
    monitor_cpu_utilization()

if __name__ == "__main__":
    run_monitor()
