class Solution:
    def generate(num: int):
        pasc = []
        c = 0
        while num > 0:
            if c == 0:
                pasc.append([1])
                num -= 1
                c += 1
            elif c == 1:
                pasc.append([1,1])
                num -= 1
                c += 1
            else:
                l = [1]
                for i in range(1, len(pasc[-1])):
                    l.append(pasc[-1][i-1] + pasc[-1][i])
                l.append(1)
                pasc.append(l)
                num -=1
        return pasc
    n=int(input("Number:"))
    print(generate(n))