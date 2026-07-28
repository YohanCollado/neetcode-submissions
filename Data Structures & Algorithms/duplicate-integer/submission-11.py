class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seenThat = set()

        for num in nums:
            if num in seenThat:
                return True
            seenThat.add(num)
        return False