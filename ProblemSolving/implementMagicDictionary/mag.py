class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        """
        # Dictionary 
        self.dic = {}
        """
        self.dic = []

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        
        """
        # Add words in dictionary - with possible list of character for somthing useful
        for word in dict:
            self.dic["default"].append(word)
            for i in range(len(word)):
                value = word[:i]+word[i+1:]
                self.dic[value] = ""
        """
        
        self.dic.extend(dict)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        
        flag = False
        for w in self.dic:
            if len(w) == len(word):
                count = 0
                for a,b in zip(w, word):
                    if a != b:
                        count += 1
                if count == 1:
                    flag = True
        return flag
            
        """
        ### Doesnt work for "hallo" and "hello" occurence
        if word in self.dic["default"]:
            return False
        
        # Check for one character delete condition
        for i in range(len(word)):
            if word[:i]+word[i+1:] in self.dic:
                return True
            
        # Return False by default
        return False
        """ 
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
