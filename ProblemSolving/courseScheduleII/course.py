class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        
        # Iterative method
        
        # Null prereq
        if not prerequisites:
            return range(numCourses)
        
        # 1. Initialize a graph with schema graph[prereq], graph[dependency]
        graph = {}
        
        # 2. Build dictionary:graph of relationships
        for prereq in prerequisites:
            course = prereq[1]
            req = prereq[0]
            # Update prereq
            if course not in graph:
                graph[course] = {"dependent":[], "dependency": 0}
            graph[course]["dependent"].append(req)
            # Update dependency
            if req not in graph:
                graph[req] = {"dependent":[], "dependency":0}
            graph[req]["dependency"] += 1
        
        # 3. Get all the non depedent nodes
        dependency_satisfied_nodes = []
        for node in range(numCourses):
            if node not in graph:
                graph[node] = {"dependent":[], "dependency":0}
                dependency_satisfied_nodes.append(node)
            elif graph[node]["dependency"] == 0:
                dependency_satisfied_nodes.append(node)
                
        print graph, dependency_satisfied_nodes
                
        # 4. Iterate to satisfy and add all nodes
        for node in dependency_satisfied_nodes:
            for req in graph[node]["dependent"]:
                graph[req]["dependency"] -= 1
                if graph[req]["dependency"] == 0:
                    dependency_satisfied_nodes.append(req)
        
        print(dependency_satisfied_nodes)
        if len(dependency_satisfied_nodes) == numCourses:
            return dependency_satisfied_nodes
        else:
            return []
                    
