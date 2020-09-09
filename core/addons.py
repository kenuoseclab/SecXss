#!/usr/bin/env python
# encoding: utf-8
"""
@author: sys71m
@contact: sys71m@163.com
@software: pycharm
@file: addons.py
@desc:
"""
from mitmproxy.http import HTTPFlow
from core.date import flow_queue
from core.flowinfo import FlowInfo


class Addons:

    def request(self, flow: HTTPFlow):
        tmp_flow = FlowInfo(flow.request, flow.response)
        flow_queue.put(tmp_flow)
