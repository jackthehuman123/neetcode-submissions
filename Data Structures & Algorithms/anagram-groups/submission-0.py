class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = {}

        for string in strs:
            counter = [0] * 26
            for i in string:
                counter[ord(i) - ord('a')] += 1
            
            my_tuple = tuple(counter)
            if my_tuple not in hashmap:  
                hashmap[my_tuple] = []
            hashmap[my_tuple].append(string)

        return list(hashmap.values())