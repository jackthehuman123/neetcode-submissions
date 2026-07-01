class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        short = s1
        long = s2
        if len(s2) < len(s1):
            return False
        s_t = [0] * 26
        for i in range(len(short)):
            s_t[ord(short[i]) - ord('a')] += 1
        l = 0
        l_g = [0] * 26
        for i in range(len(long)):
            l_g[ord(long[i]) - ord('a')] += 1
            if (i - l + 1) == len(short):
                if l_g == s_t:
                    return True
                else:
                    l_g[ord(long[l]) - ord('a')] -= 1
                    l += 1
        return False
