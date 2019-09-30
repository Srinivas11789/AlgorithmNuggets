# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        # Simple sort and create linkedlist
        
        if not lists:
            return ListNode("")
        
        def get_values_from_linked_list(array):
            result = []
            while array:
                result.append(array.val)
                array = array.next
            return result
    
        def create_linked_list_from_list(array):
            if array:
                result = ListNode(array[0])
                ans = result
                for i in range(1, len(array)):
                    result.next = ListNode(array[i])
                    result = result.next
                result.next = None
                return ans
            else:
                return ListNode("")
        
        all_values = []
        for linkedlist in lists:
            all_values.extend(get_values_from_linked_list(linkedlist))
        all_values.sort()
        
        return create_linked_list_from_list(all_values)
        
        
        """
        Logic 2: time limit exceeded but all other cases passed
        
        # Resulting linked list to hold all merged nodes
        result = None
        ans = None
        min_next = None
        
        if not lists:
            return ListNode("")
        
        # Iterate until all the lists have been iterated ( that is None for every linkedlist )
        while lists and set(lists) != set([None]):
            #print(min_next)
            if min_next != None and lists[min_next]:
                if result == None:
                    result = ListNode(lists[min_next].val)
                    if ans == None:
                        ans = result
                else:
                    result.next = ListNode(lists[min_next].val)
                    result = result.next
                if lists[min_next]:
                    lists[min_next] = lists[min_next].next
            print([p.val if p != -1 and p != None else str(p) for p in lists], min_next, result.val if result != None else result)
            pointer = 0
            min_next = 0
            while pointer < len(lists):
                # Set the head node of each linkedlist when the indicator is hit
                if lists[pointer] != None:
                    if lists[min_next] == None:
                        min_next = pointer
                    elif lists[pointer] and lists[pointer].val < lists[min_next].val:
                        min_next = pointer
                    pointer += 1
                else:
                    lists.pop(pointer)
        return ans
        """
        
        
        """
        Logic 3: time limit exceeded but all other cases passed (with helpers pointer array)
        
        # Pointers to store the start of each list ( avoid iterations and have a key to indicate start: say "-1" )
        pointers = [-1]*len(lists)
        
        # Resulting linked list to hold all merged nodes
        result = None
        ans = None
        min_next = None
        
        if not lists:
            return ListNode("")
        
        # Iterate until all the lists have been iterated ( that is None for every linkedlist )
        while set(pointers) != set([None]):
            #print(min_next)
            if min_next != None:
                if result == None:
                    result = ListNode(pointers[min_next].val)
                    if ans == None:
                        ans = result
                else:
                    result.next = ListNode(pointers[min_next].val)
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
                    elif pointers[pointer] and pointers[pointer].val < pointers[min_next].val:
                        min_next = pointer
                #print(min_next)
                pointer += 1
        return ans
        """

