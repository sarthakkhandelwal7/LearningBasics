class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a