class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words) -1 ):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        
        visited = {}
        res = []

        def dfs(n):
            if n in visited:
                return visited[n]
            visited[n] = True
            for nei in adj[n]:
                if dfs(nei):
                    return True
            visited[n] = False
            res.append(n)
            return False
        
        for i in adj:
            if dfs(i):
                return ""
        
        res.reverse()
        return "".join(res)