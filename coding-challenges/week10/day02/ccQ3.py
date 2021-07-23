def longestCommonPrefix(strs):
    
    if not strs:
        return ""

    new_string = sorted(strs)
    for i in range(len(new_string[0])):

        for str in (new_string[1:]):

            if (str[i] != new_string[0][i]) or (i >= len(str)):
                return new_string[0][:i]

    return new_string[0]


strs = ["flower","flow","flight"]
ans = longestCommonPrefix(strs)
print(ans)
