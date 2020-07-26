# -*- coding:utf-8 -*-
# @author: kayb
# @file: configs.py
# @time: 25/7/20 8:00 AM

#
# backend = "redis://:123@127.0.0.1:6379/0"
# broker = "redis://:123@127.0.0.1:6379/0"

BROKER_URL = 'redis://root:123@localhost:6379/1'
CELERY_RESULT_BACKEND = 'redis://root:123@localhost:6379/0'


