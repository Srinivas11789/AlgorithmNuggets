import base64

class Codec:
    
    # Logic 1: use a dict to store (might cause o(N) space) using char count, or any random id or tail url
    # Logic 2: use base64 algo

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        
        noSlashes = longUrl.split("/")
        
        domain = "/".join(noSlashes[:3])
        encodedPath = base64.b64encode(("/".join(noSlashes[3:]).encode()))
        
        #print(noSlashes, domain, encodedPath)
        #print(domain+ "/" + encodedPath.decode('utf-8'))
        
        return domain+ "/" + encodedPath.decode('utf-8')
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        noSlashes = shortUrl.split("/")
        
        domain = "/".join(noSlashes[:3])
        decodedPath = base64.b64decode(("/".join(noSlashes[3:]).encode()))
        
        return domain+ "/" + decodedPath.decode('utf-8')
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
