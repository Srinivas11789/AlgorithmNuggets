class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        # Logic1: 2*O(n) iteration to cover equal cases first and then non-equal ones
        
        equal = "=="
        inequal = "!="
        
        graph = {}
        
        def travG(curr, target, visited):
            if curr == target:
                return True
            
            found = False
            if curr not in visited:
                for nxt in graph[curr]:
                    found = found or travG(nxt, target, visited|set(curr))
                    
            return found
        
        for i in range(len(equations)):
            curr = equations[i]
            
            op = curr.split(equal)
            
            if len(op) > 1:
                if op[0] not in graph:
                    graph[op[0]] = []
                if op[1] not in graph:
                    graph[op[1]] = []
                graph[op[0]].append(op[1])
                graph[op[1]].append(op[0])
        
        print(graph)
            
        for i in range(len(equations)):
            curr = equations[i]
            
            op = curr.split(inequal)
            
            if len(op) > 1:
                if op[0] not in graph:
                    graph[op[0]] = []
                if op[1] not in graph:
                    graph[op[1]] = []
                if travG(op[0], op[1], set()):
                    return False
            
        return True
