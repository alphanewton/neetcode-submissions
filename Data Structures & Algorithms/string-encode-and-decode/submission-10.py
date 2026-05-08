class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        return "@,".join(strs) + "#"

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        s = s[:len(s)-1]
        return s.split("@,")
