# -*- coding:utf-8 -*-
"""
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,
当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},
连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)
"""



class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        sum = 0
        sum_list = []
        for i in array:
            sum += i
            sum_list.append(sum)
            if sum > 0:
                continue
            else:
                sum = 0
        return max(sum_list)


"""
下面介绍动态规划的做法，复杂度为 O(n)。
步骤 1：令状态 dp[i] 表示以 A[i]作为末尾的连续序列的最大和（这里是说 A[i] 必须作为连续序列的末尾）。
步骤 2：做如下考虑：因为 dp[i] 要求是必须以 A[i] 结尾的连续序列，那么只有两种情况：
这个最大和的连续序列只有一个元素，即以 A[i] 开始，以 A[i] 结尾。
这个最大和的连续序列有多个元素，即从前面某处 A[p] 开始 (p<i)，一直到 A[i] 结尾。
对第一种情况，最大和就是 A[i] 本身。
对第二种情况，最大和是 dp[i-1]+A[i]。
于是得到状态转移方程：
dp[i] = max{A[i], dp[i-1]+A[i]}
"""

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        N = len(array)
        dp = array[0]
        max_sum = dp
        for i in range(1, N):
            dp = max(array[i], array[i] + dp)
            max_sum = max(max_sum, dp)
        return max_sum


if __name__ == '__main__':
    Solution = Solution()
    print(Solution.FindGreatestSumOfSubArray([6, -3, -2, 7, -15, 1, 2, 2]))
