iclass node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class Graph:
    
    def __init__(self, size):
        self.size = size
        self.graph_list = [node(i) for i in range(size)]
        self.graph = [[-1 for i in range(size)] for j in range(size)]
        
    def connect_list(self, src, dst):
        #print src,dst
        n = self.graph[src]
        while self.graph[src].next != None:
            self.graph[src] = self.graph[src].next
        self.graph[src].next = node(dst)
    
    def find_all_distances_list(self, start):
        nodes = [i for i in range(self.size) if i!=start] # 1,2,3,4
        edges = [] # 3,2
        while self.graph[start].next != None:
            edges.append(self.graph[start].value)
            self.graph[start] = self.graph[start].next
        edges.append(self.graph[start].value)
        #print nodes
        #print edges
        for node in nodes:
            if node in edges:
                print 6,
            else:
                print -1,
        print "\n",
        
    def connect(self, src, dst):
        # Only one test case passed, but it is a undirected graph !!!!!!
        if self.graph[src][dst] == -1:
            self.graph[src][dst] = 0
        self.graph[src][dst] = 6
        # undirected graph u,v == v,u
        if self.graph[dst][src] == -1:
            self.graph[dst][src] = 0
        self.graph[dst][src] = 6
        
        for i in range(self.size):
            if self.graph[dst][i] > 0:
                value = self.graph[dst][src] + self.graph[dst][i]
                if self.graph[src][i] > value or self.graph[src][i] < 0:
                    self.graph[src][i] = value
            if self.graph[src][i] > 0:
                value = self.graph[src][dst] + self.graph[src][i]
                if self.graph[i][dst] > value or self.graph[i][dst] < 0:
                    self.graph[i][dst] = value
    
    def find_all_distances(self, start):
        for i in range(self.size):
            if i != start:
                print self.graph[start][i],
        print "\n",
                

t = input()
for i in range(t):
    n,m = [int(x) for x in raw_input().split()]
    graph = Graph(n)
    for i in xrange(m):
        x,y = [int(x) for x in raw_input().split()]
        graph.connect(x-1,y-1) 
    s = input()
    graph.find_all_distances(s-1)
    

