# master
import time, random, queue
from multiprocessing.managers import BaseManager


task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


if __name__ == '__main__':
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(10):
        n = random.randint(0, 10000)
        print('put task %s' % n)
        task.put(n)
        time.sleep(1)

    print('try get result...')

    time.sleep(10)
    for i in range(10):
        try:
            r = result.get(timeout=10)
            print('result:%s' % r)
            time.sleep(1)
        except queue.Empty:
            print('result queue is empty')

    manager.shutdown()
    print('master exit')
