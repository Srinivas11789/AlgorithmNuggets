class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Logic:
        # * Again, the confusion was at the copy decision to make
        #   - Already knew solution is something to work around the divisibility
        #   - example: for 20, we know 2, 4, 5 are divisible by 20 but going with 4 gives the minimum steps
        #   - Recursively going back from square root or half the number n and iterating for divisibility + being recursive helps...
        # * Inreference to the golang solution at https://leetcode.com/problems/2-keys-keyboard/discuss/193726/Simple-Golang-solution-beats-100
        
        if n < 2:
            return 0
        elif n >= 2 and n <= 5:
            return n
        else:
            for i in range(n//2, 1, -1):
                if n%i == 0:
                    return (n//i) + self.minSteps(i)
        return n
    
        """
        # or
        import math
        if n == 1:
            return 0
        else:
            for i in range(int(math.sqrt(n)), 1, -1):
                if n%i == 0:
                    return self.minSteps(i) + self.minSteps(n//i)
            return n
        """
        
        """
        # Literally following the problem and working around that doesnt help
        # * The challenge remains on deciding when to perform the copy again
        # * The is more of a mathematical solution, to understand the properties of the proble,
        # 
        notepad = "A"
        copied = ""
        steps = 0
        #total = n-1
        # remember it is exactly `n` number you have to reach...
        
        while len(notepad) < n:
            print notepad, copied, steps
            # Copy All Operation
            if not copied:
                copied = notepad
            # Copy operation decision 
            elif n%len(notepad) == 0:
                copied = notepad
            # Paste the data 
            else:
                notepad += copied
            steps += 1
        
        return steps
        """
            
            
        
