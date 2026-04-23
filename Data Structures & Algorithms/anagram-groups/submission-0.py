class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) #defauultdict is a Dictionary where each key automatically starts with an empty list
        
        for word in strs: #loop through every word in strs
            key = ''.join(sorted(word)) #sort characters in the word which will become the key for a word with similar characters/letters
            groups[key].append(word) #group these keys together
        return list(groups.values()) #return the list of all the groups