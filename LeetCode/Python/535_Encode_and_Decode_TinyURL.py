class Codec:

    def __init__(self):
        self.dict = {}
        self.rev = {}
        self.idx = 0


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.dict:
            return longUrl
        else:
            self.dict[longUrl] = self.idx
            self.rev[self.idx] = longUrl
            self.idx += 1
            return self.dict[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if shortUrl in self.rev:
            return self.rev[shortUrl]
        return shortUrl

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))