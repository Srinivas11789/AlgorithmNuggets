# Is a binary search tree problem
# Lessons Learned:
#   * Obvious technique is to visit every node and evaluate for BST rule in a recusive manner
#   * The obvious solution being checking for left or right to be lesser than or greater than each node respectively does not work, the max and min should be properly set for it to work
#   * The solution that would work is by setting min and max as we traverse through the tree
#	* Initially for the root node set the min and max to be -infinity and infinity
# 	* Example, as we progress through the left node, the maximum remains the root and min keeps changing as we move down
#   * The equal parameter failed a number of testcase:
#   	* checking for both less than and greater than equal passes all the testcases as both the condition could occur while we traverse deeper
#   * Recursion Structure: Observe Think and then compute the recursion structure, Returning at places without any technique would provide abruptly wrong answers
#  	* return True in the else loop would fail a lot of testcases
#	* Return for success at the deepest occurence of recursion and return for failure anytime

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
        
        def check(node, mini, maxi):
            if node is None:
                return True
            if node.data <= mini or node.data >= maxi:
                return False
            return check(node.left, mini, node.data) and check(node.right, node.data, maxi)
            
        mini = float('-inf')
        maxi = float('inf')
        return check(root, mini, maxi)
        
                                            
    #return checkBST(root.left)+checkBST(root.right)

        
        
  

