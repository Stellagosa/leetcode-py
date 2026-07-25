"""
@author Stellagosa
@description 3536. 两个数字的最大乘积
@date 7/25/2026 7:49 PM Saturday
"""
class Solution:

    def maxProduct(self, n: int) -> int:
        max_1, max_2 = 0, 0
        while n > 0:
            dig = n % 10
            if dig > max_1:
                max_2 = max_1
                max_1 = dig
            elif dig > max_2:
                max_2 = dig
            n = n // 10
        return max_1 * max_2




    # def maxProduct(self, n: int) -> int:
    #     arr = []
    #     while n > 0:
    #         arr.append(n % 10)
    #         n = n // 10
    #     res = -1
    #     for i in range(0, len(arr) - 1):
    #         for j in range(i + 1, len(arr)):
    #             res = res if res > arr[i] * arr[j] else arr[i] * arr[j]
    #     return res
