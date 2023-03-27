
import threading
import time
import serial


def thread1_task():
    print("Thread1 started")
    time.sleep(2)
    print("Thread1 ended")


def thread2_task():
    print("Thread2 started")
    time.sleep(5)
    print("Thread2 ended")

def thread_com_init():
    ser = serial.Serial('COM10',115200)
    return ser

def thread_com_task():
    print("Thread3 started")
    ser = thread_com_init()
    while True:
        if ser.inWaiting() > 0:
            data = ser.readline()
            if 'OPEN' in str(data):
                print("!!!Door opened!!!")
            # print(data)
    print("Thread3 ended")

if __name__ == "__main__":
    thread1 = threading.Thread(target=thread1_task)
    thread2 = threading.Thread(target=thread2_task)
    thread3 = threading.Thread(target=thread_com_task)

    thread1.start()
    thread2.start()
    thread3.start()
    

    thread1.join()
    thread2.join()

    print("Both threads finished execution!")

