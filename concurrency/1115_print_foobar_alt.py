import threading
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_event = threading.Event()
        self.bar_event = threading.Event()


    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            # print("foo ", i)
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.foo_event.clear()
            self.bar_event.set()
            self.foo_event.wait()
        
        self.bar_event.set()
        # print("foo exit")


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        self.bar_event.wait()
        for i in range(self.n):
            # print("bar ", i)
            
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.bar_event.clear()
            self.foo_event.set()
            self.bar_event.wait()
        
        self.foo_event.set()
        # print("bar exit")

def print1():
    print("1")


if __name__ == '__main__':
    foo = FooBar(2)
    t3 = threading.Thread(target=foo.foo, args=(print1,))

    t1 = threading.Thread(target=foo.bar, args=(print1,))

    t1.start()
    t3.start()


    t1.join()
    t3.join()