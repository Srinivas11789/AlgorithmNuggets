class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # Initialize a graph and visited array
        graph = [[] for x in xrange(numCourses)]
        visited_vertices = [0]*numCourses
        
        # Create a graph
        for pair in prerequisites:
            curr_course = pair[0]
            pre_req = pair[1]
            graph[curr_course].append(pre_req)
            visited_vertices[pre_req] += 1
        
        # Get all the root nodes or nodes with are starting/end point
        possible_start_end_nodes = [] 
        for node in range(numCourses):
            if visited_vertices[node] == 0:
                possible_start_end_nodes.append(node)
        
        # Iterate all possible start and end nodes
        for node in possible_start_end_nodes:
            for pre_req in graph[node]:
                visited_vertices[pre_req] -= 1
                if visited_vertices[pre_req] == 0:
                    possible_start_end_nodes.append(pre_req)
        print(possible_start_end_nodes, graph, visited_vertices)
        return len(possible_start_end_nodes) == numCourses  
        
        """
        # Initialize a graph and visited array
        graph = [[] for x in xrange(numCourses)]
        visited_vertices = [0]*numCourses
        
        
        # Recursively progress through the graph visiting all the nodes once
        def traverse_graph(node, path):
            # Recursively iterate the pre_req
            visited_vertices[node] = 1
            if node not in path:
                for pre_req in graph[node]:
                        if visited_vertices[pre_req] == 0:
                            traverse_graph(pre_req, path)
                            visited_vertices[pre_req] = 1
                path.append(node)
        
                
        if prerequisites == []:
            return True
        
        # Create a graph
        for pair in prerequisites:
            curr_course = pair[0]
            pre_req = pair[1]
            #print(graph, curr_course, pre_req)
            graph[curr_course].append(pre_req)
            visited_vertices[pre_req] += 1
        
        
        result = []
        max_path = 0
        for course in range(len(graph)):
            route = []
            traverse_graph(course, route)
            print(route, visited_vertices, course, result)
            if len(route) > max_path:
                max_path = len(route)
                result = [route]
            elif len(route) == max_path:
                if route[::-1] in result:
                    return False
                result.append(route)
        if result:
            return True
        return False
        """
        


