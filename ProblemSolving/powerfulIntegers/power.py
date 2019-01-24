class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        
        # Logic 1: Brute force with 2 for loops O(N**2)
        
        result = []
        
        # Iterate all i and j values
        for i in range(0,bound):
            for j in range(0, bound):
                
                # Calculate powerful integer
                powerful = x**i + y**j
                
                # Debug
                #print powerful,i, j
                
                # Result append only when result < bound, else break and increment i
                if powerful <= bound:
                    result.append(powerful)
                else:
                    break
                    
            # When power of i itself causes to exceed bound stop.
            if j == 0 and powerful > bound:
                break
            
        return list(set(result))
