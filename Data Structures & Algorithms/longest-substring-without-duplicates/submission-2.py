class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0 
        max_l = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[i])
            max_l = max(max_l, (i - l + 1))
        return max_l