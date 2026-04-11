class MinStack:

    def __init__(self):
        self.stack = []
        self.prefix = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.prefix[-1] if self.prefix else val)
        self.prefix.append(val)
        

    def pop(self) -> None:
        del self.prefix[-1]
        del self.stack[-1]
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.prefix[-1] 
        
