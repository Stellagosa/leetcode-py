"""
@author Stellagosa
@description 3014. 输入单词需要的最少按键次数Ⅰ
@date 7/30/2026 9:48 AM Thursday
"""


class Solution:

    def minimunPushes(self, word: str) -> int:
            n = len(word)
            return (n // 8) * (4 * (n // 8) + 4) + (n % 8) * ((n // 8) + 1)

    # def minimumPushes(self, word: str) -> int:
    #     n = len(word)
    #     res, k  = 0, 1
    #     while n > 0:
    #         res += k * min(8, n)
    #         n -= 8
    #         k += 1
    #     return res
