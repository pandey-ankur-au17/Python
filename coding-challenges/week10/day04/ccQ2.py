def baseballGame(ops):
    
    stack = []
    temp = 0

    for op in ops:

        if op == "C":
            temp -= stack.pop()
        elif op == 'D':
            stack.append(2*stack[-1])
            temp += stack[-1]
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
            temp += stack[-1]
        else:
            stack.append(int(op))
            temp += stack[-1]

    return temp


if __name__ == "__main__":

    ops = ["5","2","C","D","+"]
    ans = baseballGame(ops)
    print(ans)
