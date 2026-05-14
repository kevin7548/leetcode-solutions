class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        left, right = [], []
        for start, end in intervals:
            if newInterval[0] > end:
                left.append([start, end])
            elif start > newInterval[1]:
                right.append([start, end])
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
        
        return left + [newInterval] + right