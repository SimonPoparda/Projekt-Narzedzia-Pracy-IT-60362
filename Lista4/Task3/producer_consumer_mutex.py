#!/usr/bin/env python3
from multiprocessing import Process, Lock, Value
import time
import random

BUFFER_SIZE = 5

def producer(buffer_list, buffer_index, lock, producer_id):
    for i in range(10):
        item = f"Item_{producer_id}_{i}"
        with lock:
            if buffer_index.value < BUFFER_SIZE:
                buffer_list[buffer_index.value] = item
                buffer_index.value += 1
                print(f"Producer {producer_id}: Produced {item}, Buffer: {buffer_index.value}/{BUFFER_SIZE}")
            else:
                print(f"Producer {producer_id}: Buffer full, skipping {item}")
        time.sleep(random.uniform(0.1, 0.3))

def consumer(buffer_list, buffer_index, lock, consumer_id):
    consumed = 0
    while consumed < 5:
        with lock:
            if buffer_index.value > 0:
                buffer_index.value -= 1
                item = buffer_list[buffer_index.value]
                print(f"Consumer {consumer_id}: Consumed {item}, Buffer: {buffer_index.value}/{BUFFER_SIZE}")
                consumed += 1
            else:
                print(f"Consumer {consumer_id}: Buffer empty, waiting...")
        time.sleep(random.uniform(0.2, 0.4))

if __name__ == '__main__':
    print("=== Producer-Consumer with Mutex (1 Lock) ===\n")

    buffer_list = [''] * BUFFER_SIZE
    buffer_index = Value('i', 0)
    lock = Lock()

    producers = [Process(target=producer, args=(buffer_list, buffer_index, lock, i)) for i in range(2)]
    consumers = [Process(target=consumer, args=(buffer_list, buffer_index, lock, i)) for i in range(2)]

    for p in producers + consumers:
        p.start()

    for p in producers + consumers:
        p.join()

    print("\nProducer-Consumer completed successfully")
