#!/usr/bin/env python
# encoding: utf-8
"""
@author: sys71m
@contact: sys71m@163.com
@software: pycharm
@file: flowinfo.py
@desc:
"""
from mitmproxy.http import HTTPFlow


class FlowInfo(object):
    def __init__(self, requests: HTTPFlow, response: HTTPFlow):
        super()
        self.requests = requests
        self.response = response

    @property
    def url(self) -> str:
        return self.requests.url

    @property
    def method(self) -> str:
        return self.requests.method

