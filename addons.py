import mitmproxy.http
import requests
from mitmproxy import ctx
from requests_futures.sessions import FuturesSession
import os


Dir = os.path.join(os.path.dirname(__file__), 'video')


class Counter:
    def __init__(self):
        self.num = 0
        self.session = FuturesSession()

    # def request(self, flow: mitmproxy.http.HTTPFlow):
    #     self.num = self.num + 1
    #     # ctx.log.info("we've seen %d flows" % self.num)
    #     # ctx.log.info(flow.request.host + flow.request.path)
    #     # ctx.log.info(flow.request.url)

    def response(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.url.startswith("http://v"):

            # with open(os.path.join(Dir, 'mitm.txt'), 'a+') as f:
            #     f.write(flow.request.url + '\n')
            #     f.write(flow.request.path + '\n\n')

            # res = self.session.get(flow.request.url, stream=True)
            res = requests.get(flow.request.url, stream=True)
            # result_url = res.result()

            filename = Dir + '\\' + flow.request.path[1:].split('/', 1)[0] + '.mp4'

            with open(filename, 'ab') as f:
                try:
                    f.write(res.content)
                    # f.write(result_url.content)
                except Exception as e:
                    with open(os.path.join(Dir, 'mitmerror.txt'), 'a') as fe:
                        fe.write('error video: %s, (<%s>)' % (flow.request.url, e))
                f.flush()



addons = [
    Counter()
]
