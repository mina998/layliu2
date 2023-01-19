# -*- coding: utf-8 -*-

import sys
from os.path import abspath, dirname
from mitmproxy import http


class Scripts(object):

    def __init__(self):
        file = abspath(__file__)
        path = dirname(file)
        path = dirname(path)
        sys.path.append(path)

    @staticmethod
    def request(flow: http.HTTPFlow):
        url = flow.request.url

    @staticmethod
    def response(flow: http.HTTPFlow):
        # 茄子社区
        from filters.qiezi import QieZi
        QieZi(flow.request.url, flow.response.text)


addons = [
    Scripts(),
]
