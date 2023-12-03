class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        def isGoodWord(word):
            temp = {}
            for i in word:
                if i not in self.characs:
                    return False
                if i not in temp:
                    temp[i] = 0
                temp[i] += 1
                if temp[i] > self.characs[i]:
                    return False
            return True

        
        self.characs = {}
        for i in chars:
            if i not in self.characs:
                self.characs[i] = 0
            self.characs[i] += 1
        
        ans = 0
        for i in words:
            if isGoodWord(i):
                ans += len(i)
        return ans

