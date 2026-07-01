class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        t_count = {}
        for i in range(len(t)):
            t_count[t[i]] = t_count.get(t[i], 0) + 1
        s_count = {}
        l = 0
        matches = 0
        required = len(t_count)
        ans = (float('inf'), 0, 0) # better than string slicing
        for i in range(len(s)):
            if s[i] in t_count:
                s_count[s[i]] = s_count.get(s[i], 0) + 1
                if t_count[s[i]] == s_count[s[i]]:
                    matches += 1

            while matches == required:
                if (i - l + 1) < ans[0]:
                    ans = (i - l + 1, l, i)

                if s[l] in t_count:
                    s_count[s[l]] -= 1
                    if s_count[s[l]] < t_count[s[l]]:
                        matches -= 1
                
                l += 1

        return s[ans[1] : ans[2] + 1] if ans[0] != float('inf') else ""