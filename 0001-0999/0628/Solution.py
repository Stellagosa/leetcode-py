"""
@author Stellagosa
@description 628. 三个数的最大乘积
@date 7/26/2026 9:17 PM Sunday
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max_1, max_2, max_3, min_1, min_2 = -1001, -1001, -1001, 1001, 1001
        for num in nums:
            if num > max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = num
            elif num > max_2:
                max_3 = max_2
                max_2 = num
            elif num > max_3:
                max_3 = num
            if num < min_1:
                min_2 = min_1
                min_1 = num
            elif num < min_2:
                min_2 = num

        return max(max_1 * max_2 * max_3, max_1 * min_1 * min_2)
