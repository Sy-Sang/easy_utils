#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""根据目录遍历 .py 文件生成提示词"""

__author__ = "Sy,Sang"
__version__ = ""
__license__ = "GPLv3"
__maintainer__ = "Sy, Sang"
__email__ = "martin9le@163.com"
__status__ = "Development"
__credits__ = []
__date__ = ""
__copyright__ = ""

import os

if __name__ == "__main__":
    # 只需要指定根目录
    root_dir_list = [
        r'E:\code\github\data_utils\data_utils\stochastic_utils\vdistributions',
        r'E:\code\github\etrade\etrade'
    ]
    for root_dir in root_dir_list:
        file_name = root_dir.split("\\")[-1]
        output_file = f'{file_name}_source_code.txt'

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
                            all_code.append("\n\n")  # 文件间加空行
                    except Exception as e:
                        print(f"无法读取文件 {file_path}: {e}")

        # 写入到输出文件
        with open(output_file, 'w', encoding='utf-8') as out_f:
            out_f.writelines(all_code)

        print(f"所有 .py 文件内容已写入 {output_file}")