class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)
        for n in nums:
            countMap[n] += 1
        countMap = dict(sorted(countMap.items(), key=lambda item: item[1], reverse=True))

        return list(countMap.keys())[:k]
