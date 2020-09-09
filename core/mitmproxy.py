#!/usr/bin/env python
# encoding: utf-8
"""
@author: sys71m
@contact: sys71m@163.com
@software: pycharm
@file: mitmproxy.py
@desc:
"""
import time
from mitmproxy.tools import cmdline
from mitmproxy import addons
from mitmproxy import options
from mitmproxy import master
from mitmproxy.addons import dumper, termlog, termstatus, keepserving, readfile
from core.addons import Addons
from mitmproxy.tools._main import run


def mitmdump(args=None):
    run(DumpMaster, cmdline.mitmdump, args)


class ErrorCheck:
    def __init__(self):
        self.has_errored = False

    def log(self, e):
        if e.level == "error":
            self.has_errored = True


class DumpMaster(master.Master):

    def __init__(
        self,
        options: options.Options,
    ) -> None:
        super().__init__(options)
        self.errorcheck = ErrorCheck()
        self.addons.add(*addons.default_addons())
        # todo add addons
        self.addons.add(Addons())
