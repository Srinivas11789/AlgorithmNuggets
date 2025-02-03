class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        def findLongest(narr: List[int], reverse: bool) -> int:
            longest = 1
            result = 1
            for i in range(len(nums)-1):
                if not reverse and nums[i] < nums[i+1]:
                    longest += 1
                    result = max(result, longest)
                elif reverse and nums[i] > nums[i+1]:
                    longest += 1
                    result = max(result, longest)
                else:
                    longest = 1
            return result     
        
        return max(findLongest(nums, True), findLongest(nums, False))
