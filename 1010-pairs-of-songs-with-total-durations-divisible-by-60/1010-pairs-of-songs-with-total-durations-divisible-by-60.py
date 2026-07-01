from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        answer = 0
        duration = defaultdict(int)   # {나머지: 개수} 0<=t<60 인덱스에 대한 리스트 만드는 것 비효율적
        for i, t in enumerate(time):
            complement = (60 - t % 60) % 60
            if complement in duration:
                answer += duration[complement]
            duration[t % 60] += 1
        return answer