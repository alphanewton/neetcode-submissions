class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n-2):
            j = i + 1
            k = n - 1
            
            while j < k:
                curr = nums[j] + nums[k]
                if curr + nums[i] == 0:
                    res.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                elif curr + nums[i] < 0:
                    j += 1
                else:
                    k -= 1
        return list(res)