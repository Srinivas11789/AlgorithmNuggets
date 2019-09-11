class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
 
         
        n = len(distance)
        s = min(start, destination)
        d = max(start, destination)
        distance += distance

        clockwise = sum(distance[s:d])
        anticlockwise = sum(distance[d:n+s])

        print(distance[s:d], distance[d:n+s])
        return min(clockwise, anticlockwise)
        
        
