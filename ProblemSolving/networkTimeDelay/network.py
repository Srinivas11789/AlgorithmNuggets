class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        
        # Create a relation of all the nodes, like a dictionary
        relation = {}
        for time in times:
            if time[0] not in relation:
                relation[time[0]] = {}
                relation[time[0]][time[0]] = 0
                
            # Source Node = Destination Node = Time
            relation[time[0]][time[1]] = time[2]
            
        """
        # Logic to construct complete relationship from each node to all nodes (incomplete)
        # we dont need this in this problem as we are already given the source node K
        for key in relation.keys():
            temp = relation[key][:]
            for key1 in temp:
                if key1 in relation:
                    for key2 in relation[key1]:
                        relation[key][key2] = relation[key1][key2]
        """
            
        #print relation
        
        # For "k" destination try to navigate through all nodes
        distances = [0]*N
        for i in range(1,N+1):
            # Direct distance from K
            if K in relation and i in relation[K].keys():
                distances[i-1] = relation[K][i]
            else:
                if K in relation:
                    for key in relation[K].keys():
                        if key in relation:
                            if i in relation[key]:
                                distances[i-1] = relation[key][i] + distances[key-1]

        if max(distances) == 0:
            return -1
        
        print distances
        return max(distances)
            
            
            
        
