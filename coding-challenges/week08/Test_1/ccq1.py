def Segment_check(a,N,M):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i==j and a[i][j] == a[i+1][j+1]:
                print("YES")
                return "YES"
            elif a[i][j] != a[i+1][j+1]:  
                print("NO")
                return "NO"
            
            
first_multiple_input = input().rstrip().split()

N= int(first_multiple_input[0])

M= int(first_multiple_input[1])

a=[]
for i in range(N):
    arr=list(map(int,input().split()))
    a.append(arr)
    
Segment_check(a,N,M)


##########################################################
def Max_occurence(a, n):
    left = dict()

    count = dict()
    max1 = 0

    min1, start = 0, 0

    for i in range(n):
        list1 = a[i]
        if (list1 not in count.keys()):
            left[list1] = i
            count[list1] = 1
        else:
            count[list1] += 1

        if (count[list1] > max1):
            max1 = count[list1]
            min1 = i - left[list1] + 1
            start = left[list1]
            
        elif (count[list1] == max1 and
            i - left[list1] + 1 < min1):
            min1 = i - left[list1] + 1
            start = left[list1]
    ans = 0
    for i in range(start, start + min1):
        ans += 1
    return ans
n= int(input())
arr = list(map(int, input().split()))
print(Max_occurence(arr, n))






##########################################3




def Uniq_count(str, N):
    A = {}
    List1 = []
    count_char = 0
 
    for i in range(N):
        A[str[i]] = A.get(str[i], 0) + 1
        
    for it in A:
        List1.append(A[it])
 
    List1 = sorted(List1)
     
    
    while (len(List1) > 0):

        frequent = List1[-1]
        del List1[-1]
        if (len(List1) == 0):
            return count_char
             
        if (frequent == List1[-1]):
            if (frequent > 1):
                List1.append(frequent - 1)
                 
        
            count_char += 1
             
        List1 = sorted(List1)
         
    return count_char
n = input()
a = len(n)
print(Uniq_count(n,a))






    #####################################################################

def changeString(S):
         
    # Store the given String
    N = len(S)
    s = [' '] * (len(S))
     
    for i in range(len(S)):
        s[i] = S[i]
 
    # If the first character is '?'
    if (s[0] == '?'):
        s[0] = 'a'
         
        if (s[0] == s[1]):
            s[0] = chr(ord(s[0]) + 1)
 
    # Traverse the String [1, N - 1]
    for i in range(1, N - 1):
         
        # If the current
        # character is '?'
        if (s[i] == '?'):
             
            # Change the character
            s[i] = 'a'
 
            # Check equality with
            # the previous character
            if (s[i] == s[i - 1]):
                s[i] =  chr(ord(s[i]) + 1)
 
            # Check equality with
            # the next character
            if (s[i] == s[i + 1]):
                s[i] =  chr(ord(s[i]) + 1)
 
            # Check equality with
            # the previous character
            if (s[i] == s[i - 1]):
                s[i] =  chr(ord(s[i]) + 1)
 
    # If the last character is '?'
    if (s[N - 1] == '?'):
         
        # Change character
        s[N - 1] = 'a'
         
        # Check with previous
        # character
        if (s[N - 1] == s[N - 2]):
            s[N - 1] += 1
 
    ans = ""
    for i in range(len(s)):
        ans += s[i]
         
    # Return the resultant String
    return ans
 
# Driver Code
if __name__ == '__main__':
     
    # Given String S
    S = "?a?a"
 
    # Function Call
    print(changeString(S))





#https://www.hackerrank.com/contests/kalam-may-month-test/challenges