"""
@author Stellagosa
@description 3532.针对图的路径存在性查询Ⅰ
@date 7/10/2026 12:49 PM Friday
"""
from typing import List


class Solution:

    # 断开的时候下标加1
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        tags = [0] * n
        for i in range(1, n):
            tags[i] = tags[i - 1] + (1 if nums[i] - nums[i - 1] > maxDiff else 0)
        return [tags[x] == tags[y] for x, y in queries]


    # 断开的时候用下标i做标记
    # def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
    #     tags = [0] * n
    #     for i in range(1, n):
    #         if nums[i] - nums[i - 1] <= maxDiff:
    #             tags[i] = tags[i - 1]
    #         else:
    #             tags[i] = i
    #
    #     res = [False] * len(queries)
    #     for i in range(len(queries)):
    #         res[i] = tags[queries[i][0]] == tags[queries[i][1]]
    #     return res