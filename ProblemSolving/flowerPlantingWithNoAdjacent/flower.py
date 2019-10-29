class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        
        graph = {}
        
        if not paths:
            return [1]*N
        
        for gard in paths:
            if gard[0] not in graph:
                graph[gard[0]] = [gard[1]]
            else:
                graph[gard[0]].append(gard[1])
            if gard[1] not in graph:
                graph[gard[1]] = [gard[0]]
            else:
                graph[gard[1]].append(gard[0])
         
        flowers = [1 for i in range(N+1)]

        #print(graph)
        for i in graph.keys():
            fls = []
            for v in graph[i]:
                fls.append(flowers[v])
            #print(i, fls)
            for c in range(1, 5):
                if c not in fls:
                    flowers[i] = c
                    break
            #print(flowers)
        
        return flowers[1:]
            
