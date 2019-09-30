class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        
        # Logic 1:
        # * At every element delete, K elements and append the remaining string
        # * this logic doesnt work when consecutive number is the answer like [5,3,3,4], 2 ==> answer is 33
        """
        mini = float('inf')
        
        if k == len(num):
            return "0"
        elif len(num) == 1:
            return num
        
        if len(num[1:-1]) == len(num)-k and int(num[1:-1]) < mini:
            mini = int(num[1:-1])

        for i in range(len(num)):
            print(num[i], num[:i]+num[i+k:], mini)
            if num[:i]+num[i+k:] != "" and int(num[:i]+num[i+k:]) < mini:
                mini = int(num[:i]+num[i+k:])
                
        return str(mini)
        """
        
        # Logic 2: Lets go greedy --> At every iteration if the number is larger than the current element we remove it
        stack = []
        if len(num) == k:
            return '0'
        for i in range(len(num)):
            while k and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        print(stack)
        return str(int("".join(stack[:-k or None])))
