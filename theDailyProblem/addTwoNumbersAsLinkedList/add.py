# The Problem
"""
You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
     self.val = x
     self.next = None

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    # Fill this in.
    carry = 0
    i = 0
    current_sum = 0
    answer = ""
    while l1 or l2:
        print(current_sum, carry)
        current_sum = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
        current_sum = list(str(current_sum))
        carry = (int("".join(current_sum[:-1])) if current_sum[:-1] else 0)
        answer += current_sum[-1]
        l1 = l1.next
        l2 = l2.next
        i += 1
        if not l1 and not l2:
            if carry:
                answer += str(carry)
    return answer[::-1]

def createLinkedList(array):
    linkedList = ListNode(array.pop())
    head = linkedList
    while array:
        next_node = ListNode(array.pop())
        linkedList.next = next_node
        linkedList = next_node
    return head

def main():
    s= Solution()
    l1 = createLinkedList([1,8,8])
    l2 = createLinkedList([1,9,9])
    print(s.addTwoNumbers(l1, l2))

main()

