class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i, j]
        # return []
        # above method is O(n^2);
        # need to be doing at least O(n)? how?
        # now we need to find a target, and we can easily find the difference 
        # so we populate a dictionary wuth the difference and if the difference is exisitng then we can 
        # return the solution or else we can return false
        # lets make a dictionary of the diffMap

        seen = {}
        for idx, num in enumerate(nums):
            difference = target - num
            if difference in seen:
                return [seen[difference], idx]
            seen[num] = idx
        return []

