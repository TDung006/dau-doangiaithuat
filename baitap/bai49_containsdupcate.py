class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
     
        from collections import defaultdict
        
        anagram_map = defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(word))  # sorted string as key
            anagram_map[key].append(word)
        
        return list(anagram_map.values())
   