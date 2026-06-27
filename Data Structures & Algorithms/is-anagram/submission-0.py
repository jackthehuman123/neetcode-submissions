class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {};
        hashmap2 = {};
        for i in s:
            if i not in hashmap1:
                hashmap1[i] = 1
            else:
                hashmap1[i] += 1

        for i in t:
            if i not in hashmap2:
                hashmap2[i] = 1
            else:
                hashmap2[i] += 1
        
        return (hashmap1 == hashmap2)