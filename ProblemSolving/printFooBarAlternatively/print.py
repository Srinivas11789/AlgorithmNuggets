# Logic 2: Threading Events - 100 pass 71% faster

from threading import Event

class FooBar(object):
    def __init__(self, n):
        self.n = n
        self.trigger_bar = Event()
        self.trigger_foo = Event()
        self.trigger_foo.set()


    def foo(self, printFoo):
        for i in xrange(self.n):
            self.trigger_foo.wait()
            self.trigger_foo.clear()
            printFoo()
            self.trigger_bar.set()


    def bar(self, printBar):
        for i in xrange(self.n):
            self.trigger_bar.wait()
            self.trigger_bar.clear()
            printBar()
            self.trigger_foo.set()


# Logic 1: While loop with state variable ( both using one and two state variables )
# * This logic works with proper output but does not pass when submit ( not sure why? )
"""
class FooBar(object):
    def __init__(self, n):
        self.n = n
        #self.trigger_bar = False
        #self.trigger_foo = True
        self.trigger = True


    def foo(self, printFoo):
        for i in xrange(self.n):
            #while not self.trigger_foo:
            #    pass
            while not self.trigger:
                pass
            printFoo()
            self.trigger = False
            #self.trigger_foo = False
            #self.trigger_bar = True


    def bar(self, printBar):
        for i in xrange(self.n):
            #while not self.trigger_bar:
            #    pass
            while self.trigger:
                pass
            printBar()
            self.trigger = True
            #self.trigger_bar = False
            #self.trigger_foo = True
"""

