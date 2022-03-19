import tkinter as tk
from tkinter import Tk
from loguru import logger

from gui.about_frame import about_frame
from gui.main_frame import main_frame
from gui.save_frame import save_frame
from gui.search_frame import search_frame


class main_page:
    def __init__(self, master: Tk):
        self.root = master
        self.root.title("密码管理器")
        # 大小为300*300，距离屏幕左边的宽200，距离屏幕顶部的高200
        self.root.geometry("300x300+200+200")
        self.root.iconbitmap('./resources/icon/探测声音.ico')  # 添加图标文件

        # 初始化导航栏
        self.setup_menu_bar()

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

    # 页面切换-保存界面
    def save_interface(self):
        logger.info("页面切换-保存界面")
        self.about_frame.pack_forget()
        self.search_frame.pack_forget()
        self.main_frame.pack_forget()
        self.save_frame.pack()

    # 页面切换-关于界面
    def about_interface(self):
        logger.info("页面切换-关于界面")
        self.save_frame.pack_forget()
        self.search_frame.pack_forget()
        self.main_frame.pack_forget()
        self.about_frame.pack()

    # 页面切换-搜索界面
    def search_interface(self):
        logger.info("页面切换-搜索界面")
        self.save_frame.pack_forget()
        self.about_frame.pack_forget()
        self.main_frame.pack_forget()
        self.search_frame.pack()
