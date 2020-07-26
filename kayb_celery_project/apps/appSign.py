# -*- coding:utf-8 -*-
# @author: kayb
# @file: appSign.py
# @time: 26/7/20 2:20 AM

from asyn_module.tasks import add


if __name__ == '__main__':

    # 等同于  add.delay(1, 8)
    results = add.s(1, 8).delay()
    print(results)

    # 等同于 add.apply_async((1, 3), countdown=10)
    # results = add.signature((1, 3), countdown=10).apply_async()
    # print(results)

    # 直接在当前进程调用该任务
    # results = add.s(1, 8)()
    # print(results)

    # 链试任务  就是相当于 1+3的结果 再加上10
    # result = add.apply_async((1, 3), link=add.s(10))
    # print(result)

    # 链试任务二 就是相当于 1+3的结果 再加上10  使用指定选项的方式调用
    # result = add.apply_async((1, 3), link=add.signature((10, ), countdown=10))
    # print(result)

    pass

