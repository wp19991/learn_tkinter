from loguru import logger
import tkinter as tk

from myutil import global_var as gl


class save_frame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        # 变量
        self.web_var = tk.StringVar()
        self.account_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.status_var = tk.StringVar()
        self.status_var.set("状态")

        self.setup_ui()

    def setup_ui(self):
        # 用frame来框住布局
        # pack 有 fill 和 side 参数
        frame_1 = tk.Frame(self)
        frame_1.pack(fill=tk.X, side=tk.TOP)
        tk.Label(frame_1, text="保存录入信息",
                 font=("楷体", 20),  # 设置字体
                 fg="black",  # 字体的颜色
                 ).pack()

        # 创建表单的frame-使用表格布局
        frame_2 = tk.Frame(self)
        frame_2.pack(fill=tk.X, side=tk.TOP)
        tk.Label(frame_2, text="*网站：").grid(row=0, column=0)
        tk.Entry(frame_2, textvariable=self.web_var).grid(row=0, column=1)
        tk.Label(frame_2, text="账号：").grid(row=1, column=0)
        tk.Entry(frame_2, textvariable=self.account_var).grid(row=1, column=1)
        tk.Label(frame_2, text="*密码：").grid(row=2, column=0)
        tk.Entry(frame_2, textvariable=self.password_var).grid(row=2, column=1)

        frame_3 = tk.Frame(self)
        frame_3.pack(fill=tk.X, side=tk.TOP)
        tk.Button(frame_3, text="确定", command=self.save_info_event).pack(side=tk.LEFT)
        tk.Label(frame_3, textvariable=self.status_var).pack(side=tk.RIGHT)

    def save_info_event(self):
        logger.info("保存信息")
        web_name = self.web_var.get()
        account = self.account_var.get()
        password = self.password_var.get()
        DM = gl.get_value("DM")
        DM.write_data(web_name, account, password)
        self.status_var.set("保存成功")
