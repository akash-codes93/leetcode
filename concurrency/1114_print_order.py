"""
https://leetcode.com/problems/print-in-order/description/?envType=problem-list-v2&envId=concurrency
"""
from typing import Callable
import threading 


class Foo:
    def __init__(self):
        self.first_event = threading.Event()
        self.second_event = threading.Event()
        self.third_event = threading.Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:

        self.first_event.set()
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_event.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:

        self.second_event.wait()
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_event.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        self.third_event.wait()
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()


def printFirst():
    print("first")

def printSecond():
    print("second")

def printThird():
    print("third")


if __name__ == "__main__":
    foo = Foo()
    t3 = threading.Thread(target=foo.third, args=(printThird,))

    t1 = threading.Thread(target=foo.first, args=(printFirst,))
    t2 = threading.Thread(target=foo.second, args=(printSecond,))

    t2.start()
    t3.start()
    t1.start()

    t1.join()
    t2.join()
    t3.join()   
