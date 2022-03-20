import tkinter as tk
from tkinter import Tk
from loguru import logger

from gui.about_frame import about_frame
from gui.main_frame import main_frame
from gui.save_frame import save_frame
from gui.search_frame import search_frame
from myutil import global_var as gl
from myutil.mysql_diver import mysql_diver
from myutil.tools_function import resource_path


class main_page:
    def __init__(self, master: Tk):
        self.root = master
        self.root.title("密码管理器")
        # 大小为300*300，距离屏幕左边的宽200，距离屏幕顶部的高200
        self.root.geometry("300x300+200+200")
        self.root.iconbitmap(resource_path('resources/icon/探测声音.ico'))  # 添加图标文件

        # 初始化导航栏
        self.setup_menu_bar()

        # 变量
        self.sqlite: mysql_diver = gl.get_value("sqlite")
        self.is_login = tk.BooleanVar()
        self.is_login.set(False)

        # 变量-不同的界面
        self.main_frame = main_frame(self.root)
        self.save_frame = save_frame(self.root)
        self.search_frame = search_frame(self.root)
        self.about_frame = about_frame(self.root)
        self.main_frame.pack()  # 默认显示主页

    def setup_menu_bar(self):
        # 菜单导航栏
        menu_bar = tk.Menu()

        # 新建一个开始子菜单
        start_menu = tk.Menu(menu_bar, tearoff=False)
        start_menu.add_command(label="主页", command=self.main_interface)
        menu_bar.add_cascade(label="开始", menu=start_menu)  # 添加子菜单

        # 新建一个工具子菜单
        tool_menu = tk.Menu(menu_bar, tearoff=False)
        tool_menu.add_command(label="录入", command=self.save_interface)
        tool_menu.add_separator()  # 添加分隔符号
        tool_menu.add_command(label="查询", command=self.search_interface)
        menu_bar.add_cascade(label="工具", menu=tool_menu)  # 添加子菜单

        # 新建一个关于子菜单
        about_menu = tk.Menu(menu_bar, tearoff=False)
        about_menu.add_command(label="关于", command=self.about_interface)
        menu_bar.add_cascade(label="帮助", menu=about_menu)  # 添加子菜单

        self.root["menu"] = menu_bar

    def main_interface(self):
        logger.info("页面切换-主页界面")
        self.about_frame.pack_forget()
        self.search_frame.pack_forget()
        self.save_frame.pack_forget()
        self.main_frame.pack()

    def check_event(self):
        res = self.sqlite.get_find_list("select * from user")
        if res:
            return True

        # 没有用户
        # 进行第一次注册的窗口
        top = tk.Toplevel()
        top.title("用户注册")
        # 变量
        user_name = tk.StringVar()
        passsword = tk.StringVar()
        reg_status = tk.StringVar()

        frame_1 = tk.Frame(top)
        frame_1.pack(fill=tk.X, side=tk.TOP)
        tk.Label(frame_1, text="用户注册",
                 font=("楷体", 20),  # 设置字体
                 fg="black",  # 字体的颜色
                 ).pack(side=tk.TOP)

        # 创建表单的frame-使用表格布局
        frame_2 = tk.Frame(top)
        frame_2.pack(fill=tk.X, side=tk.TOP)
        tk.Label(frame_2, text="用户名：").grid(row=0, column=0)
        tk.Entry(frame_2, textvariable=user_name).grid(row=0, column=1)
        tk.Label(frame_2, text="密  码：").grid(row=1, column=0)
        tk.Entry(frame_2, textvariable=passsword).grid(row=1, column=1)

        def top_reg_event(event):
            res = self.sqlite.add_one("user", ["user_name", "password"], [user_name.get(), passsword.get()])
            if res:
                top.destroy()
            else:
                reg_status.set("注册失败")

        frame_3 = tk.Frame(top)
        frame_3.pack(fill=tk.X, side=tk.TOP)
        bt = tk.Button(frame_3, text="注册")
        # 按钮绑定
        bt.bind("<Button-1>", top_reg_event)
        bt.pack()

        tk.Label(frame_3, textvariable=reg_status).pack(side=tk.RIGHT)

    def login_event(self):
        # 查询是否有用户注册了
        if not self.check_event():
            # 没有注册，就不用跳出来登录界面了
            return

        # 用户登录的窗口
        top = tk.Toplevel()
        top.title("用户登录")
        # 变量
        user_name = tk.StringVar()
        passsword = tk.StringVar()
        login_status = tk.StringVar()

        frame_1 = tk.Frame(top)
        frame_1.pack(fill=tk.X, side=tk.TOP)
        tk.Label(frame_1, text="用户登录",
                 font=("楷体", 20),  # 设置字体
                 fg="black",  # 字体的颜色
                 ).pack(side=tk.TOP)

        # 创建表单的frame-使用表格布局
        frame_2 = tk.Frame(top)
        frame_2.pack(fill=tk.X, side=tk.TOP)
        tk.Label(frame_2, text="用户名：").grid(row=0, column=0)
        tk.Entry(frame_2, textvariable=user_name).grid(row=0, column=1)
        tk.Label(frame_2, text="密  码：").grid(row=1, column=0)
        tk.Entry(frame_2, textvariable=passsword).grid(row=1, column=1)

        def top_login_event(event):
            res = self.sqlite.get_find_list(
                "select * from user where user_name='{}' and password='{}'".
                    format(user_name.get(), passsword.get()))
            if res:
                self.is_login.set(True)
                top.destroy()
            else:
                login_status.set("登录失败，密码错误")

        frame_3 = tk.Frame(top)
        frame_3.pack(fill=tk.X, side=tk.TOP)
        bt = tk.Button(frame_3, text="确定")
        # 按钮绑定
        bt.bind("<Button-1>", top_login_event)
        bt.pack()

        tk.Label(frame_3, textvariable=login_status).pack(side=tk.RIGHT)

    # 页面切换-保存界面
    def save_interface(self):
        logger.info("页面切换-保存界面")
        if not self.is_login.get():
            # 没有登录，跳转到登录界面
            self.login_event()
            return
        self.about_frame.pack_forget()
        self.search_frame.pack_forget()
        self.main_frame.pack_forget()
        self.save_frame.pack()

    # 页面切换-搜索界面
    def search_interface(self):
        logger.info("页面切换-搜索界面")
        if not self.is_login.get():
            # 没有登录，跳转到登录界面
            self.login_event()
            return
        self.save_frame.pack_forget()
        self.about_frame.pack_forget()
        self.main_frame.pack_forget()
        self.search_frame.pack()

    # 页面切换-关于界面
    def about_interface(self):
        logger.info("页面切换-关于界面")
        self.save_frame.pack_forget()
        self.search_frame.pack_forget()
        self.main_frame.pack_forget()
        self.about_frame.pack()
