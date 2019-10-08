class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def gen_valid_paran(left, right, paran):
            if left:
                gen_valid_paran(left-1, right, paran + "(")
            if right > left:
                gen_valid_paran(left, right-1, paran + ")")
            if not right:
                self.params += paran,
        
        self.params = []
        gen_valid_paran(n, n, "")
        return self.params
