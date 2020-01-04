class Solution:
    def __init__(self):
        self.result = []

    def subsets(self, nums: list, sub_set=[]) -> list:
        self.result.append(sub_set)
        for i in range(len(nums)):
            self.subsets(nums[i + 1:], sub_set + [nums[i]])

        return self.result


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
