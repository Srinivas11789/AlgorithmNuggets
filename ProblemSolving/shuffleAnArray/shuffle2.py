import random
class Solution:

    def __init__(self, nums: List[int]):
        self.n = nums[:]
        self.comb = nums[:]

    def reset(self) -> List[int]:
        return self.n

    def shuffle(self) -> List[int]:
        i = random.randint(0, len(self.n)-1)
        j = random.randint(0, len(self.n)-1)
        self.comb[i], self.comb[j] = self.comb[j], self.comb[i]
        return self.comb


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
