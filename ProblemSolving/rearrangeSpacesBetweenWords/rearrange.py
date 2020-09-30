# Logic 1: Iterate to find words, space + compute to answer: 100 pass 86.30% faster 
class Solution:
    def reorderSpaces(self, text: str) -> str:
        # Count spaces and Obtain all words
        words = []
        spaces = 0
        current_word = ""
        for i in range(len(text)):
            if text[i] == " ":
                spaces += 1
                if current_word:
                    words.append(current_word)
                    current_word = ""
            else:
                current_word += text[i]
        if current_word:
            words.append(current_word)
        if spaces == 0:
            return text
        if len(words) <= 1:
            return words[0] + " "*spaces
        equal_spaces = spaces//(len(words)-1)
        remaining = spaces%(len(words)-1)
        #remaining = spaces - equal_spaces*len(words)
        #print(spaces, len(words), equal_spaces, remaining)
        return (" "*equal_spaces).join(words) + " "*remaining
