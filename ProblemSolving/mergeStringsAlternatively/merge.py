class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        alternate = False
        while word1 or word2:
            alternate = not alternate
            if alternate:
                if not word1:
                    continue
                result += word1[0]
                word1 = word1[1:]
            else:
                if not word2:
                    continue
                result += word2[0]
                word2 = word2[1:]
            print(word1, word2, result, alternate)
        return result
