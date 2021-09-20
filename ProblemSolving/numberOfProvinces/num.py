class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        # Init vars
        visited = set()
        provinces = 0
        
        # Contruct a graph
        graph = {}
        for i in range(len(isConnected[0])):
            for j in range(len(isConnected)):
                if i not in graph:
                    graph[i] = []
                if isConnected[i][j] == 1 and i != j:
                    graph[i].append(j)

        # Traverse graph by not-yet-visited vertices to cover all edges
        for k, v in graph.items():
            if k in visited:
                continue
            stack = v
            # cover all edges
            for e in stack:
                if e not in visited:
                    visited.add(e)
                    if e in graph:
                        stack.extend(graph[e])
            provinces += 1       
        return provinces
