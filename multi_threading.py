# 多线程 threading
import threading
from atexit import register
from time import sleep, ctime


loops = [2, 1]


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.func = func
        self.name = name
        self.args = args

    def __call__(self):
        self.func(*self.args)


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.name = name
        self.args = args

    def run(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop %s, at: %s' % (nloop, ctime()))
    sleep(nsec)
    print('\t loop %s, done at: %s' % (nloop, ctime()))


def main():
    print('main thread starts at: %s' % ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        # t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()


class CleanOutput(set):
    def __str__(self):
        return ','.join(x for x in self)


@register
def _atexit():
    print('all threads done, %s' % ctime())


if __name__ == '__main__':
    main()
