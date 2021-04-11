class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p = 1
        res = []
        for i in range(n):
            res.append(p)
            p *= nums[i]
        p = 1
        for i in range(n-1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res

