"""
even if you pass same long url twice it will give the same shorturl
"""

BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def base_62_encode(num, alphabet=BASE62):
    """Encode a positive number into Base X and return the string."""

    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)


def base_62_decode(string, alphabet=BASE62):
    """Decode a Base X encoded string into the number"""

    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num


class Codec:

    def __init__(self):
        self.urls = [0]*1000000
        self.url_map = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.url_map:
            self.urls.append(longUrl)
            id = len(self.urls) - 1
            self.url_map[longUrl] = id
        else:
            id = self.url_map[longUrl]

        return base_62_encode(id)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        id = base_62_decode(shortUrl)
        return self.urls[id]


shortner = Codec()
a = shortner.encode('google.com')
print(a)
b = shortner.encode('google.com')
print(shortner.decode(b))
print(b)
