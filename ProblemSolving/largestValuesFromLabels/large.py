# Logic1: Literally following the problem with worst case complexity --> time limit exceeded (otherwise passes all case)

class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        
        indexes = range(0,len(values))
        maxi = -60000
        import itertools
        for S in range(num_wanted+1):
            for subset in itertools.combinations(indexes, r=S):
                subset_label = []
                subset_values = []
                for item in subset:
                    subset_label.append(labels[item])
                    subset_values.append(values[item])
                import collections
                counts = collections.Counter(subset_label)
                y = 0
                for c in counts.values():
                    if c <= use_limit:
                        y += 1
                #print subset, subset_label, subset_values
                if y == len(counts.keys()):
                    if sum(subset_values) > maxi:
                        maxi = sum(subset_values)
        return maxi
                    
                
