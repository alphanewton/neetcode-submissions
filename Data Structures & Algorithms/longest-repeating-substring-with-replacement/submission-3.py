class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        i = 0
        maxfreq = 0
        res = 0
        for j in range(len(s)):
            hashmap[s[j]] += 1
            maxfreq = max(maxfreq, hashmap[s[j]])
            while (j - i + 1) - maxfreq > k:
                hashmap[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
        return res