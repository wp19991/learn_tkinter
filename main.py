from tkinter import Tk

from loguru import logger

from gui.main_page import main_page
from myutil import global_var as gl
from myutil import logs
import config

if __name__ == "__main__":
    gl.__init()
    logs.__init()
    config.__init()
    root = Tk()
    main_page(root)
    logger.info("进入主界面")
    root.mainloop()
