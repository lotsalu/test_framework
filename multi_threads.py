# coding=utf-8
#测试utf-8编码
from functools import partial
from multiprocessing.pool import Pool
from single import *
from time import time
import util

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def main():
    tables = util.excel_table_byindex()
    ts = time()
    nums = getNums(30)
    p = Pool(len(tables))
    p.map(processNum, nums)
    print("cost time is: {:.2f}s".format(time() - ts))
    p.close()
    sleep(1)
    print "---------------------------"


if __name__ == "__main__":
    main()