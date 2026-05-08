class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, resLen = [-1, -1], float("infinity")
        countT, countCurr = defaultdict(int), defaultdict(int)
        for c in t:
            countT[c] += 1
        have, need = 0, len(countT)
        l = 0
        for r in range(len(s)):
            countCurr[s[r]] += 1
            if s[r] in countT and countT[s[r]] == countCurr[s[r]]:
                have += 1
            while need == have:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = [l, r]
                countCurr[s[l]] -= 1
                if s[l] in countT and countCurr[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if resLen != float("infinity") else ""
