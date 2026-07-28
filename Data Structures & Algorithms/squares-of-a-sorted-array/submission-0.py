class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        storage = []

        for num in nums:
            new_val = num * num
            storage.insert(0, new_val)
        storage.sort()
        return storage
            
        