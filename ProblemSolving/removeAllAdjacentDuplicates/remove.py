class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        
        # Stack logic: Pop until the values are same else push
        stack = []
        
        for element in S:
            if not stack:
                stack.append(element)
            elif stack[-1] != element:
                stack.append(element)
            else:
                stack.pop()
        return "".join(stack)
