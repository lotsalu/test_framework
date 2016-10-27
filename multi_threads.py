# coding=utf-8
#测试utf-8编码
from functools import partial
from multiprocessing.pool import Pool
from single import *
from time import time

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    ts = time()
    nums = getNums(1000)
    p = Pool(100)
    p.map(processNum, nums)
    print("cost time is: {:.2f}s".format(time() - ts))
    sleep(1)
    print "---------------------------"


if __name__ == "__main__":
    main()