class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # Dictionary Method of solving
        height = {}
        
        # Result array
        result = []
        
        # Set height as the key for dictionary to collect duplicate height entries and their positions
        for queue in people:
            if queue[0] not in height:
                height[queue[0]] = []
            height[queue[0]].append(queue[1])
        
        # Sort height in descending order and sort each values for keys and append to the result
        for pos in sorted(height.keys())[::-1]:
            height[pos].sort()
            for p in height[pos]:
                result.insert(p, [pos,p])
        return result
            
            
