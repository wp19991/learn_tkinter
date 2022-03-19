from loguru import logger
import tkinter as tk

from myutil import global_var as gl


class main_frame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)
        self.setup_ui()

    def setup_ui(self):
        # 用frame来框住布局
        # pack 有 fill 和 side 参数
        frame_1 = tk.Frame(self)
        frame_1.pack(fill=tk.X, side=tk.TOP)
        tk.Label(frame_1, text="欢迎界面",
                 font=("楷体", 20),  # 设置字体
                 fg="black",  # 字体的颜色
                 ).pack()
