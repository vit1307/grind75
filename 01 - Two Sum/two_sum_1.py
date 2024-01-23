class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        subs = dict()
        
        for i, num in enumerate(nums):
            if num in subs:
                return [i, subs[num]]
            
            subs[target - num] = i
        
        return []