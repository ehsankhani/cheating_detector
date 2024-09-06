import threading
import time

# A shared resource (counter)
counter = 0
lock = threading.Lock()

# Function that increments the counter in a thread-safe way
def increment_counter():
    global counter
    for _ in range(5):
        time.sleep(1)
        with lock:
            counter += 1
            print(f"Thread {threading.current_thread().name} incremented counter to {counter}")

# Main function to create and manage threads with locking mechanism
def main():
    thread1 = threading.Thread(target=increment_counter, name="Thread 1")
    thread2 = threading.Thread(target=increment_counter, name="Thread 2")
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

    print(f"Final counter value: {counter}")

if __name__ == "__main__":
    main()
