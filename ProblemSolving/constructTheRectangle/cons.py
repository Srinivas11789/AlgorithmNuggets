class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        
        
        # Division logic - Eventually 100 pass as square root was used - Initially Passed still time limit exceeded at 9999994 - Optimized but this is still going through all possible pairs from the beginning
        # Rule 1 and Rule 2 are easily satisfied
        # Rule 3 --> Finding minimum is optimal only when we go backwards, as l and w together should be a greater value for the difference to be very less, <starting from 0 or 1 would cause large differences which would not be an optimal solution like (1,4)>
        # Using square root works and 100 pass
        import math
        result = []
        mini = float('inf')
        #for i in range(1,area//2+2):
        for i in range(1,int(math.sqrt(area))+1):
            # Rule 1
            if area%i == 0:
                # Rule 2
                l = i
                w = area//l
                if w > l:
                    l,w = w,l
                # Rule 3
                if l-w < mini:
                    mini = l-w
                    result.append([l,w])
        #print result
        return result[-1]
        
        
        """
        # 100 pass
        # Based on the logic of the Rule 3 being easily satisfied by going from the square root of the number
        # Smaller logic from discussions
        import math
        i = int(math.sqrt(area))
        while area%i != 0:
                i -= 1
        return [area//i,i]
        """
        
        """
        # Brute force solution - Passed but Time Limit Exceeded
        import itertools
        lWs = [i for i in range(1,area)]
        result = []
        mini = float('inf')
        for perm in itertools.product(lWs, repeat=2):
            # Rule 1
            if perm[0]*perm[1] == area:
                # Rule 2
                if perm[0] >= perm[1]:
                    # Rule 3
                    if perm[0] - perm[1] < mini:
                        mini = perm[0] - perm[1]
                        result.append(perm)
        print result, lWs
        return result[-1]
        """
        
