"""
@author Stellagosa
@description 3754.连续非零数字并乘以其数字和Ⅰ
@date 7/7/2026 9:10 AM Tuesday
"""


class Solution:
    def sumAndMultply(self, n: int) -> int:
        count, x, temp = 0, 0, 1
        while n > 0:
            mod = n % 10
            if mod != 0:
                x = x + mod * temp
                count += mod
            n //= 10
            temp *= 10
        return x * count
