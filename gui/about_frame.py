from tkinter import Frame, Text, DISABLED
from loguru import logger


class about_frame(Frame):
    def __init__(self, root):
        super().__init__(master=root)
        logger.info("显示-关于界面")

        self.text = "【软件名称：】密码管理器version1.0.1\n\n" \
                    "【软件开发者：】lys\n\n" \
                    "【软件内容：】\n" \
                    "          1、网站，账号，密码的录入和查询\n" \
                    "          2、该软件目前没有加密措施，只适用于个人的密码管理\n" \
                    "          3、其他开发者都可以在此基础上进行二次开发\n" \
                    "          4、禁止进行商业用途\n" \
                    "          5、使用该软件产生的后果本人不承担任何法律和道德的责任\n\n" \
                    "【版本：】1.0.1"

        self.setup_ui()

    def setup_ui(self):
        about_info = Text(self)
        about_info.pack()
        about_info.insert(0.0, self.text)
        about_info.config(state=DISABLED)  # 禁止修改
