# -*- coding:utf-8 -*-
"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.minValue = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.minValue:
            self.minValue.append(node)
        elif self.minValue[-1] > node:
            self.minValue.append(node)
        elif self.minValue[-1] < node:
            self.minValue.append(self.minValue[-1])

    def pop(self):
        # write code here
        if self.stack == []:
            return None
        self.minValue.pop()
        return self.stack.pop()

    def top(self):
        # write code here
        if self.stack == []:
            return None
        return self.stack[-1]

    def min(self):
        # write code here
        if self.minValue == []:
            return None
        return self.minValue[-1]
