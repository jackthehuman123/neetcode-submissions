class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sell = [0] * len(prices)
        cur_max = 0
        for i in range(len(prices) - 1, -1, -1):
            max_sell[i] = cur_max
            if prices[i] > cur_max:
                cur_max = prices[i]
        for i in range(len(prices)):
            prices[i] = max_sell[i] - prices[i]
        max_p = max(prices) if max(prices) > 0 else 0
        return max_p