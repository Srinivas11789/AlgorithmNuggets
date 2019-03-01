class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        
        # Logic 2 - (Just Add/Sub) 100 pass 100 percent 
        # Dictionary to count all the trust
        # * Combining the 2 rule we conclude
        #   - being trusted, Count add 1
        #   - Trusting someoone, Count subtract 1
        # * The one remaining with value equal to N-1 wins
        trusted_by_n = [0]*(N+1)
        
        # Iterate through trust to add/sub the trust scale
        for t in trust:
            trusted_by_n[t[0]] -= 1
            trusted_by_n[t[1]] += 1
        
        # Null Trust list check
        if trust == [] and N==1:
            return N
        
        # One with value of trust equal to N-1 is the Judge
        if max(trusted_by_n) == N-1:
            return trusted_by_n.index(max(trusted_by_n))
        else:
            return -1
        
        # Logic 1
        # A dictionary to satisfy both the condition
        # For a town judge,
        # * number of trusters of a person should be N-1
        # * no trust for the one person 
        """
        trust_dictionary = {}
        
        for t in trust:
            if t[1] not in trust_dictionary:
                trust_dictionary[t[1]] = []
            trust_dictionary[t[1]].append(t[0])
        """
        
        
        
        
        
