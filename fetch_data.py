
import http.cookiejar
import urllib.error
import urllib.parse
import urllib.request


class HttpClient(object):
    def __init__(self):
        cookie_filename = 'cookie_jar.txt'
        cookie_jar = http.cookiejar.MozillaCookieJar(cookie_filename)
        handler = urllib.request.HTTPCookieProcessor(cookie_jar)
        self.opener = urllib.request.build_opener(handler)
        self.headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }

    def get(self, url):
        request = urllib.request.Request(
            url,  headers=self.headers, method='GET')
        response = self.opener.open(request)
        return response

    def post(self, url, params):
        'contentType: x-www-form-urlencoded'
        postdata = urllib.parse.urlencode(params).encode()
        request = urllib.request.Request(url, postdata, self.headers)
        response = self.opener.open(request)
        return response


client = HttpClient()

url = 'https://yun.aura.cn/Login/login.html'
res = client.get(url)



LOGIN_URL = ''
passwd = ''
post_params = {
    'token': '744b74e4f49b8507d2004b3d2e0f0213',
    'vcode': '882f9e54f4ccd05ca384bb3c0b20e1d7',
    'cksign': 'c9fb697fa894511e529d76634c49c72a',
    'encpwd': md5(passwd),
    'phone': '13865167784'
}
res = client.post(LOGIN_URL, post_params)
