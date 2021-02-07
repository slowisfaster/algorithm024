class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #return nums.sort(key=lambda x: x == 0)
        if not nums:
            return []
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        for j in range(slow, len(nums)):
            nums[j] = 0
        return nums
