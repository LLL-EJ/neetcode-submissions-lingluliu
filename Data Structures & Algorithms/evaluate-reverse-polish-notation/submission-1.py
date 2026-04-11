class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for token in tokens:
            if token in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(self.apply_op(token, a, b))
            else:
                stack.append(int(token))
        
        return stack[0]
        
    
    def apply_op(self, op, a, b):
        if op == "+":
            return a + b
        elif op == "-":
            return b - a
        elif op == "*":
            return a * b
        elif op == "/":
            return int(b / a)
