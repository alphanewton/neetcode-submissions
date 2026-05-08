class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(arr):
            rob1, rob2 = 0, 0
            for i in arr:
                temp = max(i + rob2, rob1)
                rob2 = rob1
                rob1 = temp
            return rob1
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))