class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        # A DP Problem but brute force works - 100 pass
        # Brute force - Memory Limit Exceeded - Remove the list store for results and only count the matches of the result
        
        #result = []
        count = 0
        n = len(s)
        for i in range(n):
            #result.append(s[i])
            if s[i:] == s[i:][::-1]:
                #result.append(s[i:])
                count += 1
            for j in range(i+1,n):
                sub = s[i:j]
                if sub == sub[::-1]:
                    #result.append(sub)
                    count += 1
        #print result
        #return len(result)
        return count
    
    
        # 
        # DP Solution
                
