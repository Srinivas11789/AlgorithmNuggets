## 100 pass

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        import collections
        c = collections.Counter(nums)
        result = []
        most = sorted(c.values())[::-1][:k]
        for key,value in c.items():
            if value in most:
                result.append(key)
        return result
        
