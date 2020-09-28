class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        # Logic 1: Iterative without inbuilt functions --> 99% faster
        result = ""
        if n == 0:
            return "0"
        while n:
            next_thousand = n%1000
            n = n//1000
            if n:
                fmtStr = "." + "{:03d}".format(next_thousand)
            else:
                fmtStr = str(next_thousand)
            result = fmtStr + result
        return result.strip()
