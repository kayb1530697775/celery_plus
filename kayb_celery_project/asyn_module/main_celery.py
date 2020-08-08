# -*- coding:utf-8 -*-
# @author: kayb
# @file: main_celery.py
# @time: 25/7/20 8:00 AM


from celery import Celery
from celery.signals import after_task_publish, before_task_publish, task_prerun, task_postrun, task_failure, task_internal_error, setup_logging

from configs import *



"""
回调任务的方法可用作记录任务的发布记录日志等(个人理解)

注意发布前后回调的方法是在发布者的位置执行

任务执行前或者执行后的方法实在执行单元执行


"""


@after_task_publish.connect(sender="demo_task_add")  # sender参数可以 使处理的函数发布demo_task_add该任务时执行
def task_sent_handler_after(sender=None, headers=None, body=None, **kwargs):
    """
    发布任务之后回调的方法
    :param sender:
    :param headers:
    :param body:
    :param kwargs:
    :return:
    """
    # print("after_task_publish ...")
    # print("sender", sender)
    # print("headers", headers)
    # print("body", body)
    # print(kwargs)
    pass

@before_task_publish.connect
def task_sent_handler_before(sender=None, headers=None, body=None, **kwargs):
    """
    发布任务之前回调方法  注意
    :param sender:
    :param headers:
    :param body: body里面包含传递的参数
    :param kwargs:
    :return:
    """
    # print("task_sent_handler_before ...")
    # print("sender", sender)
    # print("headers", headers)
    # print("body", body)
    # print(kwargs)
    pass


@task_prerun.connect
def app_task_prerun(task_id, task, *args, **kwargs):
    """
    执行单元在任务执行之前执行该方法
    :param task_id:
    :param task:
    :param args:
    :param kwargs:
    :return:
    """
    print('app_task_prerun')
    print("task_id", task_id)
    print("task", task)
    print("args", args)
    print("kwargs", kwargs)


@task_postrun.connect
def app_task_postrun(task_id, task, retval, *args, **kwargs):
    """
    执行单位在执行任务之后执行该方法  出现异常也会执行该方法
    :param task_id:
    :param task:
    :param args:
    :param kwargs:
    :return:
    """
    print('app_task_postrun')
    print("task_id", task_id)
    print("task", task)
    print("retval", retval)  # 运行结果
    print("args", args)
    print("kwargs", kwargs)


# 'task_id', 'exception', 'args', 'kwargs', 'traceback', 'einfo'
@task_failure.connect
def app_task_failure(task_id, exception, traceback, einfo, *args, **kwargs):
    """
    任务执行失败的时候 执行该方法
    :param task_id:
    :param task:
    :param args:
    :param kwargs:
    :return:
    """
    print('app_task_failure')
    print("task_id", task_id)
    print("exception", exception)
    print("traceback", traceback)  # 运行结果
    print("einfo", einfo)
    print("args", args)
    print("kwargs", kwargs)


# 'task_id', 'args', 'kwargs', 'request', 'exception', 'traceback', 'einfo'
@task_internal_error.connect
def app_task_internal_error(task_id, request,  exception, traceback, einfo, *args, **kwargs):
    """

    :param task_id:
    :param task:
    :param args:
    :param kwargs:
    :return:
    """
    print('app_task_internal_error')
    print("task_id", task_id)
    print("request", request)
    print("exception", exception)
    print("traceback", traceback)  # 运行结果
    print("einfo", einfo)
    print("args", args)
    print("kwargs", kwargs)



app = Celery(
    main="kayb",
    include="tasks"  # 添加任务到任务注册表  也可以以列表形式导入 ['a.b', 'a.c']
)

# 导入配置文件
app.config_from_object('configs')

app.conf.timezone = "Asia/Shanghai"


if __name__ == '__main__':
    app.start()


