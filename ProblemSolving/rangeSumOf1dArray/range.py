class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [0 for i in range(len(nums))]
        for n in range(len(nums)):
            num = nums[n]
            output[n] = output[n-1]+num
        return output
