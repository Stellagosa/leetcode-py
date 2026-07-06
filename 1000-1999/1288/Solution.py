"""
@author Stellagosa
@description 1288.删除被覆盖区间
@date 7/6/2026 10:07 AM Monday
"""

from typing import List


class Solution:
    # def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    #     temp = []
    #     for i in range(len(intervals)):
    #         flag = False
    #         for j in range(len(intervals)):
    #             if i != j:
    #                 if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
    #                     flag = True
    #                     break
    #         if not flag:
    #             temp.append(intervals[i])
    #     return len(temp)

    # def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    #     intervals.sort(key=lambda x: (x[0], x[1]))
    #     temp = []
    #     n = len(intervals)
    #     for i in range(n - 1):
    #         if intervals[i][0] == intervals[i + 1][0]:
    #             continue
    #         flag = False
    #         for t in temp:
    #             if t[1] >= intervals[i][1]:
    #                 flag = True
    #                 break
    #         if not flag:
    #             temp.append(intervals[i])
    #     for t in temp:
    #         if t[1] >= intervals[n - 1][1]:
    #             return len(temp)
    #     return len(temp) + 1

    # def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
    #     intervals.sort(key=lambda x: (x[0], -x[1]))
    #     pre, pre_max, ans = -1, -1, 0
    #     for i in range(len(intervals)):
    #         if intervals[i][0] == pre:
    #             continue
    #         else:
    #             pre = intervals[i][0]
    #             if intervals[i][1] > pre_max:
    #                 pre_max = intervals[i][1]
    #                 ans += 1
    #     return ans

    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        pre_max, ans = -1, 0
        for i in range(len(intervals)):
            if intervals[i][1] > pre_max:
                pre_max = intervals[i][1]
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
