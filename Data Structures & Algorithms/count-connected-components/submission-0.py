class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for i in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        state = [0] * n
        def dfs(node):
            state[node] = 1
            for nei in graph[node]:
                if state[nei] == 0:
                    dfs(nei)
        
        comps = 0
        for i in range(n):
            if state[i] == 0:
                dfs(i)
                comps += 1
        
        return comps
