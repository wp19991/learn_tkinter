import os.path
import sys


def resource_path(relative_path):
    # 在打包的时候用到这个函数
    if "config.py" in os.listdir(os.getcwd()):
        return relative_path
    # 已经打包完成的话就提供缓存地址
    base_path = getattr(sys, '_MEIPASS',
                        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
