import threading
import time

# Function that a thread will execute
def print_numbers():
    for i in range(5):
        print(f"Thread 1: {i}")
        time.sleep(1)  # Sleep for 1 second between prints

# Main function to create and start a daemon thread
def main():
    thread1 = threading.Thread(target=print_numbers)
    thread1.daemon = True  # Set thread as daemon
    thread1.start()
    
    time.sleep(2)  # Main thread sleeps for 2 seconds

if __name__ == "__main__":
    main()
