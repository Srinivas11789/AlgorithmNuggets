class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        uniq_sum = 0
        freqs = {}
        for i in range(len(nums)):
            if nums[i] not in freqs:
                freqs[nums[i]] = 0
            freqs[nums[i]] += 1
        for k,v in freqs.items():
            if v == 1:
                uniq_sum += k
        return uniq_sum
                
