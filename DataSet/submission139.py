import threading
import time

# Function that a thread will execute with an argument
def print_numbers(name, delay):
    for i in range(5):
        print(f"{name}: {i}")
        time.sleep(delay)  # Sleep based on the delay provided

# Main function to create and start multiple threads with arguments
def main():
    thread1 = threading.Thread(target=print_numbers, args=("Thread 1", 1))
    thread2 = threading.Thread(target=print_numbers, args=("Thread 2", 0.5))
    
    thread1.start()
    thread2.start()
    
    thread1.join()  # Wait for thread 1 to finish
    thread2.join()  # Wait for thread 2 to finish

if __name__ == "__main__":
    main()
