class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = [[None] * 2 for i in nums]
        def dfs(i, flag):
            if i == len(nums):
                return 0 if flag else float("-inf")
            if flag:
                res = max(0, nums[i] + dfs(i+1, flag))
                memo[i][flag] = res
                return res
            res = max(dfs(i+1, False), nums[i] + dfs(i+1, True))
            memo[i][flag] = res
            return res

        return dfs(0, False)