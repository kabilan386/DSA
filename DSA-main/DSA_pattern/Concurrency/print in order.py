from threading import  Thread, Event

class Foo:
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.first_done.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_done.wait()
        printSecond()
        self.second_done.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_done.wait()
        printThird()




def printFirst():
    print("first", end=" ")


def printSecond():
    print("second", end=" ")


def printThird():
    print("third")


foo = Foo()

# Create threads in random order
t3 = Thread(target=foo.third, args=(printThird,))
t2 = Thread(target=foo.second, args=(printSecond,))
t1 = Thread(target=foo.first, args=(printFirst,))

# Start threads in random order
t3.start()
t2.start()
t1.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()

