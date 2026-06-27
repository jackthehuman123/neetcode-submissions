class Solution:

    def encode(self, strs: List[str]) -> str:
        en = []
        for s in strs:
            en.append(len(s))
            en.append("#")
            en.append(s)
        return "".join(map(str, en))
    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            start = j + 1
            end = start + l
            res.append(s[start : end])
            i = end
        return res