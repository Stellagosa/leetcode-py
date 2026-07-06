"""
@author Stellagosa
@description 1.两数之和
@date 7/6/2026 9:23 AM Monday
"""

from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(len(nums)):
    #             if i != j and nums[i] + nums[j] == target:
    #                 return [i, j]
    #     return [0, 0]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, v in enumerate(nums):
            if target - v in temp:
                return [i, temp[target - v]]
            temp[v] = i
        return [0, 0]


arr = [1, 3, 5, 6]
if __name__ == "__main__":
    print(Solution().twoSum(arr, 8))
