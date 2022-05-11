class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        # Logic 1: Backtrack recursively to construct string --> 9506 ms, faster than 5.08% of Python3 --> 100 pass
        self.vowels = ["a", "e", "i", "o", "u"]
        self.strings = []
        self.nums = 0
        
        def backtrack(current, remaining):
            #print(current)
            
            if remaining == 0:
                self.strings.append(current)
                self.nums += 1
                return
            
            for v in self.vowels:
                if current and v < current[-1]:
                    continue
                backtrack(current + v, remaining-1)
            return
        
        backtrack("", n)
        #print(self.strings)
        
        return self.nums
        
        # Logic 2: Mathematical combination formula [k+n-1]!//(k-1)!n!
        """
        # general combination: 2 --> _ _ --> [a,e,i,o,u] --> 5*5 --> 25 
        # lexi combination: 2 --> 
        # a = 1 x 5 
        # e = 1 x 4 
        # i = 1 x 3
        # o = 1 x 2
        # u = 1 x 1
        # ==> 15
        return (n+4)*(n+3)*(n+2)*(n+1)//24
        """
