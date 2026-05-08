class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0
        for i in hashset:
            if (i-1) not in hashset:
                length = 1
                while (i+length) in hashset:
                    length += 1
                res = max(res, length)
        return res
            