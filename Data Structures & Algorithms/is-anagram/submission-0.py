class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # make two dicts using the two lists
        # and then compare the dicts. 
        # since dicts are unordered so
        # it will work

        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for element in s:
            s_dict[element]+=1
        for element in t:
            t_dict[element]+=1
        if t_dict == s_dict:
            return True
        else:
            return False        