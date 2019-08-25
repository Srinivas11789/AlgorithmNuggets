"""
# You are given an array of k sorted singly linked lists. Merge the linked lists into a single sorted linked list and return it.
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer
 
  def get_list(self):
    c = self
    answer = []
    while c:
      answer.append(str(c.val) if c.val else "")
      c = c.next
    return answer

def merge(lists):
  # Fill this in.

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print merge([a, b])
# 123456
"""

# Structure to create each node and link the next (eventually the full linked list)
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

  def get_list(self):
    c = self
    answer = []
    while c:
      answer.append(str(c.val) if c.val else "")
      c = c.next
    return answer

def merge(lists):
  # Pointers to store the start of each list ( avoid iterations and have a key to indicate start: say "-1" ) 
  pointers = [-1]*len(lists)
  # Resulting linked list to hold all merged nodes
  result = None
  ans = None
  min_next = None
  # Iterate until all the lists have been iterated ( that is None for every linkedlist )
  while set(pointers) != set([None]):
    #print(min_next)
    if min_next != None:
      if result == None:
        result = Node(pointers[min_next].val)
        if ans == None:
          ans = result
      else:
        result.next = Node(pointers[min_next].val)
        result = result.next
      if pointers[min_next]:
        pointers[min_next] = pointers[min_next].next 
    #print([p.val if p != -1 and p != None else str(p) for p in pointers], min_next, result.val if result != None else result)
    pointer = 0
    min_next = 0
    while pointer < len(pointers):
      # Set the head node of each linkedlist when the indicator is hit
      if pointers[pointer] != None:
        if pointers[pointer] == -1:
          pointers[pointer] = lists[pointer]
        if pointers[min_next] == None:
          min_next = pointer
        elif pointers[pointer].val < pointers[min_next].val:
          min_next = pointer
      print(min_next)
      pointer += 1
  return ans

def merge2(lists):
    result = []
    ans = None
    head = None
    for list in lists:
      result.extend(list.get_list())
    result.sort()
    for val in result:
      current_node = Node(val)
      if ans == None:
        ans = current_node
        head = ans
      else:
        ans.next = current_node
        ans = ans.next  
    return head
 
a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
print(merge2([a, b]))

