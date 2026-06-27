class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0] * 26
        for c in s:
            alpha[ord('z') - ord(c)] += 1
        for c in t:
            alpha[ord('z') - ord(c)] -= 1
        return all(x == 0 for x in alpha)