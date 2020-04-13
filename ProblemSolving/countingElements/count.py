class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        import collections
        freq = collections.Counter(arr)
        counts = 0
        for k in freq.keys(): # Iterate over all elements
            if k+1 in freq: # If i+1 exists in array
                max_diff = freq[k]
                counts += max_diff # Increment count
                freq[k] -= max_diff # Update freq
        return counts
