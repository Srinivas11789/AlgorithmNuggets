class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
        # 100 pass - 76ms 42.78% faster 
        # Using extra variable to count, simpler logic
        # To maximize satisfaction, lets particularly sort the arrays 
        
        # Sort the arrays so they are both in increasing order
        g.sort()
        s.sort()
        
        # Initial point to start
        child, cookie = 0, 0
        
        # result
        content = 0
        
        # Iterate through both the arrays
        while child < len(g) and cookie < len(s):
            # Found a content child
            if s[cookie] >= g[child]:
                content += 1
                child += 1
                cookie += 1
            else:
                # Iterate cookie until a content cookie is found for respective child
                cookie += 1
                
        return content
        
        
        """
        # 100 pass - 176 ms 11.55% faster
        # Logic of deleting entries from list (Kinda like stacks), trying without using extra variable or result list
        # Use children + cookie list as a stack
        # * Pop child from chidren when their greed cannot be satisfied
        # * Pop cookie from cookies when they are given to children
        
        g.sort()
        s.sort()
        
        i, j = 0, 0
        while i < len(g):
            while j < len(s) and s[j] < g[i]:
                j += 1
            if j == len(s):
                g.pop(i)
            else:
                s.pop(j)
                i += 1
        return len(g)
        """
        
        
                
            
            
