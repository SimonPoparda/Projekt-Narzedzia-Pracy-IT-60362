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

def process2(lock1, lock2):
    with lock2:
        print("Process 2: Acquired lock 2")
        time.sleep(1)
        print("Process 2: Waiting for lock 1...")
        with lock1:
            print("Process 2: Acquired lock 1")

if __name__ == '__main__':
    print("=== Deadlock Demo ===")
    print("This program will hang due to circular lock dependency")
    print("Press Ctrl+C to stop\n")

    lock1 = Lock()
    lock2 = Lock()

    p1 = Process(target=process1, args=(lock1, lock2))
    p2 = Process(target=process2, args=(lock1, lock2))

    p1.start()
    p2.start()

    p1.join(timeout=5)
    p2.join(timeout=5)

    if p1.is_alive() or p2.is_alive():
        print("\nDeadlock detected! Processes are stuck.")
        p1.terminate()
        p2.terminate()
