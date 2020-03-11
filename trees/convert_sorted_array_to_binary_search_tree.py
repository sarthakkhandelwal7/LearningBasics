# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def helper(from_index, to_index, nums):
            mid = int((from_index+to_index)/2)
            if from_index == to_index:
                return None
            node = TreeNode(nums[mid])
            node.left = helper(from_index, mid, nums)
            node.right = helper(mid+1, to_index, nums)
            return node
        return helper(0, len(nums), nums)


if __name__ == '__main__':
    Solution().sortedArrayToBST([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
