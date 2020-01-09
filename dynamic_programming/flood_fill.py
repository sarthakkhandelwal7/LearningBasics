class Solution:
    @staticmethod
    def flood_fill(image: list[list[]], sr: int, sc: int, new_color: int) -> list[list[]]:
        def utility(image, r, c, old, new):
            if len(image) > r >= 0 and len(image[0]) > c >= 0:
                if image[r][c] != old or image[r][c] == new:
                    return None
                else:
                    image[r][c] = new

                utility(image, r - 1, c, old, new)
                utility(image, r, c - 1, old, new)
                utility(image, r + 1, c, old, new)
                utility(image, r, c + 1, old, new)

            else:
                return None

        utility(image, sr, sc, image[sr][sc], new_color)
        return image


if __name__ == '__main__':
    print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))