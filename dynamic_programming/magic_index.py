class Solution:
    @staticmethod
    def find_magic_index(data: list, start: int, end: int) -> int:
        # Cell of list whose index is same as its data
        # values are not distinct and array is sorted
        mid_index = int((start + end)/2)
        if mid_index == data[mid_index]:
            return mid_index
        if start > end or start < 0 or end < 0:
            return -1

        # Search left
        left_index = min(mid_index - 1, data[mid_index])
        left = Solution.find_magic_index(data, start, left_index)
        if left >= 0:
            return left

        # Search right
        right_index = max(mid_index + 1, data[mid_index])
        right = Solution.find_magic_index(data, right_index, end)
        return right


if __name__ == '__main__':
    print(Solution().find_magic_index([-10, -5, 1, 2, 2, 3, 4, 7, 9, 12, 13], 0, 11))
