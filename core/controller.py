#!/usr/bin/env python
# encoding: utf-8
"""
@author: sys71m
@contact: sys71m@163.com
@software: pycharm
@file: controller.py
@desc:
"""
import time
import threading
from core.date import conf
from core.mitmproxy import mitmdump
from core.date import logger, flow_queue, thread_lock
from config import listen_host, listen_port, thread_numbers


def start_scan():
    for number in range(conf["thread_numbers"]):
        scanner = threading.Thread(target=scan_task)
        scanner.setDaemon(True)
        scanner.start()


def scan_task():
    while True:
        flow = flow_queue.get()
        thread_lock.acquire()
        print(">>" + flow.url)
        print(">>" + flow.method)
        thread_lock.release()


def start_proxy():
    scanner = threading.Thread(target=start_scan)
    scanner.setDaemon(True)
    scanner.start()
    args = ['--listen-host', conf["host"], '--listen-port', str(conf["port"])]
    logger.info("server listening at http://{}:{}".format(conf["host"], str(conf["port"])))
    mitmdump(args)


def init_conf():
    conf["host"] = listen_host
    conf["port"] = listen_port
    conf["thread_numbers"] = thread_numbers
