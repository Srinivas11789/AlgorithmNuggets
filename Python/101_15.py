# Inheritance and Abstract Method in Python
# * Inheritance can be accomplished with declaration in the class head
# * Inherited constructors can be accessed by directly reference the parent class name or by using the super method
# * Abstract methods defined in the parent class can be defined in the child class with the same method name
# * When a parent class is inhertied it is mandatory to define its abstract methods else errors would be thrown
# * Why abstract class? - It throws a error reminding to implement or decorate the particular method when inheritance is performed

from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        super(MyBook,self).__init__(title,author)
        self.price = price
    
    def display(self):
        print "Title: "+ self.title
        print "Author: "+ self.author
        print "Price: "+str(self.price)
        
    
title=raw_input()
author=raw_input()
price=int(raw_input())
new_novel=MyBook(title,author,price)
new_novel.display()
