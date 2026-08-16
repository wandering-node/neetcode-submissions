class MinStack:
    def __init__(self):
        self.value = []
        self.prefix_min = []

    def push(self, val: int) -> None:
        
        if self.prefix_min:
            self.prefix_min.append(min(self.prefix_min[-1], self.value[-1]))
        else:
            self.prefix_min.append(float('inf'))
        self.value.append(val)


    def pop(self) -> None:
        self.value.pop()
        self.prefix_min.pop()

    def top(self) -> int:
        return self.value[-1]

    def getMin(self) -> int:
        return min(self.value[-1], self.prefix_min[-1])
        
