class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxA = 0
        # w = r - l
        while l < r:
            left = heights[l]
            right = heights[r]
            h = min(left, right)
            curA = h * (r - l)
            maxA = max(maxA, curA)
            if left > right:
                r -= 1
            else:
                l += 1
        return maxA