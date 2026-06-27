class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for i in range(numCourses)]
        for u, v in prerequisites:
            g[u].append(v)
        
        visited = [0] * numCourses

        def dfs(node):
            visited[node] = 1
            for nei in g[node]:
                if visited[nei] == 1:
                    return True
                if visited[nei] == 0 and dfs(nei):
                    return True
            visited[node] = 2
            return False
        
        for i in range(numCourses):
            if visited[i] == 0 and dfs(i):
                return False
        return True
                
                    
