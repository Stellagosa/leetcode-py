"""
@author Stellagosa
@description 1386.安排电影院座位
@date 8/19/2026 9:38 AM Wednesday
"""
from typing import List


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        map = {}
        for seat in reservedSeats:
            if (seat[1] > 1) and (seat[1] < 10):
                origin = map.get(seat[0], 0)
                map[seat[0]] = origin | (1 << (seat[1] - 2))

        res = (n - len(map)) * 2
        for value in map.values():
            if ((value | 0b00001111) == 0b00001111) or ((value | 0b11110000) == 0b11110000) or (
                    (value | 0b11000011) == 0b11000011):
                res += 1
        return res
