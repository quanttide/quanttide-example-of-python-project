# -*- coding: utf-8 -*-
"""
程序启动入口
此文件是该目录下所有代码的唯一统一入口（如有需要可改名）
如有其它需单独运行的简单脚本，在项目根目录下创建 `scripts` 文件夹
如有多个不能一起完成的交付目标（里程碑）
在项目根目录下新创建文件夹及其自己的 `__main__.py` 等文件
"""
import logging

from config import init_logging

init_logging()
LOGGER = logging.getLogger(__name__)


def main():
    pass


if __name__ == '__main__':
    main()
