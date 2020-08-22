# Logic 1: 100 pass 80% faster
# * Initialize dummy array elements
# * Add elements to index
# * shift when the index is already filled
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        result = [None]*n
        while i < n:
            if result[index[i]] == None:
                result[index[i]] = nums[i]
            else:
                result = result[:index[i]] + [nums[i]] + result[index[i]:]
            i += 1
        return result[:n]
