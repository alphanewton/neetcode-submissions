class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = defaultdict(list)
        for s in strs:
            charArr = [0] * 26
            for c in s:
                charArr[ord(c) - ord("a")] += 1
            resMap[tuple(charArr)].append(s)
        return list(resMap.values())
            