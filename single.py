# coding=utf-8
# 测试utf-8编码
from time import sleep, time
import sys, threading
import util

from requests_demo import login_func

reload(sys)
sys.setdefaultencoding('utf-8')


def getNums(N):
    return xrange(N)


# def processNum(num):
#     num_add = num + 1
#     sleep(1)
#     print "aaaaaaaaaaaaaaaaaaaaaaaaaa"
#     tables = util.excel_table_byindex()
#     for row in tables:
#         r = login_func("172.31.3.73:6020", str(row["teaname"]), str(row["code"]), str(row["pass"]))
#         print type(row["teaname"]), row["code"], row["pass"]
#         print r.content
#     print str(threading.current_thread()) + ": " + str(num) + " → " + str(num_add)
def processNum(num):
    tables = util.excel_table_byindex()
    for index in range(len(tables)):
        num_add = index + 1
        sleep(1)
        print "aaaaaaaaaaaaaaaaaaaaaaaaaa"
        tables = util.excel_table_byindex()
    # tables[index]
        r = login_func("172.31.3.73:6020", str(tables[index]["teaname"]), str(tables[index]["code"]),
                   str(tables[index]["pass"]))
        print type(tables[index]["teaname"]), tables[index]["code"], tables[index]["pass"]
        print r.content
        print str(threading.current_thread()) + ": " + str(index) + " → " + str(num_add)


if __name__ == "__main__":
    t1 = time()
    for i in getNums(1):
        processNum(1)

    print "cost time is: {:.2f}s".format(time() - t1)
