# Logic 0:  Naive iteration: O(1) space in-place updates with o(n) time
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # Naive iteration: O(1) space in-place updates with o(n) time
        last_sum = 0
        for i in range(len(nums)):
            nums[i] = last_sum + nums[i]
            last_sum = nums[i]
        return nums

# Logic 1: O(N) iteration in finding sum and save with separate O(N) array - 92% faster
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current_sum = 0
        run_sum = []
        for i in nums:
            current_sum += i
            run_sum.append(current_sum)
        return run_sum

# Logic 2: Itertools way
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        from itertools import accumulate
        return accumulate(nums)
