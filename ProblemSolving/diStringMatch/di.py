class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        
        # Analysis
        """
        -------------> Idea 1:
        IDID ==> [0,1,2,3,4]
        1) [0,2,1,3,4] then it proceeds...
        I --> do not change anything
        D --> Apply a swap for the current index to the maximum.
        * Every D is (ith+1) element
        * If D comes at start replace the maximum num, keep track of I as we move on the array
        """
        
        # Two Pointer Method
        left = 0
        right = len(S)
        
        result = []
        
        for i in range(right):
            
            if S[i] == "I":
                result.append(left)
                left += 1
            else:
                result.append(right)
                right -= 1
        
        return result + [left]
        
        
        
        """
        # Adding range(i) for every I and recoding D as we pass through
        # - Actually we do not need to keep track of result as it is always range(N)
        # 
        
        N = len(S)
        D = []
        
        #if S[0] == "D":
        #    S = S[::-1]
            
        result = []
        
        def mapping():
            if D:
                D.pop(len(S)-1)
       
        for i,x in enumerate(S):
            if x == "D":
                D.append(i+1)
                result.append("X")
            else:
                count = 0
                for i in range(i+1+1):
                    if (i not in D) and (i not in result):
                        count += 1
                        result.append(i)
                    if count == i+1:
                            break
                        
        #D = D[::-1]
        print result,D
        
        for i in range(len(result)):
            if result[i] == "X":
                result[i] = D.pop()
        
        return result
        """
                
        """
        # Iterating the array and operating might make a confusing logic
        D = []
        I = 0
        N = len(S)
        i = 0
        while i < N:
            if S[i] == I:
                I = i
                i += 1
            else:
                i += 1
                D.append(i)
        """
                
