class Solution:
    @staticmethod
    def multiply(n: int, m: int, i=0) -> int:
        if m == 0:
            return 0

        if m & 1 == 0:
            return 0 + Solution.multiply(n, m >> 1, i+1)

        return Solution.multiply(n, m >> 1, i + 1) + n << i


if __name__ == '__main__':
    print(Solution().multiply(12, 5))
