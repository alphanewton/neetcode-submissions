class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            if not preMap[node]:
                return True
            visiting.add(node)
            for pre in preMap[node]:
                if not dfs(pre):
                    return False
            visiting.remove(node)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
