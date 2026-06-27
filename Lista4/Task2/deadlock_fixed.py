#!/usr/bin/env python3
from multiprocessing import Process, Lock
import time

def process1(lock1, lock2):
    with lock1:
        print("Process 1: Acquired lock 1")
        time.sleep(1)
        print("Process 1: Waiting for lock 2...")
        with lock2:
            print("Process 1: Acquired lock 2")
    print("Process 1: Released locks")

def process2(lock1, lock2):
    with lock1:
        print("Process 2: Acquired lock 1")
        time.sleep(1)
        print("Process 2: Waiting for lock 2...")
        with lock2:
            print("Process 2: Acquired lock 2")
    print("Process 2: Released locks")

if __name__ == '__main__':
    print("=== Deadlock Fixed - Acquire Locks in Same Order ===")
    print("Both processes acquire lock1 first, then lock2\n")

    lock1 = Lock()
    lock2 = Lock()

    p1 = Process(target=process1, args=(lock1, lock2))
    p2 = Process(target=process2, args=(lock1, lock2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("\nNo deadlock! Both processes completed successfully.")
