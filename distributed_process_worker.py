# worker
import time, queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    print('connect address %s...' % '127.0.0.1:5000')
    manager.connect()

    task = manager.get_task_queue()
    result = manager.get_result_queue()
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d*%d' % (n, n))
            r = '%d*%d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('task queue is empty')
    print('worker exit')
