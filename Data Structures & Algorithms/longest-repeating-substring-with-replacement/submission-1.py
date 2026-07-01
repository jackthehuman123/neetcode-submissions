class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        cur_most_freq = s[0]
        max_l = 0
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            if count[s[i]] > count[cur_most_freq]:
                cur_most_freq = s[i]
            freq = count[cur_most_freq]
            length = i - l + 1
            re = length - freq
            while re > k:
                count[s[l]] -= 1 # Decrement before changing l
                l += 1
                length = i - l + 1
                re = length - freq
            max_l = max(max_l, length)
        return max_l 