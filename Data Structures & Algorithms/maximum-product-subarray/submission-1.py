class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        A = []
        curr = []
        res = max(nums)

        for i in nums:
            if i == 0:
                if curr:
                    A.append(curr)
                curr = []
            else:
                curr.append(i)
        
        if curr:
            A.append(curr)
        
        for sub in A:
            neg_count = sum(1 for i in sub if i < 0)
            prod = 1 
            need = neg_count if neg_count%2==0 else neg_count - 1
            neg_count = 0
            j = 0
            for i in range(len(sub)):
                prod *= sub[i]
                if sub[i] < 0:
                    neg_count += 1
                    while neg_count > need:
                        prod //= sub[j]
                        if sub[j] < 0:
                            neg_count -= 1
                        j+= 1
                if j<= i:
                    res = max(res, prod)
        return res
            