# _*_ coding:utf-8 _*_
import urllib.request as request
import os
import base64
import urllib.parse as parser
import threading
import multiprocessing
import json
from time import sleep, ctime


def main():
    organization_id = 531

    # region 服务器链接信息
    pic_server_add = '116.62.58.203'
    pic_server_user = 'mbglyyser'
    pic_server_password = 'mbglp@ssw0rd'
    pic_dir = r'E:\apache-tomcat-7.0.52-ncdms\webapps\ncdms\upload\hbpCustomerMainHead'
    # endregion

    list_dir = os.listdir(r'G:\PersonPictures')
    print(ctime())
    for pid_path in list_dir:
        pic_full_path = r'G:/PersonPictures/' + pid_path

        pic_base64_str = ''
        with open(pic_full_path, 'rb') as f:
            pic_base64_str = base64.b64encode(f.read())

        #region base64str
        img_2 = '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'
        # endregion
        face_recgonization(pic_base64_str, img_2)

    print(ctime())


def face_recgonization(pic_base64_str, img_2):
    print('rec start:%s' % ctime())
    data = {'image_base64_1': pic_base64_str, 'image_base64_2': img_2}
    url_params = parser.urlencode(data).encode('utf-8')
    url = 'http://ncd.bailingjk.com:20085/ncdms-third-web/faceRec/FaceCompare.html'

    req = request.Request(url, data=url_params)

    with request.urlopen(req) as f:
        similarity = f.read().decode('utf-8')

    print('rec end at:%s' % ctime())
    return similarity


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.name = name
        self.args = args

    def run(self):
        self.func(*self.args)


def thread_test(pic_path, img_2):

    with open(pic_path, 'rb') as f:
        pic_base64_str = base64.b64encode(f.read())

    similarity = face_recgonization(pic_base64_str, img_2)
    print('%s,similarity:%s' % (pic_path, similarity))


def task():
    print(ctime())
    with open(r'd:\2.jpg', 'rb') as f:
        img_2 = base64.b64encode(f.read())

    list_dir = os.listdir(r'G:\PersonPictures')

    nloops = len(list_dir)

    threads = []
    for i in range(nloops):
        full_path = r'G:\\PersonPictures\\' + list_dir[i]
        t = MyThread(thread_test, (full_path, img_2), thread_test.__name__)
        threads.append(t)

    for i in range(nloops):
        threads[i].start()

    for i in range(nloops):
        threads[i].join()

    print(ctime())


lock = multiprocessing.Lock()


def a(x):
    lock.acquire()
    print('县城%s 启动' % os.getpid())
    lock.release()

    with open(x, 'rb') as f:
        pic_base64_str = base64.b64encode(f.read())

    similarity = face_recgonization(pic_base64_str, img_22)
    print('%s,similarity:%s' % (x, similarity))

    lock.acquire()
    print('县城%s 结束' % os.getpid())
    lock.release()


def process_test():

    list_dir = ['G:\\PersonPictures\\' + x for x in os.listdir(r'G:\PersonPictures')]

    process_pool = multiprocessing.Pool(4)

    print(ctime())
    process_pool.map(a, list_dir)
    print(ctime())

#
# img_22 = ''
# with open(r'd:\2.jpg', 'rb') as f:
#     img_22 = base64.b64encode(f.read())


def get_segment(sentence):

    url = 'http://10.68.4.55:10321/segment?sentence2=' + parser.quote(sentence)
    with request.urlopen(url) as f:
        res = str(f.read(), encoding='utf-8').encode('utf-8').decode('unicode_escape')
    for r in json.loads(res):
        print(r)


def post_segment(setence):
    """
    jieba
    :return:
    """
    data = {'sentence': ''+ setence + ''}
    url_params = parser.urlencode(data).encode('utf-8')
    url = 'http://10.68.4.53:8228/segment/'

    req = request.Request(url, data=url_params)

    with request.urlopen(req) as f:
        similarity = f.read()
    print(str(base64.decodebytes(similarity), encoding='utf-8'))


if __name__ == '__main__':

    # 进程执行
    # process_test()

    # 线程
    # task()
    # 串行
    # main()
    sentence = '干哕,纳差，肚子疼，拉肚子，乏力心慌,手抖，闹肚子，干呕，拉稀，打喷嚏，流鼻涕,' \
               ',食欲减退,上腹部不适、腹胀'
    get_segment(sentence)
    post_segment(sentence)
