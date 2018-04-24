# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Understand ==>
        #   1. you have to devise a function that operates as a user for the game 
        #   2. The game logic is already implemented by the guess function
        
        """
        # Naive Brute force logic
        # Leads to memory error for a huge number as input
        for i in range(n):
            if guess(i) == 0:
                return i
        """
        
        # Try leveraging the -1, +1 output as well rather than using the 0 - brute force logic alone.
        
        # start at the mid point, to eradicate half of the number in one step
        # could add odd or even logic below but in this case we need an int and one liner below suffices it
        # mid = n//2
        
        # Using a list of numbers fails the test with memory error again 
        # possibilities = map(int, range(n))
        
        if guess(n) == 0:
            return n
        
        select = n//2
            
        while select:
            if guess(select) == -1:
                n = select
                select = select//2
            elif guess(select) == 1:
                select = select + (n-select)//2
            else:
                return select
            
            

        
