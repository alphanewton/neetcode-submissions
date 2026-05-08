class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for i in strs:
            map[tuple(sorted(i))].append(i)
        return list(map.values())
