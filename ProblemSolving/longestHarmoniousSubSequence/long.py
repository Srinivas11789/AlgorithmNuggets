class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        db = collections.Counter(nums)
        
        maxi = 0
        
        for k,v in db.items():
            if k-1 in db:
                maxi = max(maxi, db[k-1]+db[k])
            elif k+1 in db:
                maxi = max(maxi, db[k+1]+db[k])
        return maxi
        
        
        """
        # Logic: Doesnt work for subsequence occuring in the middle of the array
        nums = sorted(nums)
        n = len(nums)
        print nums
        
        for i in range(n-1, -1, -1):
            current = nums[:i]
            if max(current) - min(current) == 1:
                print current
                return len(current)
        return -1
        """
        
        
        
