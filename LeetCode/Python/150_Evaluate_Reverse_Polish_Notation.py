class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        ret = 0
        for token in tokens:
            if token.isnumeric():
                stack.append(int(token))
            elif len(token) > 1 and token[1:].isdigit():
                stack.append(-int(token[1:]))
            else:
                if len(stack) == 1:
                    return stack[0]            
                op = token
                x = stack.pop()
                y = stack.pop()
                if op == '+':
                    stack.append(y+x)
                elif op == '-':
                    stack.append(y-x)
                elif op == '*':
                    stack.append(y*x)
                elif op == '/':
                    abs_x = x if x>0 else -x
                    abs_y = y if y>0 else -y
                    if (x > 0 and y > 0) or (x < 0 and y < 0):
                        stack.append(y//x)
                    else:
                        stack.append(-(abs_y//abs_x))
        return stack[0]        