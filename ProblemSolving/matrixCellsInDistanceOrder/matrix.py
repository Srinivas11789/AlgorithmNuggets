class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        
        # Logic 1: Using sorted method with custom key for the matrix - O(N) + O(NlogN) - 58%faster
        """
        def distance(x):
            return abs(r0-x[0])+abs(c0-x[1])
        
        matrix = []
        for i in range(0, R):
            for j in range(0, C):
                #print(distance([i,j]))
                matrix.append([i,j])
        return sorted(matrix, key=lambda x: distance(x))
        """
        
        # Logic 2: Re arrange with distance calculation - O(N)? --> Use some property of the matrix
        
        
        # Logic 3: Using datastructures - 152ms - 58%faster
        def distance(x):
            return abs(r0-x[0])+abs(c0-x[1])
        
        distanc = set()
        dist = {}
        
        for i in range(0, R):
            for j in range(0, C):
                d = distance([i,j])
                if d not in dist:
                    dist[d] = []
                dist[d].append([i,j])
                distanc.add(d)
        result = []
        for d in distanc:
            result.extend(dist[d])
        return result
        
        
