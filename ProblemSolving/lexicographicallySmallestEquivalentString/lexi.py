class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        def getAllEqui(c, graph, visited):
            for nxt in graph[c]:
                if nxt in visited:
                    continue
                visited.add(nxt)
                getAllEqui(nxt, graph, visited)
            return visited

        graph = {}

        if len(s1) != len(s2):
            return baseStr

        for i in range(len(s1)):
            if s1[i] not in graph:
                graph[s1[i]] = {s1[i]}
            if s2[i] not in graph:
                graph[s2[i]] = {s2[i]}
            graph[s1[i]].add(s2[i])
            graph[s2[i]].add(s1[i])

        equiLex = ""
        for i in range(len(baseStr)):
            if baseStr[i] not in graph:
                equiLex += baseStr[i]
                continue
            visited = set()
            getAllEqui(baseStr[i], graph, visited)
            equiLex += sorted(visited)[0]
            print(baseStr[i], visited, equiLex)
        
        return equiLex
