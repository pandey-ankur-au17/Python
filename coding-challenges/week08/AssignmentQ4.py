def findExists(arr):
    temp = False
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i != j and 0 <= i and j < len(arr):
                if arr[i] / 2 == arr[j]:
                    temp = True
    if temp == True:
        return "true"
    else:
        return "false"



if __name__=="__main__":

    arr = [3,1,7,14]

    result = findExists(arr)
    print(result)