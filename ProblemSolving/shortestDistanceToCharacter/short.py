class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        
        # Iteration 2 ways ==> 2 way traversal -- from 1->n and from n->1
        
        # Initial variables
        n = len(S)
        
        # Initialize the array with n which is the maximum for an array so that we can check minimum as we traverse the array
        result = [n]*n
        
        hit = None
        
        # Based on one good implementation from the discussion by lee215, loop can also be made like for i in range(n)+range(n)[::-1] to loop twice, which might represent a smaller version
        for i in range(n):
            
            if S[i] == C:
                hit = i
            if hit != None: # Caution: if hit: will be true for both None as well as 0
                result[i] = min(result[i], abs(hit-i))
        
        for i in range(n)[::-1]:
            
            if S[i] == C:
                hit = i
            if hit != None: # Caution: if hit: will be true for both None as well as 0
                result[i] = min(result[i], abs(hit-i))
            
        return result
        
        """
        # Almost there, some edge case fails...
        # Logic 3: O(N) traversal of the array - left and right pointers to contains C char locations
        
        # Initial variables
        n = len(S)
        result = []
        left = right = None
        # Looping through N
        for i in range(n):
            
            if S[i] == C:
                # Setting left and the right pointers 
                if S[i] == C and left == None:
                    left = i
                elif S[i] == C and right == None:
                    right = i
                elif left and right:
                    left = i
                    #right = None
                    if left > right:
                        left, right = right, left
                
                # Perform distance calculation
                #if left:
                #    result.extend([j for j in range(left, -1, -1)])
                print left, right
                if left < right and left and right:
                    result.extend([min(j-left, right-j) for j in range(left+1,right+1)])
                elif left and not right:
                    result.extend([j for j in range(left, -1, -1)])
            if i == n-1 and len(result) < n:
                result.extend([j-left for j in range(left+1,n)])
            
        return result      
        """   
        
        """
        # Logic2: Split the string with respect to e and perform operation on top of it
        S = S.split(C)
        result = []
        for item in S:
            n = len(item)
            result.extend([i for i in range(n)][::-1])
        """
        
        """
        # Logic 1
        # Brute force - use 2 for loops for each character to find C - Not working properly but trying other logic
        n = len(S)
        result = []
        for i in range(n):
            for j in range(i,n):
                if S[j] == C:
                    v1 = j-i
                if S[-j-1] == C:
                    v2 = i-j
                if v1 and v2:
                    result.append(min(v1,v2))
                    break
        return result
        """
                
        
