# Graphs

# Node of a graph basically a linked list
class node:
 
      def __init__(self, value):
          self.value = value
          self.next = None

      def insert_node(self, root, value):
          while root.next is not None:
                root = root.next
          root.next = node(value)

      def print_list(self, root):
          while root.next is not None:
                print(str(root.value)+" --> "),
                root = root.next
          print(str(root.value)),

# Graph construction
class graph:
     
      def __init__(self, size):
          self.size = size
          self.graph = [node(i) for i in range(size)]
          self.graph_matrix = [[0 for j in range(size)] for i in range(size)]

      def add_edge_undirected(self, src, dst):
	  
          # Node Representation
          # Undirected graph hence adding the node both the place (u,v) = (v,u)
          if self.graph[src]:
             self.graph[src].insert_node(self.graph[src], dst)
          else:
             print("src: Node doesnt exist!")
          if self.graph[dst]:
             self.graph[dst].insert_node(self.graph[dst], src)
          else:
             print("dst: Node doesnt exist!")

          # Matrix Representation
          self.graph_matrix[src][dst] = 1
          self.graph_matrix[dst][src] = 1
             
      def add_edge_directed(self, src, dst):
	  
	  # Node Representation
	  # Directed graph hence adding the node only at one place (u,v)
          if self.graph[src]:
             self.graph[src].insert_node(self.graph[src], dst)
          else:
             print("src: Node doesnt exist!")

          # Matrix Representation
          self.graph_matrix[src][dst] = 1

      def print_graph_list(self):
          for i in range(self.size):
               self.graph[i].print_list(self.graph[i])
               print("\n")
      
      def print_graph_matrix(self):
          for i in range(self.size):
                print self.graph_matrix[i]
         
          

# Main Function
def main():
    size = 5
    g = graph(size)
    g.add_edge_undirected(0, 1)
    g.add_edge_undirected(0, 4)
    g.add_edge_undirected(1, 2)
    g.add_edge_undirected(1, 3)
    g.add_edge_undirected(1, 4)
    g.add_edge_undirected(2, 3)
    g.add_edge_undirected(3, 4)
    g.print_graph_list()
    g.print_graph_matrix()

# Driver program
main()
          
	  


