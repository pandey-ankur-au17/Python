def isValidParentheses(s):
    
    stack = []
    temp = {"(":")","{":"}","[":"]"}

    for char in s:

        if char in temp:
            stack.append(char)
        elif stack:
            if temp[stack.pop()] != char:
                return False
        else:
            return False

    return len(stack) == 0


if __name__ == "__main__":

    s = []
    ans = isValidParentheses(s)
    print(ans)