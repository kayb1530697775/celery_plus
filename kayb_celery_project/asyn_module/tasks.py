# -*- coding:utf-8 -*-
# @author: kayb
# @file: tasks.py
# @time: 25/7/20 8:03 AM

import time

from main_celery import app


@app.task(name='demo_task_add')
def add(a, b):
    result = a + b
    print(result)
    time.sleep(10)
    return result


@app.task(name="print_demo_add")
def print_time(a, b):

    print(time.time(), a)
    print(time.time(), b)
    return a+b

