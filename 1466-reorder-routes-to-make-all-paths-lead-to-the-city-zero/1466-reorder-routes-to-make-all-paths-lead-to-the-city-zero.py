class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visited = [False] * n
        for a, b in connections:
            adj[a].append((b, 1))
            adj[b].append((a, 0))

        cost = 0
        def dfs(node):
            nonlocal cost   # 함수 외부 변수는 nonlocal
            visited[node] = True
            for n, c in adj[node]:
                if not visited[n]:
                    dfs(n)
                    cost += c
        dfs(0)
        return cost