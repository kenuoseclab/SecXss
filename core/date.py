#!/usr/bin/env python
# encoding: utf-8
"""
@author: sys71m
@contact: sys71m@163.com
@software: pycharm
@file: date.py
@desc:
"""
import threading
from queue import Queue
from core.log import setup_logger


logger = setup_logger(__name__)
flow_queue = Queue()
running_process = Queue()
conf = dict()
thread_lock = threading.Lock()
