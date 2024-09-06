import threading
import time

# Function that the first thread will execute
def print_numbers():
    for i in range(5):
        print(f"Thread 1: {i}")
        time.sleep(1)  # Sleep for 1 second between prints

# Function that the second thread will execute
def print_letters():
    for letter in "ABCDE":
        print(f"Thread 2: {letter}")
        time.sleep(0.5)  # Sleep for 0.5 seconds between prints

# Main function to create and start multiple threads
def main():
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)
    
    thread1.start()
    thread2.start()
    
    thread1.join()  # Wait for thread 1 to finish
    thread2.join()  # Wait for thread 2 to finish

if __name__ == "__main__":
    main()
