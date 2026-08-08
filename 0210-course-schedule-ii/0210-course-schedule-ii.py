from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indeg = [0] * numCourses    # 필요한 선이수과목 수
        graph = defaultdict(list)   # 선이수: [과목]
        queue = deque()
        order = []

        for a, b in prerequisites:  # b: 선이수, a: 과목
            graph[b].append(a)
            indeg[a] += 1
        
        for course in range(numCourses):
            if indeg[course] == 0:
                queue.append(course)
                order.append(course)

        while queue:
            prereq = queue.popleft()
            for c in graph[prereq]:
                indeg[c] -= 1
                if indeg[c] == 0:
                    queue.append(c)
                    order.append(c)

        return order if indeg == [0] * numCourses else []