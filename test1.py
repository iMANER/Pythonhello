#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 分布式: master
import random, queue
# managers子模块支持把多进程分布到多台机器上
from multiprocessing.managers import BaseManager

# 发送任务的队列
task_queue = queue.Queue()
# 接收结果的队列
result_queue = queue.Queue()

# 从BashManager继承
class QueueManager(BaseManager):
    pass

# 1. 把两个Queue都注册到网络上, callable关联queue对象
def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

def test():
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)
    # 2. 绑定端口, 设置验证码
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 3. 启动Queue
    manager.start()

    # 4. 通过网络获得Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 5. 放置任务
    for i in range(10):
        n = random.randint(0, 1000)
        print('Put task %d...' % n)
        task.put(n)
    # 6. 获取结果
    print('Try get result...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)

    # 7. Close
    manager.shutdown()
    print('********* Master exit *********')

if __name__  == '__main__':
    test()