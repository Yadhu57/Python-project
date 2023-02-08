from time import sleep
from threading import Thread


def task():
    # Block for a moment
    sleep(2)
    # Display message
    print("This is from another thread")


# Create a Thread
thread = Thread(target=task)
"""
Next, we can create an instance of the threading. Thread class and specify our function name as the "target" argument
in the constructor
"""
# run the thread

thread.start()

# The start() function does not block, means it returns immediately
