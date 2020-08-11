# -*- coding:utf-8 -*-
'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
不能使用除法。（注意：规定B[0] = A[1] * A[2] * ... * A[n-1]，B[n-1] = A[0] * A[1] * ... * A[n-2];）
'''


class Solution:
    def multiply(self, A):
        # write code here
        B = [1] * len(A)
        for index1, array1 in enumerate(A):
            for index2, array2  in enumerate(A):
                if not index1 == index2:
                    B[index1] *=array2
        return B


if __name__ == '__main__':
    Solution = Solution()
    print(Solution.multiply([1, 2, 3]))
