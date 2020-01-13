class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        
        # Logic 1: Naive 2 iteration for 2 array pick - Time Limit Exceeded!
        """
        maxi = -float('inf')
        for i in range(len(arrays)):
            for j in range(i+1, len(arrays)):
                #print(arrays[i], arrays[j])
                if abs(arrays[j][-1] - arrays[i][0]) > maxi:
                    maxi = abs(arrays[j][-1] - arrays[i][0])
                if abs(arrays[j][0] - arrays[i][-1]) > maxi:
                    maxi = abs(arrays[j][0] - arrays[i][-1])
        return maxi
        """
        
        # Logic 2: Take the first and the last and find maxi as we iterate - 64% faster - 100 pass
        first = arrays[0][0]
        last = arrays[0][-1]
        maxi = -float('inf')
        for i in range(1, len(arrays)):
            maxi = max(maxi, abs(first-arrays[i][0]), abs(first-arrays[i][-1]))
            maxi = max(maxi, abs(last-arrays[i][0]), abs(last-arrays[i][-1]))
            if arrays[i][0] < first:
                first = arrays[i][0]
            if arrays[i][-1] > last:
                last = arrays[i][-1]
        return maxi
                
