"""
Given an expression (as a list) in reverse polish notation, evaluate the expression. Reverse polish notation is where the numbers come before the operand. Note that there can be the 4 operands '+', '-', '*', '/'. You can also assume the expression will be well formed.

Example
Input: [1, 2, 3, '+', 2, '*', '-']
Output: -9
The equivalent expression of the above reverse polish notation would be (1 - ((2 + 3) * 2)).

Here's some starter code:

def reverse_polish_notation(expr):
  # Fill this in.
  
# 1 - (2 + 3) * 2
print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
# -9
"""

def reverse_polish_notation(expr):
  
  # Logic 1: Find the inner most operand and evaluate 
  # * Iterate to find the indexes of all the operands backwards
  indexes = []
  #print(expr)
  for i in range(len(expr)-1, -1, -1):
    if expr[i] in ['+', '-', '*', '/']:
      indexes = [i] + indexes
  for i in indexes:
    o1 = i-1
    while expr[o1] == "":
      o1 -= 1
    op1 = str(expr[o1])
    expr[o1] = ""
    while expr[o1] == "":
      o1 -= 1
    op2 = str(expr[o1])
    expr[o1] = ""
    expr[i] = eval(op2+expr[i]+op1)
    #print(expr)
  #print(expr)
  return expr[-1]
    
# 1 - (2 + 3) * 2
print(reverse_polish_notation([1, 2, 3, '+', 2, '*', '-']))
# -9

"""
class Solution(object):
    def evalRPN(self, expr):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        # Logic 1: Find the inner most operand and evaluate - 5% Faster Only
        # * Iterate to find the indexes of all the operands backwards
        
        """
        indexes = []
        #print(expr)
        for i in range(len(expr)-1, -1, -1):
            if expr[i] in ['+', '-', '*', '/']:
                indexes = [i] + indexes
        for i in indexes:
            o1 = i-1
            while expr[o1] == "":
                o1 -= 1
            op1 = str(int(expr[o1]))
            expr[o1] = ""
            while expr[o1] == "":
                o1 -= 1
            op2 = str(int(expr[o1]))
            expr[o1] = ""
            expr[i] = eval(op2+expr[i]+op1)
            #print(expr)
        #print(expr)
        return int(expr[-1])
        """
        
        # Logic 2: Single Iteration Logic --> 92% faster
        stack = []
        for i in range(len(expr)):
            if expr[i] not in ["+","-","/","*"]:
                stack.append(expr[i])
            else:
                r = int(stack.pop())
                l = int(stack.pop())
                if expr[i] == "+":
                    stack.append(l+r)
                elif expr[i] == "*":
                    stack.append(l*r)
                elif expr[i] == "/":
                    if l*r < 0 and l%r != 0:
                        stack.append(l//r+1)
                    else:
                        stack.append(l//r)
                elif expr[i] == "-":
                    stack.append(l-r)
                else:
                    print("wrong")
            #print(stack)
        return stack[-1]
        # Ref: https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/47444/Python-solution-with-comments-(don't-use-eval()-function).
"""
