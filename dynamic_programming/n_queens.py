class Solution:
    @staticmethod
    def solveNQueens(n: int):
        result = []

        def dfs(queen, sum_coordinates, diff_coordinates):
            p = len(queen)
            if p == n:
                result.append(queen)
                return None
            for q in range(n):
                if q not in queen and p + q not in sum_coordinates and p - q not in diff_coordinates:
                    dfs(queen + [q], sum_coordinates + [p + q], diff_coordinates + [p - q])

        dfs([], [], [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in pos] for pos in result]


if __name__ == '__main__':
    print(Solution().solveNQueens(4))
