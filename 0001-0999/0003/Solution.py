"""
@author Stellagosa
@description 3.无重复字符的最长子串
@date 7/6/2026 4:31 PM Monday
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n
        f, max_len, begin = {}, 0, -1
        for i in range(n):
            # (begin, i]是一个无重复字符子串
            # f.get(s[i], -1) 获取该字符上一次出现位置，没出现返回-1
            begin = max(f.get(s[i], -1), begin)
            # (begin,i]的长度为 i-begin
            max_len = max(max_len, i - begin)
            # 更新字符s[i]的位置
            f[s[i]] = i
        return max_len

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     n = len(s)
    #     if n < 2:
    #         return n
    #     map, max_len, begin = {}, 0, -1
    #     for i in range(len(s)):
    #         if s[i] in map:
    #             max_len = max(max_len, i - begin - 1)
    #             begin = max(map[s[i]], begin)
    #             map[s[i]] = i
    #         else:
    #             map[s[i]] = i
    #     return max(max_len, n - begin - 1)
