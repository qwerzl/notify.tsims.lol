import aiohttp.cookiejar


class tSession:
    def __init__(self, cookies: aiohttp.cookiejar.CookieJar):
        self.cookies = cookies
