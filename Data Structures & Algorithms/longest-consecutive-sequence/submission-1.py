class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seen = set(nums)
        longest = 1
        for i in range(len(nums)):
            cur_len = 1
            cur = nums[i]
            while cur - 1 in seen:
                cur_len += 1
                cur -= 1
            longest = max(cur_len, longest)
        return longest