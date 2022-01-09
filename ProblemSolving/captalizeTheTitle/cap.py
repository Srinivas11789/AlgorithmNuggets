"""
https://leetcode.com/contest/biweekly-contest-69/problems/capitalize-the-title/
"""
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")
        for w in range(len(words)):
            if len(words[w]) <= 2:
                words[w] = words[w].lower()
            else:
                words[w] = words[w][0].upper() + words[w][1:].lower()
        return " ".join(words)
