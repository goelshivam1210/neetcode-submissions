class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # brute force
        # for idx1 in range(len(numbers)):
        #     for idx2 in range(idx1+1, len(numbers)):
        #         if numbers[idx1] + numbers[idx2] == target:
        #             return [idx1+1, idx2+1]

        # better solution has to do with two pointers
        left_ptr = 0 # first element
        right_ptr = len(numbers) - 1 # last element

        while (left_ptr < right_ptr):
            if numbers[left_ptr] + numbers[right_ptr] == target:
                return [left_ptr+1, right_ptr+1]
            elif numbers[left_ptr] + numbers[right_ptr] < target:
                left_ptr += 1
            else:
                right_ptr -= 1
                

        