import requests
import re
import json
from datetime import datetime
from datetime import timedelta

# a = datetime.strptime(str(datastr), '%Y%m%d')

# url = 'https://www.win-rar.com/fileadmin/winrar-versions/sc/sc20201211/rrlb/wrar600sc.exe'
# my_proxies = {"http": "socks5h://127.0.0.1:7890", "https": "socks5h://127.0.0.1:7890"}
# r = requests.get(url=url, proxies=my_proxies, timeout=5)
# r = requests.get(url=url, proxies=None, timeout=5)
# print(r.status_code)
if __name__ == '__main__':
    print('使用说明请查看 https://gitee.com/n233333/get-noad-rar')
    while True:
        ver = input('输入版本号[571]：')
        if re.match('^\\d{3}$', ver):
            break
        else:
            print('输入格式有误')

    while True:
        datestr = input('输入国内版数字签名日期[20190509]：')
        if re.match('^\\d{8}$', datestr):
            try:
                date = datetime.strptime(str(datestr), '%Y%m%d')
            except ValueError:
                print('输入的日期有误')
            else:
                break
        else:
            print('输入格式有误')

    while True:
        proxy = input('是否使用代理[y/n]：')
        proxy = proxy.lower()
        if re.match('^(y|n)$', proxy):
            break
        else:
            print('输入有误')

    print('开始测试')
    print(ver, date.strftime('%Y%m%d'))