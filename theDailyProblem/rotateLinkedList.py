"""
Given a linked list and a number k, rotate the linked list by k places.

Here's some starter code and an example:

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    current = self
    ret = ''
    while current:
      ret += str(current.value)
      current = current.next
    return ret

def rotate_list(list, k):
  # Fill this in.

# Order is 1, 2, 3, 4
llist = Node(1, Node(2, Node(3, Node(4))))

# Order should now be 3, 4, 1, 2
print(rotate_list(llist, 2))
# 3412
"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    current = self
    ret = ''
    while current:
      ret += str(current.value)
      current = current.next
    return ret

def rotate_list(head, k):
        # O(2N) ==> O(N) Logic

        # Head is the first node
        front = head
        length = 1

        # Tail is the last node, we use O(N)
        tail = None
        while head and head.next:
            length += 1
            head = head.next
        tail = head

        # Modulate k for rotation
        k = (length-k)%length

        # Rotate until k is zero
        while head and tail and k:
            tail.next = front
            front = front.next
            tail = tail.next
            tail.next = None
            k -= 1

        return front
         
# Order is 1, 2, 3, 4
llist = Node(1, Node(2, Node(3, Node(4))))

# Order should now be 3, 4, 1, 2
print(rotate_list(llist, 2))
