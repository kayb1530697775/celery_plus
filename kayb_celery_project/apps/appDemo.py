# -*- coding:utf-8 -*-
# @author: kayb
# @file: appDemo.py
# @time: 25/7/20 7:53 PM

from datetime import datetime, timedelta

from asyn_module.tasks import *


if __name__ == '__main__':
    # 调用方式一  使用delay
    results = add.delay(1, 2)
    print(results)

    # results = add.s(2,2)()  # 直接在当前进程调用
    # print(results)

    # results = print_time.delay(a=1, b=2)
    # print(results)

    # 调用方式二  使用apply_async   等同于上面方式一
    # results = add.apply_async((1, 4))
    # print(results)

    # 调用方式三  使用apply_async  countdown 倒计时10秒之后开始执行该任务
    # results = add.apply_async((2, 5), countdown=200)
    #print(results.get())
    # print(results)

    # 调用方式四  使用apply_async 指定eta  使用datetime 类型制定
    # 指定固定时间进行执行任务
    # 注意eta为UTC时间 clery启动可以设置时区  但是eta并没有转化  所以如果有这种需求 按照以下方式转化成多少秒后执行该任务
    # now_time = datetime.now()
    # task_start_time = datetime.now() + timedelta(seconds=5)
    # countdown = (task_start_time-now_time).total_seconds()
    # results = add.apply_async((3, 8), countdown=countdown)
    # print(results)

    # 调用方式五 10秒钟后开始执行任务 5秒钟后过期 为了测试 这样调整时间  一般使用到的场景为 比如一定时间后开始执行任务 但是由于任务过多 并没有开始执行 但是过了一定时间就没有必要执行该任务了。
    # result = add.apply_async((4, 11), countdown=10, expires=5)
    # print(result)

    # 调用方式六 目的同调用方式五 参数 expires 为 datetime类型
    # 注意expires 也有时区的问题  如果遇到指定时间过期 则使用同<调用方式四>相同的解决办法
    # result = add.apply_async((11, 23), countdown=10, expires=datetime.now()+timedelta(seconds=5))
    # print(result)


    pass
