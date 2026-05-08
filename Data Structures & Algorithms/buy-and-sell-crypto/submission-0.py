class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        currMin = prices[0]
        for i in prices:
            if currMin < i:
                ans = max(ans, i - currMin)
            else:
                currMin = i
        return ans