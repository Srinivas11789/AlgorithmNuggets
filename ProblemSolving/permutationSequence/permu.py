class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        # Logic:1 using itertools python (as usual itertools goes through huge iterations) - just 5% faster
        import itertools
        result = []
        
        # Iterate all permutation in range of n list [1,2,...n] for length 3
        for permutation in itertools.permutations(range(1,n+1), r=n):
            result.append(permutation)
        
        # Return kth permutation - convert int to string before join
        return "".join([str(i) for i in result[k-1]])
    
    

        
