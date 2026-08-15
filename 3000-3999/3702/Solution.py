"""
@author Stellagosa
@description 3702.按位异或非零的最长子序列
@date 8/15/2026 8:22 AM Saturday
"""
from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        is_all_zero = True
        xor = 0
        for num in nums:
            xor ^= num
            if is_all_zero:
                is_all_zero = num == 0
        if is_all_zero:
            return 0
        elif xor == 0:
            return n - 1
        else:
            return n


