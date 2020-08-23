# -*- coding:utf-8 -*-
"""
给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1，m<=n），每段绳子的长度记为k[1],...,k[m]。
请问k[1]x...xk[m]可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
"""

"""
思路
    由题意得 target>=4
    * target=4, 最优解：2 2
    * target=5, 最优解：3 2
    * target=6, 最优解：3 3
    * target=7, 最优解：3 2 2
    * target=8, 最优解：3 3 2
    * target=9, 最优解：3 3 3
    * target=10,最优解：3 3 2 2
    * target=11,最优解：3 3 3 2
    * target=12,最优解：3 3 3 3
    * target=13,最优解：3 3 3 2 2
    * target=14,最优解：3 3 3 3 2
    * target=15,最优解：3 3 3 3 3
    *
    * 所以不难发现3和2的个数规律
"""


class Solution:
    def cutRope(self, number):
        # write code here
        num3 = number // 3
        if number % 3 == 1:
            num3 -= 1
        num2 = (number - 3 * num3) // 2
        return pow(3, num3) * pow(2, num2)
