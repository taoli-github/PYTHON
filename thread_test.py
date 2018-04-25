# _*_ coding:utf-8 _*_
import time, threading
import multiprocessing


# def loop():
#     print('thread %s is running ... ...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         print('%s >> %s' % (threading.current_thread().name, n+1))
#         n = n+1
#         time.sleep(0.5)
#     print('thread %s ended' % threading.current_thread().name)
#
#
# print('thread %s is running ... ...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended' % threading.current_thread().name)


# balance = 0
# lock = threading.Lock()
#
#
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
#
#
# def run_thread(n):
#     for i in range(1000000):
#         lock.acquire()
#         try:
#             change_it(n)
#         finally:
#             lock.release()
#
#
# t1 = threading.Thread(target=run_thread, args=(5, ))
# t2 = threading.Thread(target=run_thread, args=(8, ))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)


def loop():
    x = 0
    while True:
        x = x ^ 1
        print(x)


# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()

# ThreadLocal

local_sch = threading.local()


def process_std():
    std = local_sch.student
    print('I am %s in %s' % (std, threading.current_thread().name))


def process_thread(name):
    local_sch.student = name
    process_std()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 多任务 Master-Worker  Master:分配任务  Worker: 执行任务


