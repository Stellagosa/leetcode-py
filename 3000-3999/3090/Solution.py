"""
@author Stellagosa
@description 3090. 每个字符最多出现两次的最长子字符串
@date 8/14/2026 2:03 PM Friday
"""
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        temp = [0] * 26
        n = len(s)
        max_len = 0
        i, j = 0, 0
        while j < n:
            index_j = ord(s[j]) - ord('a')
            temp[index_j] += 1
            while temp[index_j] > 2:
                index_i = ord(s[i]) - ord('a')
                temp[index_i] -= 1
                i += 1
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len
