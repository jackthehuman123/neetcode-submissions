class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        res = []
        # Lock a complement of the triplet
        # and find the two sums like Two Sum II
        for i in range(len(sort)):
            # Searching on the right side of i
            if i > 0 and sort[i] == sort[i - 1]:
                continue # Skip duplicates of locked value
            l = i + 1 
            r = len(sort) - 1
            while l < r:
                target = 0 - sort[i]
                if sort[l] + sort[r] > target:
                    r -= 1
                elif sort[l] + sort[r] < target:
                    l += 1
                else:
                    res.append([sort[l],sort[r],sort[i]])
                    l += 1
                    r -= 1

                    while l < r and sort[l] == sort[l - 1]:
                        # Skip duplicates for l and r
                        # Since changing l would also cause r
                        # to change
                        l += 1
        return res