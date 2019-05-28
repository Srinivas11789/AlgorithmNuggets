class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        # Logic 2
        # Looks hacky, I was thinking of just diff the sorted(array) vs array
        
        s_heights = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != s_heights[i]:
                count += 1
        return count
        
        """
        # Logic 1
        # As we iterate through the array
        # * Record all the irregularities and append to a list
        n = len(heights)
        students = []
        i = 0
        while i < len(heights):
            if (i+1 < len(heights) and heights[i+1] < heights[i]) or (i-1 >= 0 and heights[i-1] > heights[i]):
                students.append(heights[i])
                heights.pop(i)
            i += 1
        return len(students)
        """
        
