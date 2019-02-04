# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        
        # Logic1: Recursive with No Extra space - 1 --> as of now 100% faster and less than 100% memory
        
        # Function to convert the number into alphabet
        def number_to_alphabet(num):
            # lowercase a ==> ord('a') = 97, so iterate from there
            return chr(97+num)
        
        # Recursively traverse until the leaf nodes
        def traverse(node, string):
            
            # At the leaf node, add the string from the lead to root to the strings list
            # * Reverse string constructed to reverse order from root -> leaf and add the leaf character beginning
            if node:
                if not node.left and not node.right:
                    return number_to_alphabet(node.val)+string[::-1]
                else:
                    # Compare left and right for minimum lexico, else return left or right
                    left = traverse(node.left, string+number_to_alphabet(node.val))
                    right = traverse(node.right, string+number_to_alphabet(node.val))
                    if left and right:
                        return min(left, right)
                    elif left:
                        return left
                    else:
                        return right
        
        
        # Logic2: Recursive with Extra space to hold the strings - as of now 100% faster and less than 100% memory
        # * Sort the list to obtain the answer finally
        
        # Recursively traverse until the leaf nodes
        def traverse2(node, string):
            
            # At the leaf node, add the string from the lead to root to the strings list
            # * Reverse string constructed to reverse order from root -> leaf and add the leaf character beginning
            if node:
                if not node.left and not node.right:
                    self.strings.append(number_to_alphabet(node.val)+string[::-1])
                else:
                    traverse(node.left, string+number_to_alphabet(node.val))
                    traverse(node.right, string+number_to_alphabet(node.val))
        
        
        # ** Logic1:
        # Trigger
        return traverse(root, "")
        
        # ** Logic2:
        
        # List to hold all strings
        #self.strings = []
        
        # Trigger it
        #traverse2(root, "")
        
        # Sort and return the first
        #return sorted(self.strings)[0]

