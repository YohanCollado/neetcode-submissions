class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        duplicateNumber = set()

        for number in nums:
            if number in duplicateNumber:
                return True
            duplicateNumber.add(number)
        return False