### Graph Theory Datastructure
# Helper: https://www.python-course.eu/graphs_python.php

# * Directed graph -> no reversible flow, the flow or edge remains in single direction
# * UnDirected graph -> reversible flow, the flow or edge in on both the direction


## Represent a Graph with list and dictionary

# Undirected 
graph1 = {
    "node1": ["node2", "node4"],
    "node2": ["node1", "node3"],
    "node3": ["node2"],
    "node4": ["node1"]
}

# If nodes are index of a list then we can use list representation
graph2 = [[2, 4], [1, 3], [2], [1]]

# Directed
graph3 = {
    "node1": ["node2", "node4"],
    "node2": ["node3"],
    "node3": ["node4"],
    "node4": []
}

graph4 = [[2, 4], [3], [4], []]


## Create a Graph - when given a list of relationships
example_relations = [("c1","c2"), ("c2","c3"), ("c1","c4"), ("c2","c1"), ("c3","c2"), ("c4","c1")]
graph5 = {}
for relation in example_relations:
    node1 = relation[0]
    node2 = relation[1]
    if node1 not in graph5:
        graph5[node1] = []
    if node2 not in graph5:
         graph5[node2] = []
    if node2 not in graph5[node1]:
        graph5[node1].append(node2)
print(graph5)

## Get Edges and Vertices
nodes = graph3.keys()
edges = []
for node in graph3.keys():
    for node2 in graph3[node]:
        edges.append((node, node2))
print(nodes, edges)   

## Breath First Traverse or Topological Sort

# Iterative

# Recursive

## Depth First Traverse Graph

# Iterative

# Recursive

## Traverse through all the nodes of the Graph - Give relative ordering of all the nodes

