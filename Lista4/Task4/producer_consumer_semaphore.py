#!/usr/bin/env python3
from multiprocessing import Process, Lock, Semaphore, Value
import time

BUFFER_SIZE = 3

def producer(buffer_list, write_pos, produced_count, mutex, empty_sem, full_sem, producer_id):
    for i in range(5):
        item = f"Item_{producer_id}_{i}"
        empty_sem.acquire()
        with mutex:
            pos = write_pos.value
            buffer_list[pos] = item
            write_pos.value = (pos + 1) % BUFFER_SIZE
            produced_count.value += 1
            print(f"Producer {producer_id}: Produced {item} (Total: {produced_count.value})")
        full_sem.release()
        time.sleep(0.1)

def consumer(buffer_list, read_pos, consumed_count, mutex, empty_sem, full_sem, consumer_id):
    for i in range(5):
        full_sem.acquire()
        with mutex:
            pos = read_pos.value
            item = buffer_list[pos]
            read_pos.value = (pos + 1) % BUFFER_SIZE
            consumed_count.value += 1
            print(f"Consumer {consumer_id}: Consumed {item} (Total: {consumed_count.value})")
        empty_sem.release()
        time.sleep(0.15)

if __name__ == '__main__':
    print("=== Producer-Consumer with Semaphores + Mutex ===\n")

    buffer_list = [''] * BUFFER_SIZE
    write_pos = Value('i', 0)
    read_pos = Value('i', 0)
    produced_count = Value('i', 0)
    consumed_count = Value('i', 0)
    mutex = Lock()
    empty_sem = Semaphore(BUFFER_SIZE)
    full_sem = Semaphore(0)

    producers = [Process(target=producer, args=(buffer_list, write_pos, produced_count, mutex, empty_sem, full_sem, i)) for i in range(2)]
    consumers = [Process(target=consumer, args=(buffer_list, read_pos, consumed_count, mutex, empty_sem, full_sem, i)) for i in range(2)]

    for p in producers + consumers:
        p.start()

    for p in producers + consumers:
        p.join()

    print(f"\nProduced: {produced_count.value}, Consumed: {consumed_count.value}")
    print("Producer-Consumer with semaphores completed successfully!")
