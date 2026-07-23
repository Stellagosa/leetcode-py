"""
@author Stellagosa
@description 不同 XOR 三元组的数目Ⅰ
@date 7/23/2026 8:47 PM Thursday
"""
from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        return len(nums) if len(nums) < 3 else (1 << len(nums).bit_length())
