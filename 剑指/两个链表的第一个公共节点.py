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

        # 假设输入的两个链表，是同一个链表
        if pHead1 == pHead2:
            return pHead1

        pTmp1 = pHead1
        pTmp2 = pHead2

        # 我们通过循环，让其中一个节点走到最后
        while pTmp1 and pTmp2:
            pTmp1 = pTmp1.next
            pTmp2 = pTmp2.next

        # 判断哪个链表先走到最后
        # 假设pTmp1，还没有走完，说明pTmp2是更短的
        if pTmp1:
            k = 0
            # 寻找链表长度之间的差值
            while pTmp1:
                pTmp1 = pTmp1.next
                k += 1
            # 我们让pTmp1先跳N步
            pTmp2 = pHead2
            pTmp1 = pHead1
            for i in range(k):
                pTmp1 = pTmp1.next

            # 当找到节点相等的时候，也就是说明该节点是公共节点
            while pTmp1 != pTmp2:
                pTmp1 = pTmp1.next
                pTmp2 = pTmp2.next
            return pTmp1

        # 假设pTmp2，还没有走完，说明pTmp1是更短的
        if pTmp2:
            k = 0
            while pTmp2:
                pTmp2 = pTmp2.next
                k += 1
            # 我们让pTmp2先跳N步
            pTmp2 = pHead2
            pTmp1 = pHead1
            for i in range(k):
                pTmp2 = pTmp2.next

            while pTmp1 != pTmp2:
                pTmp1 = pTmp1.next
                pTmp2 = pTmp2.next
            return pTmp1
