from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        answer = 0
        duration = defaultdict(list)   # {나머지: [인덱스]}
        for i, t in enumerate(time):
            complement = (540 - t) % 60
            if complement in duration:
                answer += len(duration[complement])
            duration[t % 60].append(i)
        return answer