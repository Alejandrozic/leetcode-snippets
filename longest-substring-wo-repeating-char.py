# 3. Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # O(n)
        prev_i = {}
        left = 0
        count = 0
        for i, char in enumerate(s):
            if char in prev_i and prev_i[char] >= left:
                left = prev_i[char] + 1
            prev_i[char] = i
            current_len = i - left + 1
            if current_len > count:
                count = current_len
        return count
