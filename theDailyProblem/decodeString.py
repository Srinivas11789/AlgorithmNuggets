"""
Given a string with a certain rule: k[string] should be expanded to string k times. So for example, 3[abc] should be expanded to abcabcabc. Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.

Your starting point:

def decodeString(s):
  # Fill this in.

print decodeString('2[a2[b]c]')
# abbcabbc
"""

def decodeString(s):
        result = ""
        stack = []
        i = 0
        while i < len(s):
            if s[i] == "]":
                temp = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop() # remote [
                count = ""
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                stack.append(int(count)*temp)
            else:
                stack.append(s[i])
            i += 1
        return "".join(stack)

                
print decodeString('2[a2[b]c]')
