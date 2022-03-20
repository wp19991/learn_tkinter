import tkinter as tk
from tkinter.ttk import Combobox

from loguru import logger

from myutil import global_var as gl
from myutil.mysql_diver import mysql_diver


class search_frame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        # 变量
        self.sqlite: mysql_diver = gl.get_value("sqlite")
        self.web_name = self.sqlite.get_find_list("select web_name from web_password")
        self.web_combox = None
        self.web_name_var = tk.StringVar()
        if self.web_name:
            self.web_name_var.set(self.web_name[0][0])
        self.account_var = tk.StringVar()
        self.password_var = tk.StringVar()

        self.setup_ui()

    def setup_ui(self):
        # 用frame来框住布局-使用相对布局
        # pack 有 fill 和 side 参数
        frame_1 = tk.Frame(self)
        frame_1.pack(fill=tk.X, side=tk.TOP)
        tk.Label(frame_1, text="查询网站信息",
                 font=("楷体", 20),  # 设置字体
                 fg="black",  # 字体的颜色
                 ).pack(side=tk.TOP)
        self.web_combox = Combobox(frame_1, textvariable=self.web_name_var, values=self.web_name)
        self.web_combox.config(justify=tk.CENTER)  # 设置居中
        self.web_combox.pack(side=tk.TOP)

        # 创建表单的frame-使用表格布局
        frame_2 = tk.Frame(self)
        frame_2.pack(fill=tk.X, side=tk.TOP)
        tk.Label(frame_2, text="网站：").grid(row=0, column=0)
        tk.Entry(frame_2, textvariable=self.web_name_var).grid(row=0, column=1)
        tk.Label(frame_2, text="账号：").grid(row=1, column=0)
        tk.Entry(frame_2, textvariable=self.account_var).grid(row=1, column=1)
        tk.Label(frame_2, text="密码：").grid(row=2, column=0)
        tk.Entry(frame_2, textvariable=self.password_var).grid(row=2, column=1)

        # 创建表单的frame
        frame_3 = tk.Frame(self)
        frame_3.pack(fill=tk.X, side=tk.TOP)
        tk.Button(frame_3, text="查询", command=self.search_info_event).pack(side=tk.LEFT)
        tk.Button(frame_3, text="刷新", command=self.reload_info_event).pack(side=tk.RIGHT)

    def search_info_event(self):
        logger.info("查询信息")
        res = self.sqlite.get_find_list(
            "select web_name,account,password from web_password where web_name='{}'".format(self.web_name_var.get()))
        if res is None:
            return
        self.account_var.set(res[0][1])
        self.password_var.set(res[0][2])

    def reload_info_event(self):
        logger.info("刷新信息")
        res = self.sqlite.get_find_list("select web_name from web_password")
        self.web_combox["value"] = [i[0] for i in res]
