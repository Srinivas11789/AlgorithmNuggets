class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        start = 0
        result = []
        i = 0
        while i < len(nums):
            if nums[i]-nums[i-1] > 1:
                if start != i-1:
                    result.append(str(nums[start])+"->"+str(nums[i-1]))
                else:
                    result.append(str(nums[start]))
                start = i
            i += 1

        if nums:   
            if start != i-1:
                result.append(str(nums[start])+"->"+str(nums[i-1]))
            else:
                result.append(str(nums[start]))

        return result
