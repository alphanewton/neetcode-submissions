class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, n in enumerate(nums):
            left = target - n
            if left in hashmap:
                return [hashmap[left], i]
            hashmap[n] = i
        
        return []