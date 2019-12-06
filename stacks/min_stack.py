class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []

    def push(self, x: int) -> None:
        self.min_stack.append((x, self.getMin(x)))

    def pop(self) -> None:
        self.min_stack.pop()

    def top(self) -> int:
        return self.min_stack[len(self.min_stack) - 1][0]

    def getMin(self, x=None) -> int:
        if x is not None and (len(self.min_stack) is 0 or self.min_stack[len(self.min_stack) - 1][1] > x):
            return x
        else:
            return self.min_stack[len(self.min_stack) - 1][1]


def main():
    minstack = MinStack()
    minstack.push(0)
    minstack.push(1)
    minstack.push(0)
    print(minstack.getMin())
    print(minstack.getMin())


if __name__ == "__main__":
    main()
