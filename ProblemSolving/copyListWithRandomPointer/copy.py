"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return

        # relate existing node to new nodes for deep copy
        node_to_new_nodes = {}
        traverse = head
        while traverse:
            # current
            new_node = Node(traverse.val)
            node_to_new_nodes[traverse] = new_node
            # next
            if traverse.next and traverse.next not in node_to_new_nodes:
                nxt_node = Node(traverse.next.val)
                node_to_new_nodes[traverse.next] = nxt_node
            # random
            if traverse.random and traverse.random not in node_to_new_nodes:
                rnd_node = Node(traverse.random.val)
                node_to_new_nodes[traverse.random] = rnd_node
            
            traverse = traverse.next

        traverse = head
        copy = node_to_new_nodes[traverse]
        result = copy
        while traverse:
            if traverse.next:
                copy.next = node_to_new_nodes[traverse.next]
            if traverse.random:
                copy.random = node_to_new_nodes[traverse.random]
            copy = copy.next
            traverse = traverse.next

        return result

