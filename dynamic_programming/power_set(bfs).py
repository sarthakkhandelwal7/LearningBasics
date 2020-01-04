class Solution:
    @staticmethod
    def subsets(nums: list) -> list:
        result = [[]]
        for num in nums:
            result += [sub_set + [num] for sub_set in result]

        return result


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))