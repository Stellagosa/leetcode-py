"""
@author Stellagosa
@description 3345. 最小可整除数位乘积Ⅰ
@date 8/6/2026 8:52 PM Thursday
"""

class Solution:

    def smallestNumber(self, n: int, t: int) -> int:
        def digit_mult(num: int) -> int:
            if num == 0:
                return 0
            temp = num
            mult = 1
            while temp > 0:
                mult *= temp % 10
                temp //= 10
            return mult

        while digit_mult(n) % t != 0:
            n += 1
        return n


    # def smallestNumber(self, n: int, t: int) -> int:
    #     while self.digit_mult(n) % t != 0:
    #         n += 1
    #     return n
    # @staticmethod
    # def digit_mult(n: int) -> int:
    #     if n == 0:
    #         return 0
    #     temp = n
    #     mult = 1
    #     while temp > 0:
    #         mult *= temp % 10
    #         temp //= 10
    #     return mult