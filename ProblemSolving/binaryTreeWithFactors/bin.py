class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:   
        
        # Ref: leetcode solution for help
        MOD = 10 ** 9 + 7
        
        refs = [1]*len(arr) # single index is one tree already
        
        arr.sort() # arrange so we can iterate for product/modulo computation
        
        prods = {}
        for i in range(len(arr)): 
            prods[arr[i]] = i # unique so no need to check existence
            
        for i in range(len(arr)):
            for j in range(i):
                if arr[i]%arr[j] == 0: # left is arr[j]
                    other = arr[i]//arr[j]
                    
                    if other in prods:
                        refs[i] += refs[j] * refs[prods[other]]
                        refs[i] %= MOD
        
        return sum(refs)%MOD
            
