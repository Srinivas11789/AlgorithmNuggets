class Solution:
    def reverseWords(self, s: str) -> str:

        # 1. stack push and pop with 2*O(N) iteration for chars or for words split instead of one iteration

        process = s.split(" ")
        stack = []

        for i in range(len(process)):
            s = process[i].strip()
            if not s:
                continue
            stack = [s] + stack

        return " ".join(stack)
