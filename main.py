import requests
import re
from datetime import datetime
from datetime import timedelta
from urllib3.exceptions import ProxySchemeUnknown


def input_ver():
    while True:
        _ver = input('输入版本号[571]：')
        if re.match('^\\d{3}$', _ver):
            return _ver
        else:
            print('输入格式有误，应该为三位数字')


def input_date():
    while True:
        datestr = input('输入国内版数字签名日期[20190509]：')
        if re.match('^\\d{8}$', datestr):
            try:
                _date = datetime.strptime(str(datestr), '%Y%m%d')
            except ValueError:
                print('输入的日期有误')
            else:
                return _date
        else:
            print('输入格式有误,应该为8位数字。')


def input_proxies():
    while True:
        proxy = input('是否使用代理[y/n]：')
        proxy = proxy.lower()
        if not re.match('^y|n$', proxy):
            print('输入有误，只能输入y或者n')
            continue
        if proxy == 'n':
            return ''
        print('HTTP代理格式：http://user:pass@host:port\nSOCK代理格式：socks5://user:pass@host:port')
        while True:
            proxy = input('输入代理链接')
            _proxies = {
                'http': proxy,
                'https': proxy
            }
            print('测试代理有效性')
            try:
                _r = requests.get(url='http://connect.rom.miui.com/generate_204', proxies=_proxies, timeout=5)
            except ProxySchemeUnknown as e:
                print('不支持的代理类型', end='')
                print(e)
                continue
            except ConnectionError as e:
                print('连接错误', end='')
                print(e)
                continue
            else:
                if not _r.status_code == 204:
                    print('代理无效')
                    continue
                else:
                    print('代理有效')
                    return _proxies


if __name__ == '__main__':
    print('使用说明请查看 https://gitee.com/n233333/get-noad-rar')
    ver = input_ver()
    date = input_date()
    proxies = input_proxies()
    print('\n开始测试')
    maxdate = date + timedelta(days=3)
    mindate = date - timedelta(days=20)
    while True:
        if int(ver) >= 580:
            url = 'https://www.win-rar.com/fileadmin/winrar-versions/sc/sc' + maxdate.strftime(
                '%Y%m%d') + '/rrlb/winrar-x64-' + ver + 'sc.exe'
        else:
            url = 'https://www.win-rar.com/fileadmin/winrar-versions/sc' + maxdate.strftime(
                '%Y%m%d') + '/wrr/winrar-x64-' + ver + 'sc.exe'
        print('测试:' + url, end='  ')
        if proxies:
            r = requests.get(url=url, proxies=proxies, timeout=5)
        else:
            r = requests.get(url=url, proxies=None, timeout=5)
        print(r.status_code)
        if r.status_code == 200:
            if int(ver) >= 580:
                url_64 = 'https://www.win-rar.com/fileadmin/winrar-versions/sc/sc' + maxdate.strftime(
                    '%Y%m%d') + '/rrlb/winrar-x64-' + ver + 'sc.exe'
                url_32 = 'https://www.win-rar.com/fileadmin/winrar-versions/sc/sc' + maxdate.strftime(
                    '%Y%m%d') + '/rrlb/wrar' + ver + 'sc.exe'
            else:
                url_64 = 'https://www.win-rar.com/fileadmin/winrar-versions/sc' + maxdate.strftime(
                    '%Y%m%d') + '/wrr/winrar-x64-' + ver + 'sc.exe'
                url_32 = 'https://www.win-rar.com/fileadmin/winrar-versions/sc' + maxdate.strftime(
                    '%Y%m%d') + '/wrr/wrar' + ver + 'sc.exe'
            print('\n成功获取到WinRAR%s版本的下载地址\n\n32位：%s\n64位：%s' % (ver, url_32, url_64))
            break
        maxdate -= timedelta(days=1)
        if maxdate < mindate:
            break
        continue
