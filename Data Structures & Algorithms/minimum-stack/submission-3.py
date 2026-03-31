class MinStack:


    def __init__(self):
        
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min) == 0 or val <= self.min[len(self.min) - 1]:
            self.min.append(val)

    def pop(self) -> None:
        popped = self.stack.pop(len(self.stack)-1)
        if popped == self.min[len(self.min) - 1]:
            self.min.pop(len(self.min) - 1)
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min[len(self.min) - 1]
        
