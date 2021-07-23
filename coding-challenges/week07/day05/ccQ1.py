# 1. Write a program using recursion to count the number of
# vowels in a string.

# def Count_vowels(S):

#     count=0

#     for i in range(len(S)):

#         if S[i]=="a" or S[i]=="e" or S[i]=="i" or S[i]=="o" or S[i]=="u":
    
#             count=count+1

#     print(count)

# S=input("Enter String to count vowels:")

# Count_vowels(S)

def isVowel(ch):
    return ch.upper() in ['A', 'E', 'I', 'O', 'U']
def countVovels(str, n):
    if (n == 1):
        return isVowel(str[n - 1]);
 
    return (countVovels(str, n - 1) +
                isVowel(str[n - 1]));

str =input("Enter the string to count the vowel:")

print(countVovels(str, len(str)))