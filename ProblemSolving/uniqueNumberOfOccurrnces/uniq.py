class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        # Logic 1: Exhaustive use of libraries - 64% faster
        """
        import collections
        counts = collections.Counter(arr)
        if sorted(counts.values()) == sorted(set(counts.values())):
            return True
        else:
            return False
        """
        
        # Logic 2: Another way of using collections - 85% faster
        """
        import collections
        unique = list(set(collections.Counter(collections.Counter(arr).values()).values()))
        return unique[0] == 1 and len(unique) == 1
        """
        
        # Logic 3: O(N) Iteration with data structure - 95% faster
        # DS
        freq = {}
        # Iterate and populate DS
        for i in range(len(arr)):
            if arr[i] not in freq:
                freq[arr[i]] = 0
            freq[arr[i]] += 1
        # If no repeated then return true
        if len(freq.values()) == len(set(freq.values())) and min(freq.values()) == 1:
            return True
        else:
            return False
        
