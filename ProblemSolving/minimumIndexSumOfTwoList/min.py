class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        # 
        
        # Using a list for selected restaurant as it can be multiple
        selected = {}
        min_index = len(list1+list2)
        current = None
        
        # O(N) Looping
        for i in range(len(list1)):
            if list1[i] in list2:
                index = list2.index(list1[i])
                if i + index <= min_index:
                    min_index = i + index
                    current = list1[i]
                    if min_index not in selected:
                        selected[min_index] = []
                    selected[min_index].append(current)
        
        print selected
        mini = min(selected.keys())
        return selected[mini]
                        
            
        
