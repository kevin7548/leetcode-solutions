from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses    # 안 들은 선수과목 수
        graph = defaultdict(list)   # 선수과목: [과목]
        queue = deque()
        taken = 0

        for a, b in prerequisites:  # a: 과목 b: 선수과목
            graph[b].append(a)
            indeg[a] += 1

        for idx in range(len(indeg)):
            if indeg[idx] == 0:
                queue.append(idx)
                taken += 1
        
        while queue:
            course = queue.popleft()
            for c in graph[course]:
                indeg[c] -= 1
                if indeg[c] == 0:
                    queue.append(c) # 선수과목 다 들은 것만 큐에
                    taken += 1

        return taken == numCourses