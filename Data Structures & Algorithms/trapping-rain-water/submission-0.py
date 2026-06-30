class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = [0] * len(height)
        cur_max_l = height[0]
        for i in range(len(height)):
            max_l[i] = cur_max_l
            if height[i] > cur_max_l:
                cur_max_l = height[i]
        # Find height around each index
        max_h = [0] * len(height)
        cur_max_r = height[len(height) - 1]
        for i in range(len(height) - 1, -1, -1):
            max_h[i] = min(max_l[i], cur_max_r)
            if height[i] > cur_max_r:
                cur_max_r = height[i]
        # Calculating volume
        volume = [0] * len(height)
        for i in range(len(height)):
            cur = max_h[i] - height[i]
            if cur > 0:
                volume[i] = cur
            else:
                volume[i] = 0
        return sum(volume)