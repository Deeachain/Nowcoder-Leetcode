#  -*- coding: utf-8 -*-
"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""


"""
思路：总结规律 f[n] = f[n-1] + f[n-2]，初始条件f[1] = 1, f[2] =2
"""
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0 or number == 1 or number == 2:
            return number
        a = 1
        b = 2
        for i in range(3, number + 1):
            out = a + b
            a = b
            b = out
        return out


if __name__ == '__main__':
    Solution = Solution()
    print(Solution.rectCover(3))