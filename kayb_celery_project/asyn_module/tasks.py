# -*- coding:utf-8 -*-
# @author: kayb
# @file: tasks.py
# @time: 25/7/20 8:03 AM

import time

from main_celery import app


@app.task(name='demo_task_add')
def add(a, b):
    time.sleep(100)
    result = a + b
    print(result)
    return result


