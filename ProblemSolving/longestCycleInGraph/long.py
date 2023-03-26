class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        self.longest = -1

        def dfs(curr, dist, edges, visited, distance):
            dist += 1 # inc dist every time
            visited[curr] = True # mark visited
            distance[curr] = dist # compute dist from start node
            neighbour = edges[curr]
            
            # neighbour checks

            if neighbour == -1: # no route check
                return
            if neighbour not in visited:  # not yet visited check
                dfs(neighbour, dist, edges, visited, distance)
                return
            if neighbour in distance: # already visited then there is a cycle detected
                self.longest = max(self.longest, distance[curr] - distance[neighbour] + 1)
                return

        visited = {} # visit only once is enough as there can be only one cycle per node and we are not aware where we start
        for i in range(len(edges)):
            distance = {} # distance from start node as we are not aware prior
            if i not in visited:
                dfs(i, 0, edges, visited, distance)

        return self.longest
