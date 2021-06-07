# 100 pass
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        import collections
        maxi_uniq_val = -1
        counts = collections.Counter(A)
        for val, count in counts.items():
            if count == 1 and val > maxi_uniq_val:
                maxi_uniq_val = val
        return maxi_uniq_val
