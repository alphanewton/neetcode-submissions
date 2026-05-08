class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, arr, x):
            if i == len(nums) or x > target:
                return
            if x == target:
                res.append(arr.copy())
                return

            arr.append(nums[i])
            dfs(i, arr, x + nums[i])
            arr.pop()
            dfs(i+1, arr, x)
        
        dfs(0, [], 0)
        return list(res)