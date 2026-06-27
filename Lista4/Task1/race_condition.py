#!/usr/bin/env python3
from multiprocessing import Process, Value
import time

def increment(counter):
    for _ in range(100000):
        temp = counter.value
        temp += 1
        counter.value = temp

def decrement(counter):
    for _ in range(100000):
        temp = counter.value
        temp -= 1
        counter.value = temp

if __name__ == '__main__':
    print("=== Race Condition Demo ===")
    counter = Value('i', 0)
    print(f"Initial counter: {counter.value}")

    p1 = Process(target=increment, args=(counter,))
    p2 = Process(target=decrement, args=(counter,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"Final counter: {counter.value}")
    print("Expected: 0 (but will likely be different due to race condition)")
