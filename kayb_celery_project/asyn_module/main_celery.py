# -*- coding:utf-8 -*-
# @author: kayb
# @file: main_celery.py
# @time: 25/7/20 8:00 AM


from celery import Celery
from configs import *


app = Celery(
    main="kayb",
    include="tasks"  # 添加任务到任务注册表  也可以以列表形式导入 ['a.b', 'a.c']
)

# 导入配置文件
app.config_from_object('configs')

app.conf.timezone = "Asia/Shanghai"


if __name__ == '__main__':
    app.start()


