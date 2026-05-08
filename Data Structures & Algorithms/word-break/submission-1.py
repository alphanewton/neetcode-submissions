class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}
        def dfs(i):
            if i == len(s):
                return True
            if i in memo:
                return memo[i]
            
            for w in words:
                if s[i: i+len(w)] == w:
                    if dfs(i+len(w)):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)