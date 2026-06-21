import threading
from queue import Queue

numbers = [11, 15, 17, 20, 23, 29, 35, 41]

q = Queue()

for num in numbers:
    q.put(num)


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def worker():
    while not q.empty():
        num = q.get()

        result = is_prime(num)

        print(
            f"{threading.current_thread().name} "
            f"processed {num} -> Prime: {result}"
        )

        q.task_done()


t1 = threading.Thread(target=worker, name="Thread-1")
t2 = threading.Thread(target=worker, name="Thread-2")

t1.start()
t2.start()

t1.join()
t2.join()

print("All numbers processed")