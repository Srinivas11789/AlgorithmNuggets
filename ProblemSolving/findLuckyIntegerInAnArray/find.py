class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        # Logic 1: Dictionary + max tracking - 100 pass 84% faster
        import collections
        count = collections.Counter(arr)
        result = -1
        for k, v in count.items():
            if v == k and k > result:
                result = k
        return result
