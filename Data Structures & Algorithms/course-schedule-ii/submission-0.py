from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        in_deg = [0] * numCourses
        for crs, preq in prerequisites:
            graph[preq].append(crs)
            in_deg[crs] += 1

        q = deque()
        for i in range(numCourses):
            if in_deg[i] == 0:
                q.append(i)

        res = []
        while q:
            crs = q.popleft()
            res.append(crs)
            for preq in graph[crs]:
                in_deg[preq] -= 1
                if in_deg[preq] == 0:
                    q.append(preq)
        
        return res if len(res) == numCourses else []        