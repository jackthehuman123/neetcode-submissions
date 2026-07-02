import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        l = r = 0
        while r < k - 1:
            heapq.heappush(heap, (-1 * nums[r], r))
            r += 1
        # stop one before so that the window is 1 element short
        re = []
        for i in range(r, len(nums)):            
            heapq.heappush(heap, (-1 * nums[i], i))
            
            while heap[0][1] < l:
                heapq.heappop(heap)

            m, m_idx = heap[0]
            re.append(-1 * m)

            l += 1
        return re

            