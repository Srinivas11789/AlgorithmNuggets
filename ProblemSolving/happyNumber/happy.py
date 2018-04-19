class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        ### Hacky method - 100pass
        # * true condition - existence of 1 and len(n) == 1 
        # * false condition - count till 1000 and return false if no match occured before
        n = map(int, str(n))
        count = 0
        while len(n) >= 1:
            happy = 0
            for k in n:
                happy += k**2
            n = map(int,str(happy))
            if n[0] == 1 and len(n) == 1:
                return True
            count += 1
            if count > 1000:
                return False
        """
        ### Discussion method using set() - kinda cool too
        # 100 pass as well
        # extra set to update the elements visited
        occurred = set()
        # until n is not 1
        while n != 1:
            # sum of square of each digit
            n = sum([int(i)**2 for i in str(n)])
            # if same number is visited twice, exit, else add the number
            if n in occurred:
                return False
            else:
                occurred.add(n)
        return True
            
        
