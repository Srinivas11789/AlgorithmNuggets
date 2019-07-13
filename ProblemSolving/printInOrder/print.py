# Logic 1: 100 pass 5% faster
# * Create state variables to maintain the order of execution
# * As the execution can be on any order, we make a blocking call by using while loops for the state variables
# * Only after the blocking call breaks the execution will happen thereby maintaining the order
"""
class Foo(object):
    def __init__(self):
        self.first_done = False
        self.second_done = False
        pass


    def first(self, printFirst):
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_done = True


    def second(self, printSecond):
    
        while not self.first_done:
            pass
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_done = True
            
            
    def third(self, printThird):

        while not self.second_done:
            pass
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
"""

# Logic 2:  Using Locks --> Events for trigerring ==> 70% faster
# * Create events based on the order of execution and use them

from threading import Event

class Foo(object):
    def __init__(self):
        self.first_done = Event()
        self.second_done = Event()


    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """
        
        printFirst()
        self.first_done.set()


    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.first_done.wait()
        printSecond()
        self.second_done.set()
        self.first_done.clear()
            
            
    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.second_done.wait()
        printThird()
        self.second_done.clear()


