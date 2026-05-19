from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. 목표 문자열 t
        target = Counter(t)  # 목표 문자들
        total_count = len(target)    # 만족 문자 수
        
        # 2. 슬라이딩 윈도우
        seen = defaultdict(int)   # 현재 윈도우 문자 {문자: 개수}
        count = 0

        min_len = float('inf')
        ans_l, ans_r = 0, 0
        left = 0

        # 3. right 확장하며 탐색
        for right, char in enumerate(s):
            seen[char] += 1
            if seen[char] == target[char]: # char 개수 만족시
                count += 1
            
            # 4. 조건 만족 시 left 당기기
            while count == total_count:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    ans_l, ans_r = left, right
                
                seen[s[left]] -= 1
                if seen[s[left]] < target[s[left]]:
                    count -= 1
                
                left += 1

        return s[ans_l:ans_r + 1] if min_len != float('inf') else ""

# min_len을 통해 길이만 비교, 인덱스 저장 후 최종적으로 슬라이싱 마지막에.