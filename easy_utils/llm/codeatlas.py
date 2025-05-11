#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""生成代码摘要"""

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
import os
import ast

# 项目模块

# 外部模块
import numpy


# 代码块

def extract_definitions(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            tree = ast.parse(f.read(), filename=file_path)
        except SyntaxError:
            return []
    definitions = []
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef):
            methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
            definitions.append({'type': 'class', 'name': node.name, 'methods': methods})
        elif isinstance(node, ast.FunctionDef):
            definitions.append({'type': 'function', 'name': node.name})
    return definitions


def walk_directory(base_dir):
    project_structure = []
    for root, dirs, files in os.walk(base_dir):
        rel_root = os.path.relpath(root, base_dir)
        for file in files:
            if file.endswith('.py') and file != '__init__.py':
                file_path = os.path.join(root, file)
                defs = extract_definitions(file_path)
                project_structure.append({
                    'path': os.path.join(rel_root, file),
                    'definitions': defs
                })
    return project_structure


def write_overview(structure, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('# Project Overview\n\n')
        f.write('## Module Tree\n\n')
        for item in structure:
            f.write(f"- {item['path']}\n")
        f.write('\n## Core Classes and Functions\n\n')
        for item in structure:
            f.write(f"### {item['path']}\n")
            for d in item['definitions']:
                if d['type'] == 'class':
                    f.write(f"- class {d['name']}\n")
                    for m in d['methods']:
                        f.write(f"    - method {m}()\n")
                elif d['type'] == 'function':
                    f.write(f"- function {d['name']}()\n")
            f.write('\n')


if __name__ == "__main__":
    base_dir_list = [
        r'E:\code\github\data_utils\data_utils\stochastic_utils\vdistributions',
        r'E:\code\github\etrade\etrade'
    ]
    for BASE_DIR in base_dir_list:
        FILE_NAME = BASE_DIR.split("\\")[-1]
        OUTPUT_FILE = f'{FILE_NAME}.md'

        structure = walk_directory(BASE_DIR)
        write_overview(structure, OUTPUT_FILE)
        print(f"Overview written to {OUTPUT_FILE}")
