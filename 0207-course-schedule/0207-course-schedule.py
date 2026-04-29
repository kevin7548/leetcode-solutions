from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 초기 세팅
        graph = defaultdict(list)   # {선수과목: [과목들]}
        in_degree = [0] * numCourses

        # 초기값 대입
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1
        
        # queue
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0
        
        while queue:
            count += 1
            node = queue.popleft()
            for i in graph[node]:
                #** 선수과목을 모두 들어야 큐에 추가 **#
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

        return numCourses == count
