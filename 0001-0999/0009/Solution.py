"""
@author Stellagosa
@description 回文数
@date 7/23/2026 9:02 PM Thursday
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        arr = []
        while x > 0:
            arr.append(x % 10)
            x //= 10

        for i in range(len(arr) // 2):
            if arr[i] != arr[len(arr) - 1 - i]:
                return False
        return True
