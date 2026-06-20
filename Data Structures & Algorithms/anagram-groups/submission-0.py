class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force solution is 
        # sort all the elements
        # and then group the same ones together.
        # sorted_strs = ["".join(sorted(s)) for s in strs]
        # this now has all the sorted elements in a list
        # now how do i group them using a hash map?
        # 
        # make a dictionary in which you first sort the elements, and add an entry 
        # then if the entry exisits, okay, add the element

        # sorted_dict = defaultdict(list)

        # for element in strs:
        #     sorted_element = "".join(sorted(element))
        #     sorted_dict[sorted_element].append(element)
        # return list(sorted_dict.values())

        # a better solution here is that we can make keys for the 
        # 0-26 elements 
        # and that way we dont need to sort each time we are traversing the entry
        # this way it will be better
        # as the complexity for the k log k will be gone 0t will 
        # be m times n
        # so for this we need each key of the 

        groups = defaultdict(list)

        for element in strs:        
            count = [0] * 26
            for char in element:
                count[ord(char) - ord("a")] += 1
            groups[tuple(count)].append(element)
        
        return list(groups.values())






