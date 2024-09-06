import threading
import time

# Function that a thread will execute
def print_numbers():
    for i in range(5):
        print(f"Thread 1: {i}")
        time.sleep(1)  # Sleep for 1 second between prints

# Main function to create and start the thread
def main():
    thread1 = threading.Thread(target=print_numbers)
    thread1.start()
    thread1.join()  # Wait for the thread to complete

if __name__ == "__main__":
    main()
