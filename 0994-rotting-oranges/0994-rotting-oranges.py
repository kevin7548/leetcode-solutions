from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        max_t, fresh_count = 0, 0

        # 1. rotten orange 찾기 & fresh orange 세기
        q = deque([])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # 2. multi-source BFS
        while q:
            r, c, t = q.popleft()
            max_t = max(t, max_t)
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0<=nr<R and 0<=nc<C and grid[nr][nc] == 1:
                    q.append((nr, nc, t+1))
                    grid[nr][nc] = 2
                    fresh_count -= 1

        return max_t if fresh_count == 0 else -1

        