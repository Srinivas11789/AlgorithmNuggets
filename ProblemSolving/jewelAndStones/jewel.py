#### Practice this easy problem in GO as well by today
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        
        """
        # 100 pass 
        
        count = 0
        
        for stone in S:
            if stone in J:
                count += J.count(stone)
        
        return count
        """
        
        # Not so pythonic solution - 100
        count = 0
        
        for i in range(len(S)):
            if S[i] in J:
                count += 1
        return count
