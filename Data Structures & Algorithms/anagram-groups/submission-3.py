class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list)
        for word in strs:
            wordMap[tuple(sorted(word))].append(word)
        
        return list(wordMap.values())