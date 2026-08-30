class MinStack:

    def __init__(self):
        self.value = []
        self.prefix = []

    def push(self, val: int) -> None:
        if not self.value:
            self.value.append(val)
            self.prefix.append(float('inf'))
        else:
            self.prefix.append(min(self.value[-1], self.prefix[-1]))
            self.value.append(val)

    def pop(self) -> None:
        self.prefix.pop()
        self.value.pop()

    def top(self) -> int:
        # self.prefix.pop()
        return self.value[-1]

    def getMin(self) -> int:
        return min(self.prefix[-1], self.value[-1])
