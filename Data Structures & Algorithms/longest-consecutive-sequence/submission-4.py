class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashset = set(nums)
        for i in nums:
            if i-1 not in hashset:
                length = 1
                while (i + length) in hashset:
                    length += 1
                res = max(res, length)
        return res
            