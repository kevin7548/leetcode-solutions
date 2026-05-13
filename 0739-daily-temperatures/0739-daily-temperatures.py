class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # (temp, i)
        answer = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, j = stack.pop()
                answer[j] = i - j
            stack.append((t, i))
        return answer