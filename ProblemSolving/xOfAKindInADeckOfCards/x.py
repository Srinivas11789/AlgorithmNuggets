class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # Get the frequency of the array
        import collections
        dictionary = collections.Counter(deck)
        counts = sorted(set(dictionary.values()))
        
        #  If all elements have same frequency
        if len(counts) == 1 and counts[0] >= 2:
            return True
        # If all elements have different frequency
        elif len(counts) > 1:
            # Calculating GCD
            div = []
            for i in range(1,counts[0]+1):
                if i != 1 and counts[0]%i == 0:
                    div.append(i)
            print counts
            print div
            if div:
                for d in div:
                    c = 0
                    for i in range(0, len(counts)):
                        print counts[i], d
                        if counts[i]%d == 0:
                            c += 1
                    if c == len(counts):
                        return True
                return False
            else:
                return False
        else:
            return False
        
