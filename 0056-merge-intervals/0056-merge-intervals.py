class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for start, end in intervals[1:]:    # 리스트 슬라이싱은 인덱싱 에러 X, 그냥 빈 리스트로 루프 통과
            if start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        return result
