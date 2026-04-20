from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)   # {기준: [문자열]}
        for string in strs:
            key = tuple(sorted(string))
            seen[key].append(string)

        return list(seen.values())