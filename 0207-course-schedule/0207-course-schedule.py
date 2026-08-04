from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses    # 들어야하는 선수과목 수
        graph = defaultdict(list)   # {선수과목: [과목]}
        queue = deque()
        
        # graph, indeg
        for a, b in prerequisites:  # a:과목, b: 선수과목
            graph[b].append(a)
            indeg[a] += 1

        # queue
        for idx in range(numCourses):
            if indeg[idx] == 0:
                queue.append(idx)

        while queue:
            i = queue.popleft()
            for c in graph[i]:
                indeg[c] -= 1
                if indeg[c] == 0:
                    queue.append(c)

        return indeg == [0] * numCourses