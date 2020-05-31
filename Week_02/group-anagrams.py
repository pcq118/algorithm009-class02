class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        lookup = defaultdict(list)
        for s in strs:
            lookup["".join(sorted(s))].append(s)
        return list(lookup.values())