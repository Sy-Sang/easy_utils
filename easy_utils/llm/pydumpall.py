#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""根据tree便利py文件生成提示词"""

__author__ = "Sy,Sang"
__version__ = ""
__license__ = "GPLv3"
__maintainer__ = "Sy, Sang"
__email__ = "martin9le@163.com"
__status__ = "Development"
__credits__ = []
__date__ = ""
__copyright__ = ""

# 系统模块
import copy
import pickle
import json
from typing import Union, Self
from collections import namedtuple
import re
import os

# 项目模块

# 外部模块
import numpy

# 代码块

root_dir = r'E:\code\github\etrade'
input_txt = 'output.txt'
output_file = 'etrade.txt'

# output_file = "combined_output.txt"

# 用于存储所有代码内容
all_code = []

# 遍历目录
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith('.py') and filename != '__init__.py':
            file_path = os.path.join(dirpath, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                    all_code.append(f"### File: {file_path}\n")
                    all_code.append(code)
                    all_code.append("\n\n")  # 文件间加个空行分隔
            except Exception as e:
                print(f"无法读取文件 {file_path}: {e}")

# 写入到输出文件
with open(output_file, 'w', encoding='utf-8') as out_f:
    out_f.writelines(all_code)

print(f"所有 .py 文件内容已写入 {output_file}")

if __name__ == "__main__":
    pass
