from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses    # 들어야 하는 선수과목 수
        graph = defaultdict(list)   # 선수과목: [과목]
        queue = deque()
        result = []

        for a, b in prerequisites:
            graph[b].append(a)
            indeg[a] += 1

        for idx in range(numCourses):
            if indeg[idx] == 0:
                queue.append(idx)
                result.append(idx)

        while queue:
            prereq = queue.popleft()
            for course in graph[prereq]:
                indeg[course] -= 1
                if indeg[course] == 0:
                    queue.append(course)
                    result.append(course)

        return result if len(result) == numCourses else []