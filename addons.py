import mitmproxy.http
from mitmproxy import ctx
import requests
import os

Dir = os.path.join(os.path.dirname(__file__), 'video')


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        self.num = self.num + 1
        # ctx.log.info("we've seen %d flows" % self.num)
        # ctx.log.info(flow.request.host + flow.request.path)
        # ctx.log.info(flow.request.url)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        # if flow.request.url.endswith(".mp4"):
        if flow.request.url.startswith("http://v"):
            ctx.log.info("being load %s mp4" % flow.request.path)
            res = requests.get(flow.request.url, stream=True)
            filename = Dir + '\\' + str(self.num) + '.mp4'
            with open(filename, 'ab') as f:
                f.write(res.content)
                f.flush()
            ctx.log.info('%s is ok' % flow.request.path)


addons = [
    Counter()
]
