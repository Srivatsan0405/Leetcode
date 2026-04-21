class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        return longUrl.encode(encoding='utf-8', errors='strict')


        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return shortUrl.decode(encoding='utf-8', errors='strict')


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))