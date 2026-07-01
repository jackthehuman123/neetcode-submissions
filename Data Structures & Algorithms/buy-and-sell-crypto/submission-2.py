class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_max = 0
        max_p = 0
        for i in range(len(prices) - 1, -1, -1):
            cur_price = prices[i]
            cur_p = cur_max - prices[i]
            max_p = max(cur_p, max_p)
            cur_max = max(cur_price, cur_max)
        return max_p