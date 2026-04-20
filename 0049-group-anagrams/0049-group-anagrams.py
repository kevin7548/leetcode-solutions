from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)   # {기준: [문자열]}
        for string in strs:
            key = tuple(sorted(string))
            str_dict[key].append(string)

        return list(str_dict.values())