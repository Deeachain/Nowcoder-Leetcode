# -*- coding:utf-8 -*-
"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
class Solution:
    # 二分查找法
    # 有序的数组中使用
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return None
        left = 0
        right = len(rotateArray) - 1
        while left <= right:
            middle = (left + right) >> 1
            # middle 比两边的都小，说明是最小值
            if rotateArray[middle] < rotateArray[middle - 1]:
                return rotateArray[middle]
            # 说明右边递增，则最小在左边
            elif rotateArray[middle] < rotateArray[right]:
                right = middle - 1
            else:
                left = middle + 1
        return 0