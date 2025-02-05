# Topo Sort
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    
        graph = {}
        ingress = {}
        for i in range(len(prerequisites)):
            end = prerequisites[i][0]
            start = prerequisites[i][1]
            
            if start not in graph:
                graph[start] = []
            graph[start].append(end)

            if end not in graph:
                graph[end] = []

            if start not in ingress:
                ingress[start] = 0
            if end not in ingress:
                ingress[end] = 0
            ingress[end] += 1

        process_queue = []
        for i, val in ingress.items():
            if val == 0:
                process_queue.append((i, val))

        order = []
        while process_queue:
            curri, currv = process_queue[0]
            if len(process_queue) > 1:
                process_queue = process_queue[1:]
            else:
                process_queue = []
            
            if currv == 0:
                order.append(curri)
            
            for nxt in graph[curri]:
                ingress[nxt] -= 1
                if ingress[nxt] == 0:
                    process_queue.append((nxt, 0))

            if len(order) > len(graph):
                return False

        if len(order) == len(graph):
            return True

        return False
