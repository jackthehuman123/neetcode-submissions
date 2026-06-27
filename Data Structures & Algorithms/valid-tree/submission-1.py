class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = [[] for i in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        def detectCycle(node, parent):
            visited.add(node)
            for child in graph[node]:
                if child == parent:
                    continue
                if child in visited:
                    return True
                if detectCycle(child, node):
                    return True
            return False
        
        if detectCycle(0, -1):
            return False
        return len(visited) == n