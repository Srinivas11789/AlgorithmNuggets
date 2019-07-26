# Reverse a Linked List

"""
Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?

Example:
Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None
  
  # Function to print the list
  def printList(self):
    node = self
    output = '' 
    while node != None:
      output += str(node.val)
      output += " "
      node = node.next
    print(output,)

  # Iterative Solution
  def reverseIteratively(self, head):
    # Implement this.

  # Recursive Solution      
  def reverseRecursively(self, head):
    # Implement this.

# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
testHead.reverseIteratively(testHead)
#testHead.reverseRecursively(testHead)
print("List after reversal: ")
testTail.printList()
# 0 1 2 3 4
"""

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None    

class Solution:
     def reverse_linked_list_iterative(self, node):
         # Logic 1: using extra space to keep track of visited nodes
         """
         stack = []
         head = node
         while node:
              stack.append(node)
              node = node.next
         while stack:
              print(stack)
              first, last = None, None
              if stack:
                  last = stack.pop()
              if stack:
                  first = stack.pop(0)
              if last and first:
                  print(last.val, first.val)
                  last.val, first.val = first.val, last.val
         return head
         """

         # Logic 2: inverting next pointers as we visit and go to the next node
         reverse_pointer = None
         head = None 
         while node:
               if node.next is None:
                   head = node
               current_node = node # Store the current node reference
               node = node.next # Move node to the next node to not loose pointer
               current_node.next = reverse_pointer
               reverse_pointer = current_node
         return head

     def reverse_linked_list_recursive(self, current, previous):
        if current:
            next = current.next
            current.next = previous
            #if current.next is not None:
            #    print(current.val, current.next.val)
            if next == None:
               return current
            else:
               return self.reverse_linked_list_recursive(next, current)
        else:
            return

def construct_linked_list(input):
    # Construct linkedlist from the array
    root = Node(input[0])
    head = root
    for i in range(1, len(input)):
        head.next = Node(input[i])
        head = head.next
    return root

def print_linked_list(node):
    while node:
        print(node.val,)
        node = node.next

def main():
    s = Solution()
    input = [4, 3, 2, 1, 0]
    
    head = construct_linked_list(input)
    #head = s.reverse_linked_list_iterative(head)
    head = s.reverse_linked_list_recursive(head, None)
    print_linked_list(head)

main()
