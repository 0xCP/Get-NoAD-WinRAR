# Get-NoAD-WinRAR

## 介绍

WinRAR压缩很好用，但是国内版的有弹窗广告  
根据WinRAR吧主的 [帖子](https://tieba.baidu.com/p/6627013006) 里的方法  
制作这个脚本获取无广告版的WinRAR下载地址

## 使用说明

1.先从国内WinRAR [网站](http://www.winrar.com.cn/download.htm) 获取最新版本的版本号，版本号为三位数字。当前最新为600  
2.下载国内版的安装包后右键查看安装包数字签名日期  
图中日期为*20201211*  
![文件数字签名](./img/数字签名.png)  
3.克隆本仓库  
`git clone https://gitee.com/n233333/get-noad-rar.git`

进入项目目录  
`cd get-noad-rar`

安装依赖  
`pip install -r requirements.txt`

启动脚本  
`python main.py`
![运行截图](./img/运行截图.gif)

## 已知版本下载地址

* 版本：600 日期：20201211  [64位][winrar600-64] [32位][winrar600-32]
* 版本：591 日期：20200827  [64位][winrar591-64] [32位][winrar591-32]

[winrar600-64]:https://www.win-rar.com/fileadmin/winrar-versions/sc/sc20201210/rrlb/winrar-x64-600sc.exe

[winrar600-32]:https://www.win-rar.com/fileadmin/winrar-versions/sc/sc20201210/rrlb/wrar600sc.exe

[winrar591-64]:https://www.win-rar.com/fileadmin/winrar-versions/sc/sc20200827/rrlb/winrar-x64-591sc.exe

[winrar591-32]:https://www.win-rar.com/fileadmin/winrar-versions/sc/sc20200827/rrlb/wrar591sc.exe
