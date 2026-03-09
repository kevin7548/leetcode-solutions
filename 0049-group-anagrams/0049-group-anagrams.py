from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        answer = []

        for str in strs:
            key = ''.join(sorted(str))
            dict[key].append(str)

        return list(dict.values())