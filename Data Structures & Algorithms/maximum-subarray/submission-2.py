class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        currSum = 0
        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            res = max(res, currSum)
        return res