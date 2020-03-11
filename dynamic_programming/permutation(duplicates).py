class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        for num in nums:
            new_permutation = [[]]
            for i in new_permutation:
                for j in range(len(i)+1):
                    new_permutations.append(i[:j] + [num] + i[j:])
                    if len(new_permutation) == len(nums):
                        permutations.append()
