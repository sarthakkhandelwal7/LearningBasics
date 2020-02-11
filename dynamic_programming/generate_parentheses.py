class Solution:
    @staticmethod
    def generateParenthesis(n: int) -> List[str]:
        ans = []

        def helper(temp: str, open_paren: int, closed_paren: int):
            if len(temp) == 2 * n:
                ans.append(temp)

            if open_paren < n:
                helper(temp + '(', open_paren + 1, closed_paren)

            if closed_paren < open_paren:
                helper(temp + ')', open_paren, closed_paren + 1)

        helper('', 0, 0)
        return ans
