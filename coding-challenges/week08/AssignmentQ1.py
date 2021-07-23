def upperbound(A, target):
    n = len(A)
    prev = -1
    for i in range(n - 1, -1, -1):
        if target == A[i]:
            return i
        elif target > A[i]:
            return prev
        prev = i


if __name__ == "__main__":

    A = [1,1,1,2,2,2,3,3,4]
    x = 2
    print("upper bound :", upperbound(A, x))
