from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        length = 0

        for count in freq.values():
            length += (count // 2) * 2

        if length < len(s):
            length += 1

        return length