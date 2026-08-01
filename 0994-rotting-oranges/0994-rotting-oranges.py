from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        cur_fr, total_fr = 0, 0
        minutes = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    total_fr += 1
        
        while queue and cur_fr < total_fr:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        queue.append((nx, ny))
                        grid[nx][ny] = 2
                        cur_fr += 1
            minutes += 1
        
        return minutes if cur_fr == total_fr else -1