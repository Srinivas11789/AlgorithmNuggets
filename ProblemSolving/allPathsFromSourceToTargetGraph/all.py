class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # Given
        # * Index is the node
        # * graph[Index] is the next nodes of the index node
        
        # There are 2 method for a graph (like in a tree), 
        # * DFS - Depth ==> recursive strategy
        # * BFS - Breath ==> Iterative strategy
        
        # Common setting
        # Num of nodes (as each i is a node)
        n = len(graph)
        
        # Method 1 - 100 pass 100% faster
        
        # DFS - Recusive method, a method defined for recursing
        
        def traverse_graph(path):
            
            # As we progress with path, the last node in path is the latest node: path[-1]
            
            # When n-1 or last node is reached, add the path to result
            if path[-1] == n-1:
                result.append(path)
            
            # For each next node, add next_node to path and recurse.
            for next_node in graph[path[-1]]:
                traverse_graph(path+[next_node])
                
        # Method 2 - 100 pass, 50% faster
        # BFS - Iterative method, a method with a reference list (stack) defined for iteration
        
        def traverse_graph2():
            
            # Reference stack with known first node
            stack = [[0]]
            
            # When stack is empty all nodes are traversed
            while stack:
                # Current path from stack, current node should be the lastest in the last of path
                current_path = stack.pop(0)
                current_node = current_path[-1] # Latest Node in the path
                
                # Once, final node is reached append path
                if current_node == n-1:
                    result.append(current_path)
                    
                # Add next nodes in path and into the stack
                if graph[current_node]:
                    for next_node in graph[current_node]:
                        stack.append(current_path+[next_node])
        
        result = []
        traverse_graph([0])
        #traverse_graph2()
        return result
