from time import sleep


def task():
    # Specifies waiting time
    sleep(2)
    # Display message
    print("This is from another thread")


task()
