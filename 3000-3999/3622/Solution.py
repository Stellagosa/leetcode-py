"""
@author Stellagosa
@description 3622.判断整除性
@date 8/22/2026 10:57 AM Saturday
"""
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_dig, mult_dig, temp = 0, 1, n
        while temp > 0:
            dig = temp % 10
            sum_dig += dig
            mult_dig *= dig
            temp //= 10
        return n % (sum_dig + mult_dig) == 0
