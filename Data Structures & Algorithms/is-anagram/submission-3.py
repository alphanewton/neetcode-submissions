class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charMap = defaultdict(int)
        for i in range(len(s)):
            charMap[s[i]] += 1
            charMap[t[i]] -= 1
        
        return  not any(x!=0 for x in list(charMap.values()))
