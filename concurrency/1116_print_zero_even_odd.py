"""
https://leetcode.com/problems/print-zero-even-odd/?envType=problem-list-v2&envId=concurrency
"""

from typing import Callable
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_event = threading.Event()
        self.even_event = threading.Event()
        self.odd_event = threading.Event()
        self.len = 0
        self.turn = 0
        self.curr = 1
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:

        while True:
            # print("zero len", self.len)

            if self.len >= 2 * self.n:
                break
           
            printNumber("0")
            self.len += 1

            self.zero_event.clear()

            if self.turn == 0:
                self.turn += 1
                self.odd_event.set()
            else:
                self.turn -= 1
                self.even_event.set()
            
            self.zero_event.wait() 
        
        print("zero exit")
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:

        self.even_event.wait()
        while True:
            # print("even len", self.len)
            if self.len >= 2 * self.n:
                self.odd_event.set()
                break
            
            printNumber(self.curr)
            self.curr += 1
            self.len += 1

            self.even_event.clear()
            if self.len >= 2 * self.n:
                self.odd_event.set()
                break
            self.zero_event.set()  

            self.even_event.wait()

        
        self.zero_event.set()

        print("even exit")
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:

        self.odd_event.wait()
        while True:
            # print("odd len", self.len)
            
            if self.len >= 2 * self.n:
                self.even_event.set()
                break
            
            printNumber(self.curr)
            self.curr += 1
            self.len += 1

            self.odd_event.clear()
            if self.len >= 2 * self.n:
                self.even_event.set()
                break
            self.zero_event.set()
            self.odd_event.wait()

        self.zero_event.set()

        print("odd exit")


def print_number(x):
    print(x, end="")


if __name__ == '__main__':

    # for i in range(1):
    #     print("\nstart -------------------------------------------")
    #     obj = ZeroEvenOdd(i+1)

    #     t2 = threading.Thread(target=obj.odd, args=(print_number,))
    #     t1 = threading.Thread(target=obj.even, args=(print_number,))

    #     t3 = threading.Thread(target=obj.zero, args=(print_number,))


    #     t3.start()
    #     t2.start()
    #     t1.start()


    #     t1.join()
    #     t2.join()
    #     t3.join()  
    zeroEvenOdd = ZeroEvenOdd(5);

    thread_zero = threading.Thread(target=zeroEvenOdd.zero, args=(lambda n: print(n, end=''),))
    thread_even = threading.Thread(target=zeroEvenOdd.even, args=(lambda n: print(n, end=''),))
    thread_odd = threading.Thread(target=zeroEvenOdd.odd, args=(lambda n: print(n, end=''),))

    threads = [thread_odd, thread_zero, thread_even, ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    



        
        