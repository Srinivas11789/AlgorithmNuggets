class Node:
    def __init__(self, n, inform, mgr, children=[]):
        self.n = n
        self.inform = inform
        self.mgr = mgr
        self.children = children

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:            
            nodes = {} # map[n]*Node
            visitedMgrs = set()
            self.totalMins = 0
            root = None

            def computeTime(node, cumulTime):
                for c in node.children:
                    computeTime(c, cumulTime + node.inform)
                self.totalMins = max(self.totalMins, cumulTime)

            for i in range(n):
                mgr = manager[i]

                if mgr == -1:
                    root = i

                if i not in nodes:
                    nodes[i] = Node(i, informTime[i], mgr != 0, [])
                
                if mgr not in nodes:
                    nodes[mgr] = Node(mgr, informTime[mgr], True, [])
                
                nodes[mgr].children.append(nodes[i])

            computeTime(nodes[root], 0)

            return self.totalMins
