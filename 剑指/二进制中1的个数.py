#  -*- coding: utf-8 -*-
"""
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。
"""
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        flag = 1
        for i in range(32):
            if n & flag !=0:
                count+=1
            flag <<= 1
        return count


if __name__ == '__main__':
    Solution = Solution()
    print(Solution.NumberOf1(5))

