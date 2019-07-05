# Node class to hold each node of the tree 
class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        # Include a new path for the path from root
        self.path = []
        
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        
        """
        # Logic 1: A normal method of constructing a tree
        # Al passed but scale test case time Limit exceeded - Improvise?
        
        ## Logic
        # 1.Finding the path
        # * We just need a depth first traversal until node.val == label
        
        # 2.Constructing a tree 
        # * with labels until the given input label is exceeded
        # * do something like a breath first traversal to figure out the node values
        
        ## Idea
        # 1. Using loop to construct tree and traverse is worse
        # 2. Using oath variable in Node and constructing a tree is robust but still leads to time limit exceeded
        
        self.current_label = 0
        
        self.result = []
        
        def construct_tree(nodes, current_level):
            
            # Hold all the children at the current level
            children = []
            
            # Next level should be even if current level is odd
            if current_level%2 != 0:
                # We go on reverse order if the next level is even
                start = self.current_label+len(nodes)*2+1
                self.current_label = start-1
                for node in nodes:
                    print(node.value)
                    start -= 1
                    node.left = Node(start)
                    node.left.path = node.path+[start]
                    if start == label:
                        #print node.value, node.left.path
                        self.result = node.left.path
                        return
                    start -= 1
                    node.right = Node(start)
                    node.right.path = node.path+[start]
                    if start == label:
                        #print node.value, node.right.path
                        self.result =  node.right.path
                        return
                    children.extend([node.left, node.right])
            else:
                for node in nodes:
                    print(node.value)
                    self.current_label += 1
                    node.left = Node(self.current_label)
                    node.left.path = node.path+[self.current_label]
                    if self.current_label == label:
                        #print node.value, node.left.path
                        self.result = node.left.path
                        return
                    self.current_label += 1
                    node.right = Node(self.current_label)
                    node.right.path = node.path+[self.current_label]
                    if self.current_label == label:
                        #print node.value, node.right.path
                        self.result = node.right.path
                        return
                    children.extend([node.left, node.right])
            
            
            if self.current_label < label:
                construct_tree(children, current_level+1)
            else:
                return
    
        def traverse(node, path):
            
            if node.value == label:
                self.result = path+[node.value]
                return
            
            if node.left:
                traverse(node.left, path+[node.value])
            if node.right:
                traverse(node.right, path+[node.value])
        
        self.current_label += 1
        root = Node(self.current_label)
        root.path.append(root.value)
        self.result = root.path
        construct_tree([root], 1)
        #traverse(root, [])
        return self.result
        """
    
    
        # Best answer is at https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/324011/Python-optimized-O(logn)-time-and-space-with-readable-code-and-step-by-step-explanation
        # This uses the BST property that
        # * in a normal bst, every parent is the HALF of the children
        #   - (selected_label)//2 == parent
        # * in a zigzag bst or even inverted row bst the property is
        #   - at that level,
        #     - (highest label + minimum_label - selected_label)//2 == parent
        
        self.result = []
        
        # First level
        level = 1
        num_of_nodes = 1
        
        # Property
        # * Also, as the level increase by 1 the num of nodes increase by multiples of 2
        
        # Find exactly at which level you have the selected label or the answer
        while label >= num_of_nodes*2:
            level += 1
            num_of_nodes *= 2
        
        # Iterate backwards finding the max, min and parent at the current level and apply formula
        # * At each level, there are 2 power n nodes, so the maximum at that node is level power 2 minus 1
        while level > 0:
            self.result.append(label)
            maximum = (2**level)-1 # maximum at the current level
            minimum = 2**(level-1) # max of last level is min for current
            label = (maximum + minimum - label)//2 # parent
            level -= 1
        
        return self.result[::-1]
            
            
        
        
        """
        # Logic 1: A bit confused so rewriting above....
        
        # Finding the path
        # * We just need a depth first traversal until node.val == label
        
        # Constructing a tree 
        # * with labels until the given input label is exceeded
        # * do something like a breath first traversal to figure out the node values
        
        
        # Result to hold all the node labels as we traverse
        self.result = []
        
        # Construct a tree
        
        self.next_label = 1
        
        def construct_tree(nodes, level):
            
            # Initialize the next level which is children
            children = []
            
            # Level being even or odd
            # Even: we reverse the nodes for reverse order values
            
            if level%2 != 0:
                nodes = nodes[::-1]
                for n in nodes:
                        self.next_label += 1
                        n.right = Node(self.next_label)
                        self.next_label += 1
                        n.left = Node(self.next_label)
                        children.extend([n.left, n.right])
            else:
                for n in nodes:
                        self.next_label += 1
                        n.left = Node(self.next_label)
                        self.next_label += 1
                        n.right = Node(self.next_label)
                        children.extend([n.left, n.right])

            if self.next_label < label:
                construct_tree(children, level+1)
            else:
                return
        
        def traverse(node, path):
            
            #result.append(node.value)
            
            if node.value == label:
                #print path+[node.value]
                self.result = path+[node.value]
                return
            
            print(node.value)
            if node.left:
                print(node.left.value)
            if node.right:
                print(node.right.value)
            #print path
            
            if node.left:
                traverse(node.left, path+[node.value])
            if node.right:
                traverse(node.right, path+[node.value])
            
        
        root = Node(self.next_label)
        self.next_label += 1
        root.right = Node(self.next_label)
        self.next_label += 1
        root.left = Node(self.next_label)
        construct_tree([root.left, root.right], 2)
        traverse(root, [])
        return self.result
        """
        
        
