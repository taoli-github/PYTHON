# _*_ coding:utf-8 _*_
import os, time, random
from multiprocessing import Process, Queue


def p_read(q):
    print('read process is %s' % os.getpid())
    while True:
        val = q.get(True)
        print('Get %s from queue' % val)


def p_write(q):
    print('write process is %s' % os.getpid())
    for val in ['a', 'b', 'c']:
        print('put %s to queue.' % val)
        q.put(val)
        time.sleep(random.random()*10)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=p_write, args=(q, ))
    pr = Process(target=p_read, args=(q, ))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
