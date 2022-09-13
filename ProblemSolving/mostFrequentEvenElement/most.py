class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        
        import collections
        c = collections.Counter(nums)
        
        maxi = 0
        mink = float('inf')
        
        for k,v in c.items():
            if k%2 == 0 and v >= maxi:
                if v == maxi and k < mink:
                    mink = k
                if v > maxi:
                    mink = k
                    maxi = v
    
        if mink == float('inf'):
            return -1
        
        return mink
