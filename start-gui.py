# coding:utf-8

import os
from time import sleep
from tkinter import *
import configparser
from function import Function


class StartDouyin:
    def __init__(self, master):
        self.fun = Function()
        self.cf = configparser.ConfigParser()
        self.root = master
        self.root.title('Reptile Douyin')
        self.root.resizable(width=False, height=False)
        width = 500
        height = 180
        self.root.geometry('%dx%d' % (width, height))
        self.create_window()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)  # 协议，处理与Windows的互动

    def create_window(self):
        frameTitle = Frame(self.root, bg='lightyellow', width=480, height=50)
        frameTitle.place(x=10, y=0)
        frameTitle.pack_propagate(0)
        Label(frameTitle, text='Reptile Douyin Video', font=('"Helvetica', 15), bg='lightyellow').place(x=150, y=10)

        frame1 = Frame(self.root, width=480, height=30)
        frame1.place(x=20, y=60)

        Label(frame1, text='循环次数：').place(x=0, y=0)

        self.entry_num = Entry(frame1)
        self.entry_num.place(x=80, y=0)

        Label(frame1, text='*默认为0无限循环', font='Arial 8', fg='blue').place(x=300, y=0)

        frame2 = Frame(self.root, width=480, height=30)
        frame2.place(x=20, y=100)
        Button(frame2, text='开始REPTILE', width=20, command=self.reptileStart).place(x=50, y=0)
        Button(frame2, text='停止', width=20, command=self.reptileStop).place(x=250, y=0)

        frame3 = Frame(self.root, width=480, height=40, bg="lightblue")
        frame3.place(x=10, y=140)
        Label(frame3, text='请手动运行mitmdump -s addons.py(绝对路径)', font='Arial 8', fg='red', bg='lightblue').place(x=100, y=10)


    def reptileStop(self):
        """
        点击停止按钮事件
        :return:
        """
        self.fun.write_file('LOOP', 'is_stop', 'ok')

    def reptileStart(self):
        """
        点击开始爬取视频按钮事件
        启动时命令行运行mitmdump、appium
        :return:
        """
        # os.popen('mitmdump -s {}'.format(os.path.join(os.path.dirname(__file__), 'addons.py')))       #运行mitmdump报错，还未找到原因，请手动启动mitmdump

        os.popen('appium -a 127.0.0.1 -p 4723 --session-override')
        sleep(10)  # 等待服务启动

        if not self.entry_num.get() == '':
            self.fun.write_file('LOOP', 'num', self.entry_num.get())
        from douyinswipe import Douyin
        Douyin().main()  # 开始执行手机滑动

    def on_closing(self):
        """
        关闭窗口事件
        :return:
        """
        self.fun.write_file('LOOP', 'is_stop', 'no')
        self.fun.write_file('LOOP', 'num', '0')
        self.root.destroy()  # 摧毁所有窗口


if __name__ == '__main__':
    root = Tk()
    StartDouyin(root)
    root.mainloop()
