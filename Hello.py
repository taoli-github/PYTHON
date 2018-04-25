#! user/bin/env python3
# _*_ coding:utf-8 _*_


# 'a test model'

__author__ = 'litao'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello %s' % args[1])
    else:
        print('many args')


if __name__ == '__main__':
    test()
