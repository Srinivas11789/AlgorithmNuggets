class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxi = 0
        n = len(nums)
        if n == 0:
            return maxi
        elif n == 1:
            return 1
        curr_subseq = [nums[0]]
        prev = nums[0]
        for i in range(1,n):
            if nums[i] > prev:
                curr_subseq.append(nums[i])
                if i == n-1 and len(curr_subseq)>maxi:
                    return len(curr_subseq)
            else:
                if len(curr_subseq)>maxi:
                    maxi = len(curr_subseq)
                curr_subseq = [nums[i]]
            prev = nums[i]
            
        return maxi
