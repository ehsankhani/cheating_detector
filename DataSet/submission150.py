import threading
import time


# Function executed by threads with a custom identifier
def display_count(tag, wait_time):
    for count in range(5):
        print(f"{tag}: {count}")
        time.sleep(wait_time)  # Pause for the specified time


# Core function to initiate and manage threads
def run_threads():
    t1 = threading.Thread(target=display_count, args=("Worker 1", 1.2))
    t2 = threading.Thread(target=display_count, args=("Worker 2", 0.6))

    t1.start()
    t2.start()

    t1.join()  # Ensure t1 completes
    t2.join()  # Ensure t2 completes


if __name__ == "__main__":
    run_threads()
