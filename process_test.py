from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s(%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s runs %.2f' % (name, end-start))


if __name__ == '__main__':
    print('parent process %s.' % os.getpid())
    p = Pool(5)
    for i in range(5):
        p.apply_async(func=long_time_task, args=(i,))
    print('waiting for subprocess done')
    p.close()
    p.join()
    print('all subprocess done')

