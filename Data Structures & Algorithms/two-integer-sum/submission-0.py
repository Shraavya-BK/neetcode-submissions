class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen={}

        for i, num in enumerate(nums):  #enumerate(nums) → gives index and value for each number in the list
            complement = target - num  #complement is the number we have to pair with the num so that on subtracting we get the target
            if complement in seen:
                return[seen[complement],i]
            seen[num]=i

        