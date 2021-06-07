class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Logic 1: 
        # * if there is an edge, add the respective nodes to a separate group as a key in dictionary
        """
        connected_groups = {0:set(edges[0])}
        g = 1
        for edge in edges:
            for group in list(connected_groups.keys()):
                if edge[0] in connected_groups[group]:
                    connected_groups[group].add(edge[0])
                    connected_groups[group].add(edge[1])
                elif edge[1] in connected_groups[group]:
                    connected_groups[group].add(edge[1])
                    connected_groups[group].add(edge[0])
                else:
                    connected_groups[g] = set()
                    connected_groups[g].add(edge[1])
                    connected_groups[g].add(edge[0])
                    g += 1
                print(connected_groups)
        return len(connected_groups.keys())
        """
        
        # Logic 2: proper dfs
        
        graph = [[] for i in range(n)]
        visited = [False for i in range(n)]
        connected = 0
        
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        def dfs(node):
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
        
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                connected += 1
                dfs(i)
        
        return connected
