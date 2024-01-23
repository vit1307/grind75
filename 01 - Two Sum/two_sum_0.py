class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            for ii in range(i + 1, len(nums)):
                if nums[ii] +  nums[i] == target:
                    return [i, ii]
                    