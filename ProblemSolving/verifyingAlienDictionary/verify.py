class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        """
        # This logic is for each word to be lexicographic. the question asks you to do lexicographic of the words
        result = True
        # Brute force
        for word in words:
            temp = list(word)
            prev = -1
            while temp:
                for j in range(len(order)):
                    if order[j] == temp[0] and prev < j:
                        del temp[0]
                        prev = j
                        break
    
            if temp == []:
                result =  result and True
            else:
                result = result and False
        return result
        """
                        
        # 2 pointer method
        
        # Firstly, if there is a length decrease down the line (based on null logic), it would be a false
        sort_by_len = sorted(words, key = len)
        if sort_by_len == words:
            return True
        #else:
        #    return False
        
        # Secondly iterate by index for all the entries in the array (instead of iterating 2 by 2 or 3 by 3)
        n = len(words)
        indexes = [0]*n

        def sort_by_order(ch):
            if ch == None:
                return len(order)
            return order.index(ch)
        
        maxi = len(sort_by_len[-1])
        for j in range(maxi):
            for i in range(len(words)):
                    if j >= len(words[i]):
                        indexes[i] = None
                    else:
                        indexes[i] = words[i][j]

            if sorted(indexes,key=sort_by_order) == indexes:
                continue
            else:
                print indexes
                return False
        return True
            
        """
        # List of lists logic may not work with this logic
        # Sorted logic method
        def sort_by_order(ch):
            return order.index(ch)
        
        if sorted(words, key = sort_by_order) == words:
            return True
        else:
            return False
        """
