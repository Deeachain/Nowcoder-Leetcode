# -*- coding:utf-8 -*-
"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

题目分析，假设f[i]表示在第i个台阶上可能的方法数。逆向思维。如果我从第n个台阶进行下台阶，下一步有2中可能，一种走到第n-1个台阶，一种是走到第n-2个台阶。所以f[n] = f[n-1] + f[n-2].
那么初始条件了，f[0] = f[1] = 1。
所以就变成了：f[n] = f[n-1] + f[n-2], 初始值f[0]=1, f[1]=1，目标求f[n]
"""


class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 1 or number == 2:
            return number
        first = 1
        second = 2
        for i in range(3, number + 1):
            res = first + second
            first = second
            second = res
        return res

if __name__ == '__main__':
    Solution = Solution()
    print(Solution.jumpFloor(5))