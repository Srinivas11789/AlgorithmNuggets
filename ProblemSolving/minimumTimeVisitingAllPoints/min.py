class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        
        # Logic 2: 67% faster
        # By math distance formula d^2 = (x2-x2)^2 + (y2-y1)^2
        # Kind of digesting this, we would know x2-x1 and y2-y1 is x, y distances.
        # always choose diagnal to go twice and then resort to hor, ver
        seconds = 0
        current = points[0]
        nxt = 1
        while nxt < len(points):
            seconds += max(abs(points[nxt][0]-current[0]), abs(points[nxt][1]-current[1]))
            current = points[nxt]
            nxt += 1
        return seconds
    
        """
        # Logic 1: Literally moving through points
        seconds = 0
        current = points[0]
        nxt = 1
        # all 1s operations
        # * (0, +/- 1)
        # * (+/- 1, 0)
        # * (+/- 1, +/- 1)
        while nxt < len(points):
            while current != points[nxt]:
                # go diagnal first
                if current[0]+1 < points[nxt][0] and current[1]+1 < points[nxt][1]:
                    current[0] += 1
                    current[1] += 1
                    seconds += 1
                else if current[0]+1 < points[nxt][0]
            nxt += 1
        """
            
            
