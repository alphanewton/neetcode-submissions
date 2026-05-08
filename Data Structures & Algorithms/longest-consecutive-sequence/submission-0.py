class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        ans = 0
        for i, n in enumerate(nums):
            map[n] = i
        for i, n in enumerate(nums):
            if (n-1) not in map:
                streak = 1
                curr = n
                while i  < len(nums) and (curr+1) in map:
                    streak += 1
                    curr += 1

                ans = max(ans, streak)
                
        return ans