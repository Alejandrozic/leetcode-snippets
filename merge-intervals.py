# 56. Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an 
# array of the non-overlapping intervals that cover all the intervals in the input.

# https://leetcode.com/problems/merge-intervals

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        
        output = [intervals[0]]

        for start, end in intervals:
            last_start, last_end = output[-1]
            if start <= last_end:
                output[-1][0] = last_start if last_start < start else start
                output[-1][1] = last_end if last_end > end else end
            else:
                output.append([start, end])
        
        return output
