class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
    
        # Logic - 100 pass 100%
        # * Stack to store and iterate
        # ** We will operate only when "]" appear in the string
        
        stack = []
        
        # Iterate across the string
        for i in range(len(s)):
            # Operate only on ]
            if s[i] == "]":
                # fetch the sub string within []
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop() # removes "["
                # fetch the integer times 
                num_of_time = ""
                while stack and stack[-1].isdigit(): # stack[-1] != "]"
                    num_of_time = stack.pop() + num_of_time
                # Append the decoded string back into stack (to support nested format)
                stack.append(int(num_of_time)*substring)
            else:
                # Add everything except "]" into array
                stack.append(s[i])
        # Return stack
        return "".join(stack)
                
