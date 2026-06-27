class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = [0] * 26
        for i in s:
            alpha[ord(i) - ord('a')] += 1
        for i in t:
            alpha[ord(i) - ord('a')] -= 1
        return all(x == 0 for x in alpha)