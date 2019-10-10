class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Logic 1: Brute force: Worst case O(N2) ==> get the current sum + check all the sum of subarray before it
        """
        maxi = nums[0]
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
            maxi = max(maxi, nums[i])
            for j in range(0, i):
                maxi = max(maxi, nums[i]-nums[j])
        maxi = max(maxi, nums[-1])
        return maxi
        """
        
        # Logic 2: DP Like --> Calculate the Sum of the subarray including the current element
        # * If adding the sum would help maximum then add it else 0
        # * We want the sum to be max, so get the sum of the contiguous subarray from the previous value as we calculate and only when it is above 0 use it as it helps maximum else stop.
        """
        ans = nums[0]
        for i in range(1, len(nums)):
            nums[i] = nums[i]  + (nums[i-1] if nums[i-1] > 0 else 0)
            ans = max(ans, nums[i])
        return ans
        """
        
        # Logic 3: Referring to https://leetcode.com/problems/maximum-subarray/discuss/20211/Accepted-O(n)-solution-in-java a math property
        
        maxHere = nums[0]
        maxUntilNow = nums[0]
        for i in range(1, len(nums)):
            maxHere = max(nums[i], nums[i]+maxHere)
            maxUntilNow = max(maxUntilNow, maxHere)
        return maxUntilNow
