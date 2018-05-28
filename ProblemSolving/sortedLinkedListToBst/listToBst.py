# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # List here mentions LinkedList data structure and not python lists
        
        """
        # Logic1: 100pass
        # InOrder Type Logic ==> Left + node.val + Right
        # Steps:
        # 1. Get the length of the list
        # 2. Use a control variable or array to maintain each node of the list as we traverse
        # 3. Use l,r pointer to track the progress
        # 4. Use InOrder type assigning
        
        def listToTree(control, l, r):
            
            # Left and the Right pointers
            if l > r:
                return None
            
            # Calculate the middle element
            mid = (l+r)//2
            
            # 4. InOrder Type Traverse
            left = listToTree(control, l, mid-1)
            
            node = TreeNode(control[0].val)
            control[0] = control[0].next
            
            right = listToTree(control, mid+1, r)
            
            node.left = left
            node.right = right
            
            return node
        
        
        # Null check for list head
        if not head:
            return None
        
        # Step 1 and Part Step 2
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        # the control element is a single element list here, using list the elements are mutatable inside the list, where using just a variable is not. Hence using list work here.
        return listToTree([head], 0, length-1)
        """
        
        # Logic2: 100pass
        # 1. Convert the Linkedlist into an array representation 
        # 2. Solve as the arrayToBst logic we used earlier
        
        def arrayToBst(nums):
            
            if not nums:
                return None
        
            mid = len(nums)//2
            
            node = TreeNode(nums[mid])
            node.left = arrayToBst(nums[:mid])
            node.right = arrayToBst(nums[mid+1:])
            return node
        
        current = head
        arrayOfElements = []
        while current:
            arrayOfElements.append(current.val)
            current = current.next
        
        return arrayToBst(arrayOfElements)
        
        
        
        
        
        
