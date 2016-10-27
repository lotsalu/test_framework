# coding=utf-8
import requests

def req_post(url, headers, data):
    r = requests.post(url=url, headers=headers, data=data)

    # print "status_code" + r.status_code, "headers" + r.headers, "content" + r.content
    return r

def login_func( host, tenantname, code, password):
    url = "http://" + host + '/portal/logon.action'
    print url
    headers = {
        "Connection": "keep-alive",
        "Referer": "http://" + host + "/layout_new/login.jsp?url=" + "http://" + host + "/layout_new/login.html",
        "Accept-Language": "zh-CN",
        "x-requested-with": "XMLHttpReques",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        "Pragm": "=no-cache",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; InfoPath.3)",
        "Content-Length": "195",
        "Host": host
    }
    data = {
        # "identifiers.src": "waiqin365",
        "identifiers.password": password,
        # "refer": "http://172.31.3.73:6020/layout_new/login.html",
        # "identifiers.type": "1",
        "identifiers.tenantname": tenantname,
        "identifiers.code": code
    }
    # def req(self, method, url, headers, data):
    # pf = public_function
    r = req_post(url, headers, data)
    print r.status_code
    print r.content
    return r

if __name__ == '__main__':
    login_func("172.31.3.73:6020", "ywcsb", "zhouyong", "a111111")