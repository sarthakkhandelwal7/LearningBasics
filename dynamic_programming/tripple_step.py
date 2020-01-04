class Solution:
    @staticmethod
    def climbStairs(n: int) -> int:
        count = [None] * (n + 1)

        def utility(num: int, count: list) -> int:
            if num == 0:
                return 1
            elif num < 0:
                return 0
            if count[num]:
                return count[num]
            count[num] = utility(num - 1, count) + utility(num - 2, count) + utility(num - 3, count)
            return count[num]

        return utility(n, count)
