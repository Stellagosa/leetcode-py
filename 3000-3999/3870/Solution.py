"""
@author Stellagosa
@description 3870.统计范围内的逗号
@date 9/8/2026 8:46 AM Tuesday
"""

class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        if n < 1000000:
            return n - 999
        if n < 1000000000:
            return 2 * (n - 999999) + 999000
        return 3 * (n - 999999999) + 999000000 + 999000
