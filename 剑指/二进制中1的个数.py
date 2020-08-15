#  -*- coding: utf-8 -*-
"""
输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。
"""

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        cnt = 0
        for i in range(1, n+1):
            if '1' in str(i):
                cnt += 1
        return cnt

if __name__ == '__main__':
    Solution = Solution()
    print(Solution.NumberOf1Between1AndN_Solution(2593))