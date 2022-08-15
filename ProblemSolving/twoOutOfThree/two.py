class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        # Logic 1: using space to compute frequency across arrays: O(ABC) time + O(2N) space --> ~ 25% faster
        freqs = {}
        result = []
        added = set()
        
        def record(nums):
            visited = set()
            for i in nums:
                if i not in freqs:
                    freqs[i] = 1
                else:
                    if i in visited:
                        continue
                    freqs[i] += 1
                visited.add(i)
        
        record(nums1)
        record(nums2)
        record(nums3)
        
        result = []
        for k,v in freqs.items():
            if v >= 2:
                result.append(k)
                
        return result

