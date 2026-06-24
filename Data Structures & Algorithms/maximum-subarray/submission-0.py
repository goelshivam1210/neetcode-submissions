class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # using kadane's algorithm approach 
        # can reduce it to O(n)
        # how?
        # so the insight is that every single sub array will end at an index
        # so every index we have two choice, either take this array further
        # or end here, so we check the max here and maintain two sums
        # current sum and max_sum

        max_sum = -math.inf
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum+num)
            max_sum = max(current_sum, max_sum)

        return max_sum