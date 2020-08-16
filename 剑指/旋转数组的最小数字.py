# -*- coding:utf-8 -*-
"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


"""
思路：二分查找
"""
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if rotateArray ==None:
            return 0
        left, right = 0, len(rotateArray)-1
        while left < right:
            mid = (left + right) >> 1
            if rotateArray[mid] < rotateArray[right]:
                right = mid
            elif rotateArray[mid] > rotateArray[right]:
                left = mid+1
            else:
                right -= 1
        return rotateArray[left]


if __name__ == '__main__':
    Solution = Solution()
    print(Solution.minNumberInRotateArray([6501, 6828, 6963, 7036, 7422, 5725, 6300, 6335]))
