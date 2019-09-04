#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'a test module'

__author__='ANPAN'

import sys

def test():
    args=sys.argv
    if len(args)==1:
        print('Hello,World!')
    elif len(args)==2:
        print('Hello,%s'% args[2])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

'''
作用域
函数与变量的作用域测试
Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
'''

def _private_1(name):
    print('Hello,%s'% name)
def _private_2(name):
    print('Hi,%s'% name)
def greeting(name):
    if len(name)>3:
        return _private_1(name)
    else:
        return _private_2(name)