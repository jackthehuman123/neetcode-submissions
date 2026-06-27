class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = 26 * [0]
    
        for a in s:
            counter[ord(a) - ord('a')] += 1
        for b in t:
            counter[ord(b) - ord('a')] -= 1    

        return all(x == 0 for x in counter)
