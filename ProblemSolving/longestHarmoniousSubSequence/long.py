class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Make a dictionary to track the frequency of the characters
        import collections
        db = collections.Counter(nums)
        
	# Maximum to be zero
        maxi = 0
        
	# Iterate through the DB to check for difference of +1 or -1 and add their frequencies to check for maximum
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
        
        
        
