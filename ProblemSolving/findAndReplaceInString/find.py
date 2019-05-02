# Pending..
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        
        # Logic 2
        # * Create a relation between different elements in the problem
        # * Solve accordingly
        
        # Logic X: A Python Approach using a bunch of inbuilt functions
        result = S
        for i in range(len(indexes)):
            current = sources[i]
            index = indexes[i]
            n = len(current)
            if S[index:index+n] == current:
                result = result.replace(current, targets[i], 1)
        return result
        
        # Logic
        # * Literally follow instructions --> find and replace
        # * No overlap is a good thing and is given!
       
        # this problem has a bunch of disintegrated list which need to be related. Below logic will pass when the index list is sorted and corresponding entries are present in the targets list.
        # Having the indexes sorted would require each related list to arrange accordingly. Rethink a different approach
        """
        length_delta = 0
        # Start with index
        for i in range(len(indexes)):
            # Get the Source
            current = sources[i]
            index = indexes[i]+length_delta
            n = len(current)
            # Check the Source is S
            if S[index:index+n] == current:
                # Replace is match
                S= S[:index] + targets[i] + S[index+n:]
            length_delta += len(targets[i])-1
            print S
        return S
        """
