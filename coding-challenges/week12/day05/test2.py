def max_idx_pref():
    sum = 0
    idx = -1
    for i in range(len(arr)):
        sum = sum + arr[i]
        if sum > k:
            idx = i -1
            break
    if idx == -1:
        return -1
    else:
        return idx

n, k = input().split()
arr = list(map(int, input().split()))
n = int(n)
k = int(k)        
print(max_idx_pref())