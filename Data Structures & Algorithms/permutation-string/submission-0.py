class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        short = s1
        long = s2
        if len(s2) < len(s1):
            return False
        s_t = {}
        for i in range(len(short)):
            s_t[short[i]] = s_t.get(short[i], 0) + 1
        l = 0
        l_g = {}
        for i in range(len(long)):
            l_g[long[i]] = l_g.get(long[i], 0) + 1
            if (i - l + 1) == len(short):
                if l_g == s_t:
                    return True
                else:
                    l_g[long[l]] -= 1
                    if l_g[long[l]] == 0:
                        del l_g[long[l]]
                    l += 1
        return False
