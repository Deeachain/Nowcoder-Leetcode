# -*- coding:utf-8 -*-
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""


class Solution:
    # 初始化
    def __init__(self):
        self.stack = []
        # 存储最小元素
        self.minValue = []
    # 压栈
    def push(self, node):
        self.stack.append(node)

        # 维护当前最小的数组
        if self.minValue:
            if self.minValue[-1] > node:
                self.minValue.append(node)
            else:
                self.minValue.append(self.minValue[-1])
        else:
            self.minValue.append(node)
    # 出栈
    def pop(self):
        if self.stack == []:
            return None
        self.minValue.pop()
        return self.stack.pop()
    # 获取栈顶
    def top(self):
        if self.stack == []:
            return None
        return self.stack[-1]
    def min(self):
        if self.minValue == []:
            return None
        return self.minValue[-1]