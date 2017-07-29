'''
Python支持多种图形界面的第三方库，包括：
Tk
wxWidgets
Qt
GTK
等等。
但是Python自带的库是支持Tk的Tkinter，使用Tkinter，无需安装任何包，就可以直接使用。
'''

'''
第一步是导入Tkinter包的所有内容：
'''

from tkinter import *
from . import PIL_T

import tkinter.messagebox as messagebox


'''
    ============== Hello World !==============
'''

'''
第二步是从Frame派生一个Application类，这是所有Widget的父容器：
'''


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text="Hello Word !")
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()

        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'World'
        messagebox.showinfo('Message', 'Hello, %s' % name)


'''
第三步，实例化Application，并启动消息循环：
'''
app = Application()

# 设置窗口标题
app.master.title('Hello World')
# 住消息循环
app.mainloop()


'''
    =============== 输入文本 =============
'''



