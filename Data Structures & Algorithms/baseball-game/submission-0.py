class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "+":
                a, b = stack[-1], stack[-2]
                stack.append(a + b)
            elif i == "D":
                stack.append(stack[-1] * 2)
            elif i == "C":
                stack.pop()
            else:
                stack.append(int(i))

        res = 0
        while stack:
            res += stack.pop()
        return res
            
        