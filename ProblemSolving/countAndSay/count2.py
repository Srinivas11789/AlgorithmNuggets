class Solution:
    def countAndSay(self, n: int) -> str:

        def say(nStr):
            
            ns = list(nStr)
            stack = []
            saying = ""

            while ns:
                #print(ns)
                curr = ns.pop(0)
                if stack and stack[-1] == curr:
                    stack.append(curr)
                else:
                    if stack:
                        saying += str(len(stack))+stack[-1]
                    stack = [curr]

            if stack:
                saying += str(len(stack))+stack[-1]

            return saying

        self.memo = {1:"1"}
        for i in range(2, n+1):
            result = say(self.memo[i-1])
            self.memo[i] = result

        #print(self.memo)
        return self.memo[n]
