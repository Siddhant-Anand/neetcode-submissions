class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }
        for i in tokens:
            if i.lstrip("-").isdigit():
                stack.append(int(i))
            else:
                num1=stack.pop()
                num2=stack.pop()
                ans=operations[i](num2, num1)
                stack.append(ans)
        return stack[0]