import tkinter as tk
from tkinter.ttk import Combobox

from loguru import logger

from myutil import global_var as gl


class sql_test_frame(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        # 变量


        self.setup_ui()

    def setup_ui(self):
        pass