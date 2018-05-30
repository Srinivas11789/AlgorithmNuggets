class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        # Math Magic Logic
        m = 1
        count = 0
        
        while N >= (m*(m+1)//2):
            
            if m%2 == 1:
                if N%m == 0:
                    #print m
                    count += 1
            elif N%m == m//2:
                #print m
                count += 1
            
            m += 1
        return count
        
        """
        # Logic: that failed with timeout
        # 1. With subArray list of possible sum(sub) == target
        # 2. With left, right pointer to traverse the array + memoize the subArray sum as we traverse through
        # 3. Brute force method
        # Counting the target number as well
        count = 1
        
        # Using an array
        sub = []
        
        i = 1
        sumi = 0
        
        while i <= N:
            #print i, sub, sumi
            if sumi < N:
                sumi += i
                sub.append(i)
                i += 1
            elif sumi > N:
                sumi -= sub[0]
                sub.pop(0)
            elif sumi == N:
                count += 1
                sumi -= sub[0]
                sub.pop(0)
        
        return count
        """
            
