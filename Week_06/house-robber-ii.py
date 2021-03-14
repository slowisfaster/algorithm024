class Solution:
    def rob(self, nums: List[int]) -> int:
        def sub_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(cur, pre + num), cur
            return cur
        return max(sub_rob(nums[:-1]), sub_rob(nums[1:])) if len(nums) != 1 else nums[0]

