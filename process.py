import os
import time
from multiprocessing import Process

def func_1():
    pid = os.getpid()
    print(f"Функция 1, PID: {pid}")
    time.sleep(2)


def func_2():
    pid = os.getpid()
    print(f"Функция 2, PID: {pid}")
    time.sleep(3)


def func_3():
    pid = os.getpid()
    print(f"Функция 3, PID: {pid}")
    time.sleep(4)


def func_4():
    pid = os.getpid()
    print(f"Функция 4, PID: {pid}")
    time.sleep(5)

if __name__ == "__main__":
    
    p1 = Process(target=func_1)  
    p2 = Process(target=func_2) 
    p3 = Process(target=func_3) 
    p4 = Process(target=func_4) 


    for process in [p1, p2, p3, p4]:
        process.start()
    

    for process in [p1, p2, p3, p4]:
        process.join()   

    print("Все процессы завершены!")