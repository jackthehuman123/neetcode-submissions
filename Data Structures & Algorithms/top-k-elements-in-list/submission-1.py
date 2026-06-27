class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1
        n = len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, v in hashmap.items():
            buckets[v].append(key)
        
        re = []
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                re.append(num)
                if len(re) == k:
                    return re