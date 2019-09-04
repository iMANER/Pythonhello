import time,random,queue
from multiprocessing.managers import BaseManager
'''
分布式进程
进程和处理任务的进程分布到两台机器上，通过managers模块把Queue通过网络暴露
'''
def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

#发送任务的队列
task_queue=queue.Queue()

#接受结果的队列
result_queue=queue.Queue()

#从BaseManager继承QueueManager
class QueueManager(BaseManager):
    pass
def freeze_support():
    # 把两个Queue都注册到网络上，callable参数关联Queue对象
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # 绑定端口5000和设置验证码
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    # 启动queue
    manager.start()

    # 获得通过网络访问的对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放置任务
    for i in range(1000):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    print('Try get results...')
    for i in range(1000):
        r = result.get(timeout=10)  # 可选的timeout参数不填时将一直阻塞直到获得锁定,Queue.get([block[, timeout]])获取队列，timeout等待时间
        print('Result:%s' % r)

    # 关闭
    manager.shutdown()
    print('master exit')

if __name__ == '__main__':
    freeze_support()
