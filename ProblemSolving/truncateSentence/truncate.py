class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # Logic 1: using string split and rejoin k words - 100 pass - 85% faster
        ## return " ".join(s.split(" ")[:k])
    
        # Logic 2: Naive iteration
        result = ""
        word = ""
        count = 0
        for c in s:
            print(word, result, count, c)
            if count >= k:
                return result
            if c == " ":
                if result != "":
                    result += " "
                result += word
                word = ""
                count += 1
            else:
                word += c
        if word:
            if result:
                result += " "
            result +=  word
        return result
