# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
 

# Follow up: Could you find an algorithm that runs in O(m + n) time?

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)

        required = len(need)

        left = 0
        formed = 0

        window = {}

        min_len = float("inf")
        min_start = 0

        for right in range(len(s)):

            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            while left <= right and formed == required:

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                left_char = s[left]

                window[left_char] -= 1

                if (
                    left_char in need
                    and window[left_char] < need[left_char]
                ):
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[min_start:min_start + min_len] 

s = "ADOBECODEBANC"
t = "ABC"
sul = Solution()
print("the result is:",sul.minWindow(s,t))