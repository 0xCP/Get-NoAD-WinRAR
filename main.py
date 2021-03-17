import requests
import re
from datetime import datetime
from datetime import timedelta


# a = datetime.strptime(str(datastr), '%Y%m%d')

# url = 'https://www.win-rar.com/fileadmin/winrar-versions/sc/sc20201211/rrlb/wrar600sc.exe'
# my_proxies = {"http": "socks5h://127.0.0.1:7890", "https": "socks5h://127.0.0.1:7890"}
# r = requests.get(url=url, proxies=my_proxies, timeout=5)
# r = requests.get(url=url, proxies=None, timeout=5)
# print(r.status_code)

def input_ver():
    while True:
        ver = input('输入版本号[571]：')
        if re.match('^\\d{3}$', ver):
            break
        else:
            print('输入格式有误，应该为三位数字')
    return ver


def input_date():
    while True:
        datestr = input('输入国内版数字签名日期[20190509]：')
        if re.match('^\\d{8}$', datestr):
            try:
                date = datetime.strptime(str(datestr), '%Y%m%d')
            except ValueError:
                print('输入的日期有误')
            else:
                return date
        else:
            print('输入格式有误,应该为8位数字。')


def input_proxies():
    while True:
        proxy = input('是否使用代理[y/n]：')
        proxy = proxy.lower()
        if not re.match('^(y|n)$', proxy):
            print('输入有误，只能输入y或者n')
            continue
        if proxy == 'n':
            return ''
        print('HTTP代理格式：http://user:pass@host:port\nSOCK代理格式：socks5://user:pass@host:port')
        while True:
            proxy = input('输入代理链接')
            proxies = {
                'http': proxy,
                'https': proxy
            }
            r = requests.get(url='http://connect.rom.miui.com/generate_204', proxies=proxies, timeout=5)
            if not r.status_code == 204:
                print('代理无效')
            else:
                return proxies


if __name__ == '__main__':
    print('使用说明请查看 https://gitee.com/n233333/get-noad-rar')
    ver = input_ver()
    date = input_date()
    proxies = input_proxies()
    print('\n')
    print('开始测试')
    if int(ver) >= 580:
        maxdate = date + timedelta(days=10)
        mindate = date - timedelta(days=10)
        while True:
            url = 'https://www.win-rar.com/fileadmin/winrar-versions/sc/sc' + maxdate.strftime(
                '%Y%m%d') + '/rrlb/winrar-x64-' + ver + 'sc.exe'
            print('测试:' + url, end='  ')
            if proxies:
                r = requests.get(url=url, proxies=proxies, timeout=5)
            else:
                r = requests.get(url=url, proxies=None, timeout=5)
            print(r.status_code)
            if r.status_code == 200:
                print('\n\n成功获取到WinRAR%s版本的下载地址\n%s' % (ver, url))
                break
            maxdate -= timedelta(days=1)
            if maxdate < mindate:
                break
    else:
        pass
