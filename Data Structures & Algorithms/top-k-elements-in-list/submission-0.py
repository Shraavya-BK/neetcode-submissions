class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums) #creates a frequency map and stores the numbers
        return [num for num, _ in freq.most_common(k)] #extracts only the numbers from the top k freq and ignores the counts