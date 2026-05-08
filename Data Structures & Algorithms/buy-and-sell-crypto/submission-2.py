class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        res = 0
        for j in range(1, len(prices)):
            if prices[j] < minPrice:
                minPrice = prices[j]
            
            res = max(res, prices[j] - minPrice)
        return res