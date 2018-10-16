class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """

        # Use normal method of parathesis balancing with only "()" 
        # Use this logic to find the unmatched braces and return the length to make them balanced

	# Relation array
        relation = {"(":")"}

        # Stack to track the array
        stack = []

        # O(N) traverse through the array
        for i, e in enumerate(S):
   
            # If bracket is in key or "(" then append, else remove matched braces
            # Add mathced braces if more than one unbalanced exista
            if e in relation:
                stack.append(e)
            else:
                if stack and stack[-1] in relation:
                    stack.pop()
                else:
                    stack.append(e)
        return len(stack)
                
            
        
        
