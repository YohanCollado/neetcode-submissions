class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        squared = []

        for num in nums:
            new_val = num * num
            squared.insert(0, new_val)
        squared.sort()
        return squared
        