# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """
        # 100 pass 
        # 1. Making sum as we iterate through the list and creating a new list
        sumi = l1.val + l2.val
        carry = sumi//10
        output = ListNode(sumi%10)
        result = output
        #output.next = ListNode(carry)
        while l1.next != None and l2.next != None:
                output.next = ListNode(carry)
                output = output.next
                l1 = l1.next
                l2 = l2.next
                #print output.val,l1.val,l2.val
                sumi = l1.val + l2.val + output.val
                output.val = sumi%10
                carry = sumi//10
        while l1.next != None:
            l1 = l1.next
            sumi = l1.val+carry
            carry = sumi//10
            output.next = ListNode(sumi%10)
            output = output.next
        while l2.next != None:
            l2 = l2.next
            sumi = l2.val+carry
            carry = sumi//10
            output.next = ListNode(sumi%10)
            output = output.next
        if carry:
            output.next = ListNode(carry)
        return result
        """
        
        # 100 pass
        # 2. Iterate throught the list, get the numbers, then add them and remake the list to return
        num1 = [str(l1.val)]
        num2 = [str(l2.val)]
        while l1.next != None:
            l1 = l1.next
            num1.append(str(l1.val))
        while l2.next != None:
            l2 = l2.next
            num2.append(str(l2.val))
        sumi = int("".join(num1[::-1])) +  int("".join(num2[::-1]))
        sumi = map(int,str(sumi))[::-1]
        output = ListNode(sumi[0])
        result = output
        for num in sumi[1:]:
            output.next = ListNode(num)
            output = output.next
        return result
            
        
