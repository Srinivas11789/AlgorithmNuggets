class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        # Logic 1: Naive Iteration O(N) - exit on first match of more than 25% - 100 pass 97% faster
        """
        n = len(arr)
        visited = None
        count = 0
        for i in range(n):
            if visited != None and arr[i] == visited:
                count += 1
            else:
                visited = arr[i]
                count = 1
            if count > n//4:
                return visited
        return -1
        """
        
        # Logic 2: Dictionary count method
        import collections
        counts = collections.Counter(arr)
        n25 = len(arr)//4
        for k, v in counts.items():
            if v > n25:
                return k
        return -1
