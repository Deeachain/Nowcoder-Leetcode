# -*- coding:utf-8 -*-
"""
输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 == pHead2:
            return pHead1
        p1 = pHead1
        p2 = pHead2
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
        if p1:
            # 寻找链表长度之间的差值
            k = 0
            while p1:
                p1 = p1.next
                k += 1
            # 让p1先跳K步
            for i in range(k):
                pHead1 = pHead1.next
            while pHead1 and pHead2:
                if pHead1 == pHead2:
                    return pHead1
                pHead1 = pHead1.next
                pHead2 = pHead2.next
        if p2:
            k = 0
            while p2:
                p2 = p2.next
                k += 1
            for i in range(k):
                pHead2 = pHead2.next
            while pHead1 and pHead2:
                if pHead1 == pHead2:
                    return pHead1
