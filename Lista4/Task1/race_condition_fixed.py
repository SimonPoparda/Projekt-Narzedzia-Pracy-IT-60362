#!/usr/bin/env python3
from multiprocessing import Process, Value, Lock

def increment(counter, lock):
    for _ in range(100000):
        with lock:
            counter.value += 1

def decrement(counter, lock):
    for _ in range(100000):
        with lock:
            counter.value -= 1

if __name__ == '__main__':
    print("=== Race Condition Fixed with Lock (Mutex) ===")
    counter = Value('i', 0)
    lock = Lock()
    print(f"Initial counter: {counter.value}")

    p1 = Process(target=increment, args=(counter, lock))
    p2 = Process(target=decrement, args=(counter, lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"Final counter: {counter.value}")
    print("Expected: 0 (with proper synchronization)")
