# Travel Between Cities
"""
You need to travel between cities, but some roads may have been blocked by a recent storm. 
You want to check before you travel to make sure you avoid them. 
Given a map of the cities and their bidirectional roads, determine which roads are along any shortest path so you can check that they are not blocked. 
The roads or edges are named using their 1-based index within the input arrays.
For example, given a map of g_nodes = 5 nodes, the starting nodes, ending nodes and road lengths are:
Road from/to/weight
1 (1, 2, 1)
2 (2, 3, 1)
3 (3, 4, 1)
4 (4, 5, 1)
5 (5, 1, 3)
6 (1, 3, 2)
7 (5, 3, 1)
You always need to go from node 1 to node g_nodes, so from node 1 to node 5 in this case.
The shortest path is 3, and there are three paths of that length: 1 → 5, 1 → 2 → 3 → 5, and 1 → 3 → 5.
We create an array of strings, one for each road in order, where the value is YES if a road is along a shortest path or NO if it is not. 
In this case, the resulting array is [YES, YES, NO, NO, YES, YES, YES].
Function Description
Complete the function classifyEdges in the editor below. 
The function must return an array of g_edges strings where the value at ith index is YES if the ith edge is a part of a shortest path from vertex 1 to vertex g_nodes. 
Otherwise it should contain NO.
classifyEdges has the following parameter(s):
g_nodes: an integer, the number of nodes
g_from[g_from[1],...g_from[g_nodes]]: an array of integers, the start g_nodes for each road
g_to[to[1],...g_to[g_nodes]]: an array of integers, the end g_nodes for each road
g_weight[g_weight[1],...g_weight[g_nodes]]: an array of integers, the lengths of each road
Constraints
2 ≤ g_nodes ≤ 3000
1 ≤ g_edges ≤ min(105, (g_nodes x g_nodes - 1)/2)
1 ≤ g_weight[i] ≤ 105
1 ≤ g_from[i], g_to[i] ≤ g_nodes
There is at most one edge between any pair of g_nodes
The given graph is connected
Sample Input 1
4 5
1 2 1
2 4 1
1 3 1
3 4 2
1 4 2
Sample Output 1
YES
YES
NO
NO
YES

Sample Input 2

5 7
1 2 1
2 3 1
3 5 1
1 4 1
4 5 2
3 4 2
2 4 4

Sample Output 2
YES
YES
YES
YES
YES
NO
NO

Sample Input 3
4 5
1 2 1
1 3 1
1 4 1
2 3 1
2 4 1

Sample Output 3

NO
NO
YES
NO
NO
"""

# Logic 1: We will do using graphs to track the paths 
# - Build them using a dictionary/hashmap datastructure
# - Bidirectional route - take that into consideration, consider infinite loops when cities route are completed by a circle
# - Using traceback logic

def get_paths(src, target, weight, path, paths, visited, graph):
    # Reached the target, then append to paths
    if src == target:
        if weight not in paths:
            paths[weight] = []
        paths[weight].append(path)
    else:
        # Iterate all possible destinations until we reach the target
        for dst in graph[src].keys():
            if dst not in visited: # Bidirectional check - we do not want to visit already visited node... avoid infinite loop
              get_paths(dst, target, weight+graph[src][dst], path+[(src, dst)], paths, visited+[dst], graph)
    return

def shortest_path(s, d, paths):

    # Build graph with a dictionary
    graph = {}

    # Iterate paths to fill in the dictionary
    for path in paths:
        # For simplicity, call out explicitly
        src = path[0]
        dst = path[1]
        weight = path[2]

        # add the SOURCE city in the graph
        if src not in graph:
            graph[src] = {}
        if dst not in graph:
            graph[dst] = {}
        
        # add the DESTINATION city to the source - if duplicate choose minimum for shortest
        if dst not in graph[src]:
          graph[src][dst] = weight
        else:
          graph[src][dst] = min(graph[src][dst], weight)
        if src not in graph[dst]:
            graph[dst][src] = weight
        else:
            graph[dst][src] = min(graph[dst][src], weight)
        
    #print(graph)
    s_paths = {}
    # for s in graph.keys(): # Need iteration to start from any nodes, but we need to start from 1 in this case
    get_paths(1, d, 0, [], s_paths, [1], graph) # src, target, weight, path, paths, graph
    #print(s_paths)
    s = []
    for dir in s_paths[min(s_paths.keys())]:
        s.extend(dir)
    return s

def solution(node, map):
    shortest = shortest_path(1, g_nodes, map)
    print(shortest)
    result = ["NO"]*len(map)
    for m in range(len(map)):
        s = map[m][0]
        d = map[m][1]
        if (s,d) in shortest or (d,s) in shortest:
            result[m] = "YES"
    print(result)

# TC1
g_nodes = 5
map = [(1, 2, 1), (2, 3, 1), (3, 4, 1), (4, 5, 1), (5, 1, 3), (1, 3, 2), (5, 3, 1)]
solution(g_nodes, map)

# TC2
g_nodes = 4
map = [(1, 2, 1), (2, 4, 1), (1, 3, 1), (3, 4, 2), (1, 4, 2)]
solution(g_nodes, map)

# TC3
g_nodes = 5
map = [(1, 2, 1), (2, 3, 1), (3, 5, 1), (1, 4, 1), (4, 5, 2), (3, 4, 2), (2, 4, 4)]
solution(g_nodes, map)

# TC4
g_nodes = 4
map = [(1, 2, 1), (1, 3, 1), (1, 4, 1), (2, 3, 1), (2, 4, 1)]
solution(g_nodes, map)