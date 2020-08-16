# -*- coding:utf-8 -*-
"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""


"""
思路：创建一个列表存储链表循环值，链表的值如果出现在列表中，则返回
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        temp = []
        while pHead:
            if pHead in temp:
                return pHead
            temp.append(pHead)
            pHead = pHead.next
        return None