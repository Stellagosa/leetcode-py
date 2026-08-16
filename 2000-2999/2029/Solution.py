"""
@author Stellagosa
@description 2029.石子游戏Ⅸ
@date 8/16/2026 8:17 AM Sunday
"""
from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0] * 3
        for num in stones:
            cnt[num % 3] += 1
        if cnt[0] % 2== 0:
            return cnt[1] >= 1 and cnt[2] >= 1
        return cnt[1] - cnt[2] > 2 or cnt[2] - cnt[1] > 2

