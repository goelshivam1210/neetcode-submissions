class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # a solution can be to make a frequency map of the elelemnts
        # and then we search 
        # in the map for the top k 
        frequency_map = defaultdict(int)
        count = [[] for _ in range(len(nums)+1)]

        for num in nums:
            frequency_map[num] +=1

        for key, value in frequency_map.items():
            count[value].append(key)

        result = []
        for i in range(len(count)-1, 0, -1):
            for num in count[i]:
                result.append(num)
                if len(result) == k:
                    return result

            


        
        # sort the values
        # sorted_values = sorted(frequency_map.values(), reverse = True)
        # return sorted_values[:k]

