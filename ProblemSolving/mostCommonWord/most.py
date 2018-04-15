
# Using Dictionary
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        count = {}
        
        for word in paragraph.strip().split(" "):
            word = word.lower().strip(",.?!;':")
            if word not in count:
                count[word] = 0
            count[word] += 1
        
        maxi = 0
        select = ""
        for key, value in count.items():
            if (value > maxi) and (key not in banned):
                maxi = value
                select = key
        
        return select

# Todo ==> Try doing this without dictionary
