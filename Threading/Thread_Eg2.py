from time import sleep
from threading import Thread


def task(sleep_time, message):
    # block for a moment
    sleep(sleep_time)
    # display a message
    print(message)


# create a thread
thread = Thread(target=task, args=(1.5, 'New message from another string'))

# run the thread
thread.start()

# wait for the thread to finish
print('Waiting for the thread...')
thread.join()
