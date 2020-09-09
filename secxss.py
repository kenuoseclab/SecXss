#!/usr/bin/env python
# encoding: utf-8
"""
@author: sys71m
@contact: sys71m@163.com
@software: pycharm
@file: secxss.py
@desc:
"""
import sys
from core.date import logger
from core.controller import start_proxy, start_scan, init_conf


def check_version():
    if sys.version.split()[0] < "3.6":
        logger.error(
            "incompatible Python version detected ('{}'). you need python version >= 3.6".format(
                sys.version.split()[0]))
        sys.exit()


if __name__ == "__main__":
    check_version()
    init_conf()
    start_scan()
    start_proxy()

