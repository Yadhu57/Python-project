# Multi threading
import time
import threading


def cal_square(num):
    print("CALCULATE THE SQUARE OF THE GIVEN NUMBER")
    for n in num:
        time.sleep(0.3)  # at each iteration it waits for 0.3 time
        print("Square is :", n * n)


def cal_cube(num):
    print("CALCULATE THE CUBE OF THE GIVEN NUMBER")
    for n in num:
        time.sleep(0.3)  # at each iteration it waits for 0.3 time
        print("cube is:", n * n * n)


arr = [4, 5, 6, 7, 2]  # given array or list

t1 = time.time()    # get total time to execute the functions

th1 = threading.Thread(target=cal_square, args=(arr,))    # thread object
th2 = threading.Thread(target=cal_cube, args=(arr,))      # thread object
th1.start()
th2.start()
th1.join()
th2.join()
print("Total time taken by threads is:", time.time() - t1)