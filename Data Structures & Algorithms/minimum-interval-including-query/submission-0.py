import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sort_int = sorted(intervals)
        heap = []
        res, i = {}, 0
        
        for q in sorted(queries):
            while i < len(sort_int) and sort_int[i][0] <= q:
                l, r = sort_int[i]
                heapq.heappush(heap, (r - l + 1, r))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            res[q] = heap[0][0] if heap else -1
        
        return [res[q] for q in queries]
