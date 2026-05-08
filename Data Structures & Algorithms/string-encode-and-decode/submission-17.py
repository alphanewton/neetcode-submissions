class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "None"
        return "#NEWT#".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        res = s.split("#NEWT#")
        return [""] if res == [] else res