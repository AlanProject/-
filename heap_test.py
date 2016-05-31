#!/usr/bin/env python
#-*- coding:utf-8 -*-



#构建构建大顶堆


def big_heap(argv):
    for i in range(len(argv)//2, 0, -1):
        print argv[i],i


if __name__ == '__main__':

    l = [26, 5, 77, 1, 61, 11, 59, 15, 48, 19, 10, 13, 33]

    big_heap(l)