
class Codec:
    
    def __init__(self):
        self.db = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        import random
        split = longUrl.split("/")
        val = "/".join(split[3:])
        key = str(hex(random.randint(10000,50000)))[2:]
        if key not in self.db:
            self.db[key] = val
        return split[0]+"//"+split[2]+"/"+key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        :type shortUrl: str
        :rtype: str
        """
        import random
        split = shortUrl.split("/")
        key = split[3]
        shortUrl = split[0]+"//"+split[2]+"/"+self.db[key]
        return shortUrl
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
