"""
@author Stellagosa
@description 2744.最大字符串匹配数目
@date 8/15/2026 10:22 PM Saturday
"""
from typing import List

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        temp = set()
        res = 0
        for word in words:
            if word[::-1] in temp:
                res += 1
                temp.remove(word[::-1])
            else:
                temp.add(word)
        return res



    # def maximumNumberOfStringPairs(self, words: List[str]) -> int:
    #     temp = set()
    #     res = 0
    #     for word in words:
    #         ch = word[1]+word[0]
    #         if ch in temp:
    #             res += 1
    #             temp.remove(ch)
    #         else:
    #             temp.add(word)
    #     return res
