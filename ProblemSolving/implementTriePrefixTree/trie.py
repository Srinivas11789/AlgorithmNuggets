# Classification for each node
class Node(object):
    
    # Initialize 
    def __init__(self, val):
        self.next = {}
	self.val = val
        self.isAWord = False

    def add_next(self, ch): 
        new = Node(ch)
        self.next[ch] = new
        return new

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
	self.root = Node("")
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if c in cur:
               cur = cur.next
            else:
               cur = cur.add_next(c)
        cur.isAWord = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
