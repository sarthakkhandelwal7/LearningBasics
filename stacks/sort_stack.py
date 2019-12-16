class SortStack:
    @staticmethod
    def sort(stack: list) -> list:
        temp_stack = []
        while stack:
            num = stack.pop()
            while len(temp_stack) and num > temp_stack[-1]:
                stack.append(temp_stack.pop())
            temp_stack.append(num)
        return temp_stack


if __name__ == '__main__':
    sortstack = SortStack()
    print(sortstack.sort([34, 3, 31, 98, 92, 23]))
