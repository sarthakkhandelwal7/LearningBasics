class Solution:
    def __init__(self):
        self.permutations = []

    def permute(self, temp: list, sets=[]) -> list:
        if temp == []:
            self.permutations.append(sets)
            return self.permutations
        for i in range(len(temp)):
            self.permute([item for item in temp if item != temp[i]], sets + [temp[i]])
        return self.permutations


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
