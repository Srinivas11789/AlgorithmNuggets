class Solution:
    # Logic 1: check for empty and palindrome all other cases it will becomes palindrome when removing 2 elements
    def removePalindromeSub(self, s: str) -> int:
            if s == "":
                return 0
            if s == s[::-1]:
                return 1
            return 2
